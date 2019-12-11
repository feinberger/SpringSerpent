'''Spring.py: This is the python module for interacting with spring jobs

This python module is used to load, create, or find jobs in the job database. Additionally, this
module contains functions to create/handle the machine instructions for the Teknic motors.

'''

from PyQt5.QtCore import QThread, pyqtSignal
from sqlalchemy.orm.exc import NoResultFound
import json

from .Database import Job, JobDatabase, configure_database


# Create New Job
def create_job(part_number, company_name, spring_constant, spring_length, spring_type, spring_wind_direction,
               arbor_size, wire_diameter, feed_distance, start_dead_turns, live_turns, live_turn_spacing,
               end_dead_turns):
    """ Creates a new job entry in the jobs database

    Args: 
        part_number (str): Part number of spring job
        company_name (str): Company name of spring job
        spring_constant (str): Spring constant of spring job
        spring_length (str): Spring length (in) of spring job
        spring_type (str): Spring Type (Compression or extension) of spring job
        spring_wind_direction (str): Direction of winding (Left or Right) of spring job
        arbor_size (str): Arbor Size of spring job
        wire_diameter (str): Wire diameter size (in) of spring job
        feed_distance (str): Feed disance (in) of spring job
        start_dead_turns (str): Number of starting dead turns (count) of spring job
        live_turns (str): Number of live turns (count) of spring job
        live_turn_spacing (str): Live turn spacing (in) of spring job
        end_dead_turns (str): Number of ending dead turns (count) of spring job
    """

    # Create job entry into job table
    new_job = Job(part_number, company_name, spring_constant, spring_length, spring_type, spring_wind_direction,
                  arbor_size, wire_diameter, feed_distance, start_dead_turns, live_turns, live_turn_spacing,
                  end_dead_turns)

    JobDatabase.session.add(new_job)
    try:
        JobDatabase.session.commit()
    except Exception as e:
        print(e)
    else:
        return new_job


def get_all_jobs():
    """ Gets all jobs (in job table) in job database """
    return JobDatabase.session.query(Job).all()


def find_job(**kwargs):
    """ Finds job in job table that fits the keyword arguments given """
    if len(kwargs) < 1:
        print("No search filters given, add filter")
        return None
    else:
        part_number = str(kwargs.get('part_number', None))
        company_name = str(kwargs.get('company_name', None))

    if (part_number is not None) and (company_name is not None):
        try:
            result = JobDatabase.session.query(Job).filter_by(part_number=part_number, company_name=company_name).one()
            print(result)
        except NoResultFound:
            print("No Job Found")
            return None
        except Exception as e:
            print(e)
        else:
            return result  # type: Job


def delete_job(job):
    """ Deletes a specific job entry in the jobs database table """
    try:
        JobDatabase.session.delete(job)
    except Exception as e:
        print(e)
        return False
    else:
        JobDatabase.session.commit()
        return True

def create_spring_instructions(start_dead_turns, end_dead_turns, live_turns, live_turns_spacing, wire_diameter):
    """ Creates the spring instructions for a spring job

    Args: 
        start_dead_turns (str): Number of start dead turns in the spring job
        end_dead_turns (str): Number of ending dead turns in the spring job
        live_turns (str): Number of live turns in the spring job
        live_turns_spacing (str): Spacing between live turns in spring job
        wire_diameter (str): Wire diameter used in spring job
    """
    # Instruction List (to be converted to json)
    instruction_set = []

    # Initial distance required starts at 0
    total_distance = 0

    # Move Count starts at 0
    move_count = 0

    # single instruction place-holder
    instruction = {}

    # Add start dead turn moves
    for i in range(int(start_dead_turns)):
        instruction["Command"] = "Move Z"
        instruction["Position"] = convert_in_to_counts(float(wire_diameter))
        instruction_set.append(instruction)

    return instruction_set

def convert_in_to_counts(distance):
    """ Function to convert inches into an encoder count for moves """
    # 6400 counts per revolution
    # 1 rev = .1 in of z-axis travel
    count_total = (6400 * distance) / (.1)

    # round count total to nearest whole number
    return int(round(count_total))


# https://kushaldas.in/posts/pyqt5-thread-example.html
class MotorThread(QThread):
    """ Class that handles the sending of motor move instructions """
    signal = pyqtSignal(str)

    def __init__(self):
        """ init function of Motor Thread """
        QThread.__init__(self)

        self.instruction_set = []
        self.motor_client = None

    # run method gets called when we start the thread
    def run(self):
        """ Run method of the thread class that sends all instructions to 
        the motor server 
        """
        # Run through all instructions
        for instruction in self.instruction_set:
            print(instruction)

            # Create payload for message
            payload = {}
            payload["Command"] = instruction["Command"]
            payload["Position"] = instruction["Position"]
            
            # Create message to send over socket
            message = {}
            message['Payload'] = payload

            # Send json message over socket
            self.motor_client.send_json(message)

            # Wait for Success
            msg = self.motor_client.recv()

        # Emit done signal
        self.signal.emit('Done')


# https://kushaldas.in/posts/pyqt5-thread-example.html
class MotorStatusThread(QThread):
    """ Class that handles the motor status pub """
    signal = pyqtSignal(str)
    new_pos = pyqtSignal(str)
    new_rpm = pyqtSignal(str)

    def __init__(self):
        """ init function of Motor Thread """
        QThread.__init__(self)

        self.motor_subscription = None

    # run method gets called when we start the thread
    def run(self):
        """ Run method of the thread class that sends all instructions to 
        the motor server 
        """
        while True:
            # Wait for message
            msg = self.motor_subscription.recv()
            item = json.loads(msg.decode("utf-8"))
            rpm = float(item["Z RPM"])
            rpm = f"{rpm:.0f}"
            pos = float(item["Z Position"])
            pos = f"{pos:.0f}"
            self.new_rpm.emit(rpm)
            self.new_pos.emit(pos)

        # Emit done signal
        self.signal.emit('Done')


if __name__ == '__main__':
    # Create and configure database
    configure_database()

    # Add sample job
    create_job('1234', 'GlennCo', '1.1', '1.2', 'Compression', 'Left', '1.3', '1.4', '1.5', '1', '2', '1.7', '3')

    jobs = get_all_jobs()

    print(jobs)

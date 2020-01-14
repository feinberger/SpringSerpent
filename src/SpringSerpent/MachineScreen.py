'''MachineScreen.py: This is the python module for functions relating to the MachineScreen page

This python module is used to interface and supply functionality to the MachineScreen page on the main
application. This screen is used to interact with the motor server (via zmq) which controls the Teknic 
motors (seperate process). This also provides functionality to home motors, view feedback of the motors,
and control varying motor settings.

'''

import datetime

from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtWidgets import QWidget

import zmq

from .AWS import AWSHandler
from .Spring import MotorThread, create_spring_instructions, find_job, MotorStatusThread
from .ui.MachineScreen import Ui_MachineScreen


class MachineScreen(QWidget):
    """ This is the python code for the MachineScreen UI functionality """

    # Change Screen Signal
    change_screen = pyqtSignal(str, str)

    def __init__(self):
        ''' init function to prepare and connect UI functionality '''
        # Create MachineScreen from UI->PY file
        super(MachineScreen, self).__init__()

        # Setup screen ui
        self.screen_ui = Ui_MachineScreen()
        self.screen_ui.setupUi(self)

        # Allow for widget background to show
        self.setAttribute(Qt.WA_StyledBackground, True)

        # Spring Object
        self.spring = None

        # Screen Parameters
        self.previous_screen = None
        self.job_loaded_flag = False

        # Motor Thread
        self.motor_thread = MotorThread()
        self.motor_status_thread = MotorStatusThread()

        # Motor parameters
        self.motor_status = "Ready"
        self.motor_start_position = 0
        self.motor_current_position = 0
        self.move_total = 0
        self.feed_rate = 50

        # Client Command Variables
        self.context = None
        self.client = None
        self.subscriber = None

        # AWS Handler
        self.aws_handler = AWSHandler()

        # Connect buttons
        self.screen_ui.home_button.pressed.connect(self.load_home_screen)
        self.screen_ui.home_button_2.pressed.connect(self.load_home_screen)
        self.screen_ui.back_button.pressed.connect(self.load_previous_screen)
        self.screen_ui.home_zaxis_button.pressed.connect(self.home_zaxis_motor_request)
        self.screen_ui.start_job_button.pressed.connect(self.start_job)
        self.screen_ui.stop_job_button.pressed.connect(self.stop_job)

        # Connect feed rate slider
        self.screen_ui.feed_rate_slider.valueChanged.connect(self.update_feed_rate)

        # Connect thread signal
        self.motor_thread.signal.connect(self.instructions_finished)
        self.motor_status_thread.new_pos.connect(self.update_z_position)
        self.motor_status_thread.new_rpm.connect(self.update_z_speed)
        self.motor_status_thread.new_status.connect(self.update_z_status)

        # Connect to teknic process
        self.initialize_client()

        # Initialize AWS Handler
        self.aws_handler.load_configuration()
        self.aws_handler.initialize_mqtt_client()

        # Set feed rate percentage
        self.screen_ui.feed_rate_slider.setValue(self.feed_rate)

        # Initialize jog controller to none
        self.screen_ui.none_jog.setChecked(True)

    def load_home_screen(self):
        """ Emits the home screen signal """
        self.change_screen.emit("HomeScreen", "MachineScreen")

    def prepare_screen(self, job_load=False, part_number=None, company_name=None):
        """Prepares the machine screen for use

        Args:
            job_load (str): job loading variable
            part_number (str): part number of loaded job
            company_name (str): company name of loaded job
        """
        # Determine screen settings dependent on if job file has been loaded
        if job_load:
            self.screen_ui.Header.setCurrentIndex(1)

            # Set header to home and back button header
            self.screen_ui.Header.setCurrentIndex(1)

            # Set job button to start/stop job buttons
            self.screen_ui.job_button_frame.setCurrentIndex(1)

            # Determine back screen
            if job_load == 'New':
                self.previous_screen = "NewJobScreen"
                self.set_sys_status_label("Job Ready")
                self.spring = find_job(part_number=part_number, company_name=company_name)
                self.job_loaded_flag = True
            elif job_load == 'Existing':
                self.previous_screen = "JobLibraryScreen"
                self.spring = find_job(part_number=part_number, company_name=company_name)
                self.set_sys_status_label("Job Ready")
                self.job_loaded_flag = True

        else:
            # Set header to home button only header
            self.screen_ui.Header.setCurrentIndex(0)

            # Set job button to device load
            self.screen_ui.job_button_frame.setCurrentIndex(0)

            # Set back screen to home button
            self.previous_screen = "HomeScreen"

            # Set system status to load job
            self.set_sys_status_label("Load Job")

            self.job_loaded_flag = False

    def load_previous_screen(self):
        """ Loads the previously loaded screen """
        if self.previous_screen == "NewJobScreen":
            self.change_screen.emit("NewJobScreen", "MachineScreen")
        elif self.previous_screen == "JobLibraryScreen":
            self.change_screen.emit("JobLibraryScreen", "MachineScreen")

    def set_sys_status_label(self, status, percentage=0):
        """Prepares the machine screen for use

        Args:
            status (str): system status to set 
        """
        if status == "Job Ready":
            self.screen_ui.sys_state.setStyleSheet("""
            border: 2px solid rgb(255, 251, 244);
            background-color: rgb(0, 170, 127);""")
            self.screen_ui.sys_state.setText(status)
        elif status == "Load Job":
            self.screen_ui.sys_state.setStyleSheet("""
            border: 2px solid rgb(255, 251, 244);
            background-color: rgb(93, 173, 226);""")
            self.screen_ui.sys_state.setText(status)
        elif status == "Running":
            self.screen_ui.sys_state.setStyleSheet("""
            border: 2px solid rgb(255, 251, 244);
            background-color: rgb(0, 170, 127);""")
            self.screen_ui.sys_state.setText(f"{status} {percentage}%")
        elif status == "Homing":
            self.screen_ui.sys_state.setStyleSheet("""
            border: 2px solid rgb(255, 251, 244);
            background-color: rgb(174, 214, 241);""")
            self.screen_ui.sys_state.setText(status)
        elif status == "Stopped":
            self.screen_ui.sys_state.setStyleSheet("""
            border: 2px solid rgb(255, 251, 244);
            background-color: rgb(231, 76, 60);""")
            self.screen_ui.sys_state.setText(status)

    def initialize_client(self, client_port='5555', subscriber_port='5556'):
        """Prepares the zmq req client for use.

        Args:
            port (str): the client port of the local host to connect to
        """
        # Create context and client
        self.context = zmq.Context()
        self.client = self.context.socket(zmq.REQ)
        self.client.connect(f'tcp://localhost:{client_port}')

        # Create subscriber for motor status
        self.subscriber = self.context.socket(zmq.SUB)
        self.subscriber.connect('tcp://localhost:5556')
        self.subscriber.setsockopt(zmq.SUBSCRIBE, b'')

        # Send Connect Request
        self.client.send(b'Connect')

        # Wait for Success
        msg = self.client.recv()

        # TODO: Add error handling to motor server connection
        if msg != b'Success':
            print("Failed to connect to motor server")
        else:
            self.motor_status_thread.motor_subscription = self.subscriber
            self.motor_status_thread.start()


    def home_zaxis_motor_request(self):
        """ Sends a request to the motor server to home z-axis"""
        # Create payload for message
        payload = {}
        payload["Command"] = "Home Z"
        
        # Create message to send over socket
        message = {}
        message['Payload'] = payload

        # Send json message over socket
        self.client.send_json(message)

        # Wait for Success
        msg = self.client.recv()

    def start_job(self):
        print(f"Start Turns: {self.spring.start_dead_turns}")
        print(f"End Turns: {self.spring.end_dead_turns}")
        print(f"Live Turns: {self.spring.live_turns}")
        print(f"Live Turn Spacing: {self.spring.live_turn_spacing}")
        print(f"Live Turn Spacing: {self.spring.wire_diameter}")
        
        """ Sends the job's instruction set to the motor thread to be processed by the motor server"""
        instruction_set = create_spring_instructions(self.spring.start_dead_turns, 
        self.spring.end_dead_turns, self.spring.live_turns, self.spring.live_turn_spacing, self.spring.wire_diameter)

        # Get total moves
        self.move_total = instruction_set["Move Total"]

        # Configure motor thread
        self.motor_thread.instruction_set = instruction_set["Instructions"] 
        self.motor_thread.motor_client = self.client
        self.motor_thread.start()
        
        self.motor_status = "Running"
        self.set_sys_status_label("Running", "0%")

    def stop_job(self):
        """ Sends a request to the motor server to stop z-axis"""
        # Create payload for message
        payload = {}
        payload["Command"] = "Stop"
        
        # Create message to send over socket
        message = {}
        message['Payload'] = payload

        # Send json message over socket
        self.client.send_json(message)

        # Wait for Success
        msg = self.client.recv()
        
        # Reset motor status
        self.motor_status = "Stopped"
        self.set_sys_status_label("Stopped")
        self.motor_start_position = self.motor_current_position


    def instructions_finished(self):
        """ Responds to job finished signal and sends out AWS completion email"""
        print("Job Complete!")

        msg_payload = {}
        msg_payload['Command'] = 'Job Status'
        msg_payload['Part Number'] = self.spring.part_number
        msg_payload['Company Name'] = self.spring.company_name
        msg_payload['Timestamp'] = datetime.datetime.now().strftime("%m/%d/%Y %H:%M:%S")

        # self.aws_handler.send_message('job', msg_payload)

    def update_z_position(self, value):
        """ Updates z position label and running status"""
        self.motor_current_position = value

        # Convert position to inches
        position_in_inches = (float(self.motor_current_position) * 0.1) / 6400.0
        self.screen_ui.zaxis_position.setText(f"{position_in_inches:.02f} in")

        # Update motor positions on initial start
        if self.motor_status == "Ready":
            self.motor_start_position = self.motor_current_position
        elif self.motor_status == "Running":
            # Check percentage done
            percentage_complete = (int(self.motor_current_position) - int(self.motor_start_position)) / (self.move_total)
            percentage_complete = int(round(percentage_complete * 100))
            
            if percentage_complete >= 100:
                self.motor_status = "Ready"
                self.set_sys_status_label("Job Ready")
                self.motor_start_position = self.motor_current_position
                print("Job Complete!")

                msg_payload = {}
                msg_payload['Command'] = 'Job Status'
                msg_payload['Part Number'] = self.spring.part_number
                msg_payload['Company Name'] = self.spring.company_name
                msg_payload['Timestamp'] = datetime.datetime.now().strftime("%m/%d/%Y %H:%M:%S")

                # self.aws_handler.send_message('job', msg_payload)
            else:
                self.set_sys_status_label("Running", str(percentage_complete))
        elif self.motor_status == "Homing":
            # Check if motor was homed
            if int(self.motor_current_position) == 0:
                self.motor_status = "Ready"
                self.motor_start_position = self.motor_current_position
                # Set system status to job ready or load job
                if self.job_loaded_flag:
                    self.set_sys_status_label("Job Ready")
                else:
                    self.set_sys_status_label("Load Job")


    def update_z_speed(self, value):
        """ Updates z speed label"""
        self.screen_ui.zaxis_speed.setText(f"{value} RPM")


    def update_z_status(self, value):
        if value == "Homing":
            self.set_sys_status_label("Homing")
            self.motor_status = "Homing"

    
    def update_feed_rate(self):
        # Get current value from feed rate slider
        self.feed_rate = self.screen_ui.feed_rate_slider.value()

        # Update feed rate percentage label
        self.screen_ui.feed_rate.setText(f"{self.feed_rate}%")

        # Create payload for message
        payload = {}
        payload["Command"] = "Feed Rate Z"
        payload["Position"] = self.feed_rate
        
        # Create message to send over socket
        message = {}
        message['Payload'] = payload

        # Send json message over socket
        self.client.send_json(message)

        # Wait for Success
        msg = self.client.recv()

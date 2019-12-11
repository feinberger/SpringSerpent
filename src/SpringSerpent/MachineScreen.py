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

        # Motor Thread
        self.motor_thread = MotorThread()
        self.motor_status_thread = MotorStatusThread()

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

        # Connect thread signal
        self.motor_thread.signal.connect(self.instructions_finished)
        self.motor_status_thread.new_pos.connect(self.update_z_position)
        self.motor_status_thread.new_rpm.connect(self.update_z_speed)
        # Connect to teknic process
        self.initialize_client()

        # Initialize AWS Handler
        self.aws_handler.load_configuration()
        self.aws_handler.initialize_mqtt_client()

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
            elif job_load == 'Existing':
                self.previous_screen = "JobLibraryScreen"
                self.spring = find_job(part_number=part_number, company_name=company_name)

        else:
            # Set header to home button only header
            self.screen_ui.Header.setCurrentIndex(0)

            # Set job button to device load
            self.screen_ui.job_button_frame.setCurrentIndex(0)

            # Set back screen to home button
            self.previous_screen = "HomeScreen"

            # Set system status to load job
            self.set_sys_status_label("Load Job")

    def load_previous_screen(self):
        """ Loads the previously loaded screen """
        if self.previous_screen == "NewJobScreen":
            self.change_screen.emit("NewJobScreen", "MachineScreen")
        elif self.previous_screen == "JobLibraryScreen":
            self.change_screen.emit("JobLibraryScreen", "MachineScreen")

    def set_sys_status_label(self, status):
        """Prepares the machine screen for use

        Args:
            status (str): system status to set 
        """
        if status == "Job Ready":
            self.screen_ui.sys_state.setStyleSheet("""
            border: 2px solid rgb(255, 251, 244);
            background-color: rgb(0, 170, 127);""")
            self.screen_ui.sys_state.setText(status)
        if status == "Load Job":
            self.screen_ui.sys_state.setStyleSheet("""
            border: 2px solid rgb(255, 251, 244);
            background-color: rgb(93, 173, 226);""")
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
        """ Sends the job's instruction set to the motor thread to be processed by the motor server"""
        instruction_set = create_spring_instructions(self.spring.start_dead_turns, 
        self.spring.end_dead_turns, self.spring.live_turns, self.spring.live_turn_spacing, self.spring.wire_diameter)

        self.motor_thread.instruction_set = instruction_set
        self.motor_thread.motor_client = self.client
        self.motor_thread.start()

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
        """ Updates z position label"""
        self.screen_ui.zaxis_position.setText(value)

    def update_z_speed(self, value):
        """ Updates z speed label"""
        self.screen_ui.zaxis_speed.setText(value)
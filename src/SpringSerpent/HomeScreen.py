'''HomeScreen.py: This is the python module for functions relating to the HomeScreen page

This python module is used to interface and supply functionality to the HomeScreen page on the main
application

'''

from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtWidgets import QWidget

from .ui.HomeScreen import Ui_HomeScreen


class HomeScreen(QWidget):
    """ This is the python code for the HomeScreen UI functionality """

    # Change Screen Signal
    change_screen = pyqtSignal(str, str)

    def __init__(self):
        ''' init function to prepare and connect UI functionality '''
        # Create HomeScreen from UI->PY file
        super(HomeScreen, self).__init__()

        # Setup screen ui
        self.screen_ui = Ui_HomeScreen()
        self.screen_ui.setupUi(self)

        # Allow for widget background to show
        self.setAttribute(Qt.WA_StyledBackground, True)

        # Connect buttons
        self.screen_ui.new_spring_button.released.connect(self.load_new_spring_screen)
        self.screen_ui.machine_button.released.connect(self.load_machine_screen)
        self.screen_ui.job_library_button.released.connect(self.load_job_library_screen)

    def load_new_spring_screen(self):
        """ Function to load new job screen """
        self.change_screen.emit("NewJobScreen", "HomeScreen")

    def load_machine_screen(self):
        """ Function to load machine screen """
        self.change_screen.emit("MachineScreen", "HomeScreen")

    def load_job_library_screen(self):
        """ Function to load job library screen """
        self.change_screen.emit("JobLibraryScreen", "HomeScreen")

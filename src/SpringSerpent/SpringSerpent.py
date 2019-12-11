from PyQt5.QtWidgets import QMainWindow

from .ui.SpringSerpent import Ui_MainWindow


class MainWindow(QMainWindow):
    """ This is the python code for the Main Application """
    
    def __init__(self):
        """ Init function for the Main Application """
        super(MainWindow, self).__init__()

        self.screen_ui = Ui_MainWindow()
        self.screen_ui.setupUi(self)

        # Home Screen
        self.home_screen = self.screen_ui.home_screen
        self.home_screen.change_screen.connect(self.load_screen)

        # New Job Screen
        self.new_job_screen = self.screen_ui.new_job_screen
        self.new_job_screen.change_screen.connect(self.load_screen)

        # Machine Screen
        self.machine_screen = self.screen_ui.machine_screen
        self.machine_screen.change_screen.connect(self.load_screen)

        # Job Library Screen
        self.job_library_screen = self.screen_ui.job_library_screen
        self.job_library_screen.change_screen.connect(self.load_screen)

        # Start screen at home screen
        self.load_screen("HomeScreen", None, None, None)

    def load_screen(self, screen, prev_screen, part_number=None, company_name=None):
        """ Function that loads the required screen on the stack widget """
        if screen == "HomeScreen":
            # Show home screen on stacked widget
            self.screen_ui.screen_stack.setCurrentIndex(0)

        if screen == "NewJobScreen":
            # Prepare machine screen depending on job loading
            if prev_screen == "HomeScreen":
                # Prepare 'fresh' new job screen
                self.new_job_screen.prepare_screen(clear_flag=True)
            elif prev_screen == "MachineScreen":
                # Prepare new job screen without clearing items
                self.new_job_screen.prepare_screen(clear_flag=False)

            # Show new job screen on stacked widget
            self.screen_ui.screen_stack.setCurrentIndex(1)

        if screen == "MachineScreen":
            # Prepare machine screen depending on job loading
            if prev_screen == "HomeScreen":
                # Prepare machine screen with no job loaded
                self.machine_screen.prepare_screen(job_load=False)
            elif prev_screen == "NewJobScreen":
                # Prepare machine screen with job loaded
                self.machine_screen.prepare_screen(job_load='New', part_number=part_number, company_name=company_name)
            elif prev_screen == "JobLibraryScreen":
                # Prepare machine screen with job loaded
                self.machine_screen.prepare_screen(job_load='Existing', part_number=part_number, company_name=company_name)

            # Show new job screen on stacked widget
            self.screen_ui.screen_stack.setCurrentIndex(2)

        if screen == "JobLibraryScreen":
            # Prepare job screen depending on job loading
            if prev_screen == "HomeScreen":
                # Prepare job screen with no job loaded
                self.job_library_screen.prepare_screen()

            # Show job library screen on stacked widget
            self.screen_ui.screen_stack.setCurrentIndex(3)

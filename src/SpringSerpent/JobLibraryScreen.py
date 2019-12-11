'''JobLibraryScreen.py: This is the python module for functions relating to the JobLibraryScreen page

This python module is used to interface and supply functionality to the JobLibraryScreen page on the main
application. This screen is used look at previously created jobs or load a job via barcode and then pass
the loaded job to the machine screen.

'''

from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtWidgets import QHeaderView, QTableWidgetItem, QWidget

from peripherals.barcode import BarcodeScanner

from .Spring import find_job, get_all_jobs, delete_job
from .ui.JobLibraryScreen import Ui_JobLibraryScreen


class JobLibraryScreen(QWidget):
    """ This is the python code for the JobLibraryScreen UI functionality """

    # Change Screen Signal
    change_screen = pyqtSignal(str, str, str, str)

    def __init__(self):
        ''' init function to prepare and connect UI functionality '''
        # Create HomeScreen from UI->PY file
        super(JobLibraryScreen, self).__init__()

        # Setup screen ui
        self.screen_ui = Ui_JobLibraryScreen()
        self.screen_ui.setupUi(self)

        # Allow for widget background to show
        self.setAttribute(Qt.WA_StyledBackground, True)

        # Stretch job directory columns to screen width
        self.screen_ui.job_library_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        # Barcode scanner
        self.barcode_scanner = BarcodeScanner()

        # Connect buttons
        self.screen_ui.home_button.pressed.connect(self.load_home_screen)
        self.screen_ui.proceed_button.pressed.connect(self.load_job)
        self.screen_ui.scan_code_button.pressed.connect(self.scan_barcode)
        self.screen_ui.delete_button.pressed.connect(self.delete_job)

        # Connect selection
        self.screen_ui.job_library_table.itemSelectionChanged.connect(self.show_hidden_buttons)

        # Connect barcode slot
        self.screen_ui.barcode_edit.returnPressed.connect(self.process_barcode)

        # Update job library table
        self.update_jobs()

    def prepare_screen(self):
        """ Prepares screen for use """
        # Update job library table
        self.update_jobs()

        # Clear selection
        self.screen_ui.job_library_table.clearSelection()

        # Hide proceed button
        self.hide_hidden_buttons()

    def load_home_screen(self):
        """ Emits the home screen signal """
        self.change_screen.emit("HomeScreen", "JobLibraryScreen", None, None)

    def update_jobs(self):
        """ Updates and readies job listings in job table for display """
        # Get all jobs from database
        job_list = get_all_jobs()

        # Determine number of rows
        self.screen_ui.job_library_table.setRowCount(len(job_list))

        # Set job directory table
        for row, job in enumerate(job_list):
            # Extract job information into list for ease of update
            job_info = [f"{job.part_number}",
                        f"{job.company_name}",
                        f"{job.spring_constant}",
                        f"{job.spring_length}",
                        f"{job.spring_type}"]

            # Update row with info and center text
            for column, item in enumerate(job_info):
                table_item = QTableWidgetItem(item)
                table_item.setTextAlignment(Qt.AlignCenter)
                self.screen_ui.job_library_table.setItem(row, column, table_item)

        # Update job library table size
        self.screen_ui.job_library_table.size()

    def show_hidden_buttons(self):
        ''' function to un-hide proceed and delete button'''
        self.screen_ui.proceed_stack.setCurrentIndex(0)
        self.screen_ui.delete_stack.setCurrentIndex(1)

    def hide_hidden_buttons(self):
        ''' function to hide proceed and delete button'''
        self.screen_ui.proceed_stack.setCurrentIndex(1)
        self.screen_ui.delete_stack.setCurrentIndex(0)

    def load_job(self):
        ''' function to load selected job from on screen table widget'''
        # Selected index is the first item in the list of selections from table
        selected_index = self.screen_ui.job_library_table.selectionModel().selectedRows()[0]
        selected_row = selected_index.row()

        # Part number is column 0
        part_number = self.screen_ui.job_library_table.item(selected_row, 0).text()
        
        # Company name is column 1
        company_name = self.screen_ui.job_library_table.item(selected_row, 1).text()

        self.change_screen.emit("MachineScreen", "JobLibraryScreen", part_number, company_name)

    def scan_barcode(self):
        ''' function to handle barcode job loading'''
        self.screen_ui.barcode_edit.setFocus()
    
    def process_barcode(self):
        ''' function to process the selected barcode '''
        # Parse barcode data (partnumber-companyname)
        barcode_text = self.screen_ui.barcode_edit.text()
        barcode_part_number = barcode_text.split('-')[0]
        barcode_company_name = barcode_text.split('-')[1]

        # Get number of rows from table
        table_rows = self.screen_ui.job_library_table.rowCount()

        # Find part number (if possible) in table
        for row in range(0, table_rows):
            part_number = self.screen_ui.job_library_table.item(row, 0).text()

            # If part number is the same, check for company
            if part_number == barcode_part_number:
                company_name = self.screen_ui.job_library_table.item(row, 1).text()

                # if company name is the same, select row
                if company_name == barcode_company_name:
                    self.screen_ui.job_library_table.selectRow(row)

    def delete_job(self):
        # Selected index is the first item in the list of selections from table
        selected_index = self.screen_ui.job_library_table.selectionModel().selectedRows()[0]
        selected_row = selected_index.row()

        # Part number is column 0
        part_number = self.screen_ui.job_library_table.item(selected_row, 0).text()
        
        # Company name is column 1
        company_name = self.screen_ui.job_library_table.item(selected_row, 1).text()

        # Load job from database
        job = find_job(part_number=part_number, company_name=company_name)

        # Delete job
        delete_job(job)

        # Refresh table and clear selection
        self.prepare_screen()




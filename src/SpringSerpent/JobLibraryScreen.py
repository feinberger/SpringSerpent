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

        # Connect filter functions
        self.screen_ui.company_name.textChanged.connect(self.filter_table_function)
        self.screen_ui.part_number.textChanged.connect(self.filter_table_function)
        self.screen_ui.compression_spring.stateChanged.connect(self.filter_table_function)
        self.screen_ui.extension_spring.stateChanged.connect(self.filter_table_function)

        # Connect barcode slot
        self.screen_ui.barcode_edit.returnPressed.connect(self.process_barcode)

        # Update job library table
        self.update_jobs()

        # Set Filter Compression and Extension to checked
        self.screen_ui.compression_spring.setChecked(True)
        self.screen_ui.extension_spring.setChecked(True)

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
        # Clear text
        self.screen_ui.barcode_edit.clear()

        # Set focus to allow for text input
        self.screen_ui.barcode_edit.setFocus()
    
    def process_barcode(self):
        ''' function to process the selected barcode '''
        # Parse barcode data (partnumber-companyname)
        barcode_text = self.screen_ui.barcode_edit.text()

        # Match flag
        match = False

        try:
            barcode_part_number = barcode_text.split('-')[0]
            barcode_company_name = barcode_text.split('-')[1]
        except:
            pass
        else:
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
                        match = True
        
        if match:
            self.screen_ui.barcode_edit.clear()
        else:
            self.screen_ui.barcode_edit.setText(f"{barcode_text} Not Found!")

        # Clear focus
        self.screen_ui.barcode_edit.clearFocus()
        

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

    def filter_table_function(self):
        # Get filter attributes
        part_number = self.screen_ui.part_number.text()
        company_name = self.screen_ui.company_name.text()
        extension_flag = self.screen_ui.extension_spring.isChecked()
        compression_flag = self.screen_ui.compression_spring.isChecked()

        if part_number != "" or company_name != "":
            for i in range(self.screen_ui.job_library_table.rowCount()):
                if part_number != "":
                    if self.check_matching_part_number(i, part_number):
                        if company_name != "":
                            if self.check_matching_company_name(i, company_name):
                                match = True
                            else:
                                match = False
                        else:
                            match = True
                    else:
                        match = False
                else:
                    if company_name != "":
                        if self.check_matching_company_name(i, company_name):
                            match = True
                        else:
                            match = False
        
                if not compression_flag:
                    if self.check_compression_spring(i):
                        match = False
                if not extension_flag:
                    if self.check_extension_spring(i):
                        match = False

                self.screen_ui.job_library_table.setRowHidden(i, not match)
        else:
            match = True
            for i in range(self.screen_ui.job_library_table.rowCount()):
                if not compression_flag:
                    if self.check_compression_spring(i):
                        match = False
                if not extension_flag:
                    if self.check_extension_spring(i):
                        match = False
                self.screen_ui.job_library_table.setRowHidden(i, not match)


    def check_matching_part_number(self, row, part_number):
        if part_number.lower() in self.screen_ui.job_library_table.item(row, 0).text().lower():
            return True
        else:
            return False

    def check_matching_company_name(self, row, company_name):
        if company_name.lower() in self.screen_ui.job_library_table.item(row, 1).text().lower():
            return True
        else:
            return False

    def check_compression_spring(self, row):
        if self.screen_ui.job_library_table.item(row, 4).text().lower() == "compression":
            return True
        else:
            return False

    def check_extension_spring(self, row):
        if self.screen_ui.job_library_table.item(row, 4).text().lower() == "extension":
            return True
        else:
            return False





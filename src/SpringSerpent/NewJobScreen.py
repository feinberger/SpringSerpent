'''NewJobScreen.py: This is the python module for functions relating to the NewJobScreen page

This python module is used to interface and supply functionality to the JobLibraryScreen page on the main
application. This screen is used to create a new spring job which will then be stored into the database and
then load the machine screen once the job has been created.

'''

import subprocess

from PyQt5.QtCore import QEvent, QObject, Qt, pyqtSignal
from PyQt5.QtWidgets import QWidget

from .Spring import create_job, find_job
from .ui.NewJobScreen import Ui_NewJobScreen


class NewJobScreen(QWidget):
    """ This is the python code for the NewJobScreen UI functionality """

    # Change Screen Signal
    change_screen = pyqtSignal(str, str, str, str)

    def __init__(self):
        ''' init function to prepare and connect UI functionality '''
        # Create HomeScreen from UI->PY file
        super(NewJobScreen, self).__init__()

        # Setup screen ui
        self.screen_ui = Ui_NewJobScreen()
        self.screen_ui.setupUi(self)

        # Allow for widget background to show
        self.setAttribute(Qt.WA_StyledBackground, True)

        # Screen Parameters
        self.spring_parameters = {}

        # Disable spring constant from typing
        self.screen_ui.spring_constant.setDisabled(True)
        self.screen_ui.spring_length.setDisabled(True)

        # Screen Parameters
        self.winding_options = ['Left', 'Right']
        self.spring_types = ['Compression', 'Extension']

        # Spring Parameters
        self.wire_diameter = 0.0
        self.feed_distance = 0.0
        self.feed_distance_change_rate = .1
        self.feed_distance_max = 3
        self.start_dead_turns = 0
        self.turn_change_rate = 1
        self.start_dead_turns_max = 9999
        self.live_turns = 0
        self.live_turns_max = 9999
        self.live_turn_spacing = 0.0
        self.live_turn_spacing_change_rate = .1
        self.live_turn_spacing_max = 999.9
        self.end_dead_turns = 0
        self.end_dead_turns_max = 9999

        # Connect buttons
        self.screen_ui.back_button.pressed.connect(self.load_home_screen)
        self.screen_ui.proceed_button.pressed.connect(self.confirm_parameters)
        self.screen_ui.feed_distance_inc_button.pressed.connect(
            self.increase_feed_distance)
        self.screen_ui.feed_distance_dec_button.pressed.connect(
            self.decrease_feed_distance)
        self.screen_ui.start_dead_turns_inc_button.pressed.connect(
            self.increase_start_turns)
        self.screen_ui.start_dead_turns_dec_button.pressed.connect(
            self.decrease_start_turns)
        self.screen_ui.end_dead_turns_inc_button.pressed.connect(
            self.increase_end_turns)
        self.screen_ui.end_dead_turns_dec_button.pressed.connect(
            self.decrease_end_turns)
        self.screen_ui.live_turn_inc_button.pressed.connect(
            self.increase_live_turns)
        self.screen_ui.live_turn_dec_button.pressed.connect(
            self.decrease_live_turns)
        self.screen_ui.live_turn_spacing_inc_button.pressed.connect(
            self.increase_live_turn_spacing)
        self.screen_ui.live_turn_spacing_dec_button.pressed.connect(
            self.decrease_live_turn_spacing)

        # Connect wire diameter change
        self.screen_ui.wire_diameter.textChanged.connect(self.update_wire_diameter)

        # Connect line edits to event filter
        # self.screen_ui.part_number.installEventFilter(self)

    def load_home_screen(self):
        """ Emits the home screen signal """
        self.change_screen.emit("HomeScreen", "NewJobScreen", None, None)

    def prepare_screen(self, clear_flag):
        """ Prepares the new job screen for use.

        Args: 
            clear_flag (bool): whether to clean the gui elements
        """
        if clear_flag:
            # Set all Parameters to 0
            self.spring_length = 0.0
            self.wire_diameter = 0.0
            self.feed_distance = 0.0
            self.start_dead_turns = 0
            self.end_dead_turns = 0
            self.live_turns = 0
            self.live_turn_spacing = 0.0

            # Clear part number field
            self.screen_ui.part_number.clear()
            self.screen_ui.company_name.clear()

            # Clear spring info
            self.screen_ui.spring_constant.clear()
            self.screen_ui.spring_length.clear()
            self.screen_ui.wire_diameter.clear()
            self.screen_ui.arbor_size.clear()

        # Update spring parameter labels
        self.screen_ui.feed_distance.setText(f"{self.feed_distance:.1f}")
        self.screen_ui.start_dead_turns.setText(str(self.start_dead_turns))
        self.screen_ui.live_turns.setText(str(self.live_turns))
        self.screen_ui.live_turn_spacing.setText(
            f"{self.live_turn_spacing:.1f}")
        self.screen_ui.end_dead_turns.setText(str(self.end_dead_turns))

        # Update spring length
        self.calculate_spring_length()

    def increase_feed_distance(self):
        """ Updates the feed distance the GUI label """
        # Increase feed distance unless already at max
        if self.feed_distance < self.feed_distance_max:
            self.feed_distance += self.feed_distance_change_rate
            round(self.feed_distance, 1)

        # Update Feed Distance Label
        self.screen_ui.feed_distance.setText(f"{self.feed_distance:.1f}")

        # Update spring length
        self.calculate_spring_length()

    def decrease_feed_distance(self):
        """ Decreases the feed distance the GUI label """
        # Decrease feed distance unless already at 0
        if self.feed_distance >= 0.1:
            self.feed_distance -= self.feed_distance_change_rate
            round(self.feed_distance, 1)
        else:
            self.feed_distance = 0.0

        # Update Feed Distance Label
        self.screen_ui.feed_distance.setText(f"{self.feed_distance:.1f}")

        # Update spring length
        self.calculate_spring_length()

    def increase_start_turns(self):
        """ Increases the start turn count and updates the GUI label """
        # Increase start dead turns unless already at max
        if self.start_dead_turns < self.start_dead_turns_max:
            self.start_dead_turns += self.turn_change_rate

        # Update Start Dead Turn Label
        self.screen_ui.start_dead_turns.setText(str(self.start_dead_turns))

        # Update spring length
        self.calculate_spring_length()

    def decrease_start_turns(self):
        """ Decreases the start turn count and updates the GUI label """
        # Decrease start dead turn count unless already at 0
        if self.start_dead_turns > 0:
            self.start_dead_turns -= self.turn_change_rate

        # Update Start Dead Turn Label
        self.screen_ui.start_dead_turns.setText(str(self.start_dead_turns))

        # Update spring length
        self.calculate_spring_length()

    def increase_end_turns(self):
        """ Increases the end turn count and updates the GUI label """
        # Increase end dead turns unless already at max
        if self.end_dead_turns < self.end_dead_turns_max:
            self.end_dead_turns += self.turn_change_rate

        # Update End Dead Turn Label
        self.screen_ui.end_dead_turns.setText(str(self.end_dead_turns))

        # Update spring length
        self.calculate_spring_length()

    def decrease_end_turns(self):
        """ Decreases the end turn count and updates the GUI label """
        # Decrease end dead turn count unless already at 0
        if self.end_dead_turns > 0:
            self.end_dead_turns -= self.turn_change_rate

        # Update End Dead Turn Label
        self.screen_ui.end_dead_turns.setText(str(self.end_dead_turns))

        # Update spring length
        self.calculate_spring_length()

    def increase_live_turns(self):
        """ Increases the live count and updates the GUI label """
        # Increase live turns unless already at max
        if self.live_turns < self.live_turns_max:
            self.live_turns += self.turn_change_rate

        # Update live Turn Label
        self.screen_ui.live_turns.setText(str(self.live_turns))

        # Update spring length
        self.calculate_spring_length()

    def decrease_live_turns(self):
        """ Decreases the live count and updates the GUI label """
        # Decrease live turn count unless already at 0
        if self.live_turns > 0:
            self.live_turns -= self.turn_change_rate

        # Update live Turn Label
        self.screen_ui.live_turns.setText(str(self.live_turns))

        # Update spring length
        self.calculate_spring_length()

    def increase_live_turn_spacing(self):
        """ Increases the live turn spacing and updates the GUI label """
        # Increase live turn spacing unless already at max
        if self.live_turn_spacing < self.live_turn_spacing_max:
            self.live_turn_spacing += self.live_turn_spacing_change_rate
            round(self.live_turn_spacing, 1)

        # Update Live Turn Spacing Label
        self.screen_ui.live_turn_spacing.setText(
            f"{self.live_turn_spacing:.1f}")

        # Update spring length
        self.calculate_spring_length()

    def decrease_live_turn_spacing(self):
        """ Decreases the live turn spacing and updates the GUI label """
        # Decrease live turn spacing unless already at 0
        if self.live_turn_spacing >= 0.1:
            self.live_turn_spacing -= self.live_turn_spacing_change_rate
            round(self.live_turn_spacing, 1)
        else:
            self.live_turn_spacing = 0.0

        # Update Live Turn Spacing Label
        self.screen_ui.live_turn_spacing.setText(
            f"{self.live_turn_spacing:.1f}")

        # Update spring length
        self.calculate_spring_length()

    def confirm_parameters(self):
        """ Confirms the input parameters for new spring and loads machine screen """
        # Get all parameters
        part_number = self.screen_ui.part_number.text().strip()
        company_name = self.screen_ui.company_name.text().strip()
        spring_constant = '1'
        spring_length = self.screen_ui.spring_length.text().strip()
        spring_type = self.screen_ui.spring_type.currentText().strip()
        spring_wind_direction = self.screen_ui.spring_direction.currentText().strip()
        arbor_size = self.screen_ui.arbor_size.text().strip()
        wire_diameter = self.screen_ui.wire_diameter.text().strip()
        feed_distance = self.screen_ui.feed_distance.text()
        start_dead_turns = self.screen_ui.start_dead_turns.text()
        live_turns = self.screen_ui.live_turns.text()
        live_turn_spacing = self.screen_ui.live_turn_spacing.text()
        end_dead_turns = self.screen_ui.end_dead_turns.text()

        # Check if job already exists in database
        job = find_job(part_number=part_number, company_name=company_name)

        # TODO: Add warning box if job exists

        # If no part is found, create it
        if job is None:
            job = create_job(part_number, company_name, spring_constant, spring_length, spring_type,
                             spring_wind_direction, arbor_size, wire_diameter, feed_distance, start_dead_turns,
                             live_turns, live_turn_spacing, end_dead_turns)

        parameters_valid = True

        # TODO: determine what valid parameters are
        if parameters_valid:
            self.change_screen.emit(
                "MachineScreen", "NewJobScreen", job.part_number, job.company_name)

    def update_wire_diameter(self):
        try:
            self.wire_diameter = float(self.screen_ui.wire_diameter.text().strip())
        except:
            self.wire_diameter = 0.0

        # Update spring length
        self.calculate_spring_length()

    def calculate_spring_length(self):
        self.spring_length = self.wire_diameter * (self.start_dead_turns + self.end_dead_turns + self.live_turns) + \
            self.feed_distance + (self.live_turns * self.live_turn_spacing)
        self.screen_ui.spring_length.setText(str(f"{self.spring_length:.02f}"))

    # def eventFilter(self, obj, event):
    #     if event.type() == QEvent.FocusIn:
    #         subprocess.call('/home/gfeinberg/Documents/Projects/Spring-Serpent/tools/keyboard.sh')
    #     if event.type() == QEvent.FocusOut:
    #         subprocess.call('/home/gfeinberg/Documents/Projects/Spring-Serpent/tools/kill_keyboard.sh')

    #     return super(NewJobScreen, self).eventFilter(obj, event)

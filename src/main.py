import sys
import os
import platform
import subprocess
import multiprocessing

os.environ["QT_IM_MODULE"] = "qtvirtualkeyboard"

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication

from SpringSerpent import SpringSerpent
from SpringSerpent.Database import configure_database

def run_main_controller():
    app = QApplication([])

    # Configure job library database
    configure_database()

    # Determine if debug or platform
    if platform.platform() == 'Linux-4.19.75-v7l+-armv7l-with-debian-10.2':
        main_window = SpringSerpent.MainWindow()
        app.setOverrideCursor(Qt.BlankCursor)
        main_window.showFullScreen()
    else:
        main_window = SpringSerpent.MainWindow()
        main_window.show()
    sys.exit(app.exec_())

def run_motor_controller():
    subprocess.call(["./Teknic/build/teknic.out"])


if __name__ == '__main__':
    print("Starting Spring-Serpent")

    # Start main controller process
    main_controller_process = multiprocessing.Process(target=run_main_controller, args=())

    # Start motor controller process
    motor_controller_process = multiprocessing.Process(target=run_motor_controller, args=())
    motor_controller_process.start()

    main_controller_process.start()

    main_controller_process.join()
    motor_controller_process.join()
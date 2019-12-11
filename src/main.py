import sys
import os

os.environ["QT_IM_MODULE"] = "qtvirtualkeyboard"

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication

from SpringSerpent import SpringSerpent
from SpringSerpent.Database import configure_database

if __name__ == '__main__':
    print("Starting Spring-Serpent")

    # Configure job library database
    configure_database()

    app = QApplication([])
    # app.setOverrideCursor(Qt.BlankCursor)
    main_window = SpringSerpent.MainWindow()
    main_window.show()
    sys.exit(app.exec_())
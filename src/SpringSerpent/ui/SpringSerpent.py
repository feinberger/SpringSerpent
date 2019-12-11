# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\Projects\Spring Serpent\Spring-Serpent\designer\SpringSerpent.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1360, 768)
        self.central_widget = QtWidgets.QWidget(MainWindow)
        self.central_widget.setStyleSheet("")
        self.central_widget.setObjectName("central_widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.central_widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.screen_stack = QtWidgets.QStackedWidget(self.central_widget)
        self.screen_stack.setStyleSheet("")
        self.screen_stack.setObjectName("screen_stack")
        self.home_screen = HomeScreen()
        self.home_screen.setObjectName("home_screen")
        self.screen_stack.addWidget(self.home_screen)
        self.new_job_screen = NewJobScreen()
        self.new_job_screen.setObjectName("new_job_screen")
        self.screen_stack.addWidget(self.new_job_screen)
        self.machine_screen = MachineScreen()
        self.machine_screen.setObjectName("machine_screen")
        self.screen_stack.addWidget(self.machine_screen)
        self.job_library_screen = JobLibraryScreen()
        self.job_library_screen.setObjectName("job_library_screen")
        self.screen_stack.addWidget(self.job_library_screen)
        self.horizontalLayout.addWidget(self.screen_stack)
        MainWindow.setCentralWidget(self.central_widget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
from SpringSerpent.HomeScreen import HomeScreen
from SpringSerpent.JobLibraryScreen import JobLibraryScreen
from SpringSerpent.MachineScreen import MachineScreen
from SpringSerpent.NewJobScreen import NewJobScreen


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

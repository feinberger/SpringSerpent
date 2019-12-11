# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\Projects\Spring Serpent\Spring-Serpent\designer\HomeScreen.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_HomeScreen(object):
    def setupUi(self, HomeScreen):
        HomeScreen.setObjectName("HomeScreen")
        HomeScreen.resize(1360, 768)
        HomeScreen.setStyleSheet("QWidget {\n"
"    background-color: rgb(71, 79, 84);\n"
"}\n"
"\n"
"QPushButton {\n"
"    border-radius: 20px;\n"
" }")
        self.gridLayout_2 = QtWidgets.QGridLayout(HomeScreen)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.warnings_button = QtWidgets.QPushButton(HomeScreen)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.warnings_button.sizePolicy().hasHeightForWidth())
        self.warnings_button.setSizePolicy(sizePolicy)
        self.warnings_button.setMinimumSize(QtCore.QSize(350, 200))
        self.warnings_button.setFocusPolicy(QtCore.Qt.NoFocus)
        self.warnings_button.setStyleSheet("QPushButton {\n"
"    image: url(:/buttons/buttons/warning.png);\n"
"    background-color: rgba(236, 112, 99,1);\n"
" }\n"
"QPushButton:pressed {\n"
"    background-color: rgba(236, 112, 99, .7);\n"
"}")
        self.warnings_button.setText("")
        self.warnings_button.setObjectName("warnings_button")
        self.gridLayout_2.addWidget(self.warnings_button, 0, 3, 1, 1)
        self.settings_button = QtWidgets.QPushButton(HomeScreen)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.settings_button.sizePolicy().hasHeightForWidth())
        self.settings_button.setSizePolicy(sizePolicy)
        self.settings_button.setMinimumSize(QtCore.QSize(350, 200))
        self.settings_button.setFocusPolicy(QtCore.Qt.NoFocus)
        self.settings_button.setStyleSheet("QPushButton {\n"
"    image: url(:/buttons/buttons/settings.png);\n"
"    background-color: rgba(82, 190, 128, 1);\n"
" }\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgba(82, 190, 128, .7);\n"
" }")
        self.settings_button.setText("")
        self.settings_button.setObjectName("settings_button")
        self.gridLayout_2.addWidget(self.settings_button, 1, 2, 1, 1)
        self.new_spring_button = QtWidgets.QPushButton(HomeScreen)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.new_spring_button.sizePolicy().hasHeightForWidth())
        self.new_spring_button.setSizePolicy(sizePolicy)
        self.new_spring_button.setMinimumSize(QtCore.QSize(350, 200))
        self.new_spring_button.setFocusPolicy(QtCore.Qt.NoFocus)
        self.new_spring_button.setStyleSheet("QPushButton {\n"
"    image: url(:/buttons/buttons/new_job.png);\n"
"    background-color: rgba(93, 173, 226, 1);\n"
" }\n"
"QPushButton:pressed {\n"
"    background-color: rgba(93, 173, 226, .7);\n"
"}")
        self.new_spring_button.setText("")
        self.new_spring_button.setObjectName("new_spring_button")
        self.gridLayout_2.addWidget(self.new_spring_button, 0, 0, 1, 1)
        self.machine_button = QtWidgets.QPushButton(HomeScreen)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.machine_button.sizePolicy().hasHeightForWidth())
        self.machine_button.setSizePolicy(sizePolicy)
        self.machine_button.setMinimumSize(QtCore.QSize(350, 200))
        self.machine_button.setFocusPolicy(QtCore.Qt.NoFocus)
        self.machine_button.setStyleSheet("QPushButton {    \n"
"    image: url(:/buttons/buttons/machine.png);\n"
"    background-color: rgba(235, 152, 78, 1);\n"
" }\n"
"QPushButton:pressed {\n"
"    background-color: rgba(235, 152, 78, .7);\n"
"}")
        self.machine_button.setText("")
        self.machine_button.setObjectName("machine_button")
        self.gridLayout_2.addWidget(self.machine_button, 0, 2, 1, 1)
        self.job_library_button = QtWidgets.QPushButton(HomeScreen)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.job_library_button.sizePolicy().hasHeightForWidth())
        self.job_library_button.setSizePolicy(sizePolicy)
        self.job_library_button.setMinimumSize(QtCore.QSize(350, 200))
        self.job_library_button.setFocusPolicy(QtCore.Qt.NoFocus)
        self.job_library_button.setStyleSheet("QPushButton {\n"
"    image: url(:/buttons/buttons/job_library.png);\n"
"    background-color: rgba(175, 122, 197,1);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgba(175, 122, 197, .7);\n"
"}")
        self.job_library_button.setText("")
        self.job_library_button.setObjectName("job_library_button")
        self.gridLayout_2.addWidget(self.job_library_button, 1, 0, 1, 1)
        self.about_button = QtWidgets.QPushButton(HomeScreen)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.about_button.sizePolicy().hasHeightForWidth())
        self.about_button.setSizePolicy(sizePolicy)
        self.about_button.setMinimumSize(QtCore.QSize(350, 200))
        self.about_button.setFocusPolicy(QtCore.Qt.NoFocus)
        self.about_button.setStyleSheet("QPushButton {\n"
"    image: url(:/buttons/buttons/information.png);\n"
"    background-color: rgba(170, 183, 184, 1);\n"
" }\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgba(170, 183, 184, .7);\n"
" }")
        self.about_button.setText("")
        self.about_button.setObjectName("about_button")
        self.gridLayout_2.addWidget(self.about_button, 1, 3, 1, 1)

        self.retranslateUi(HomeScreen)
        QtCore.QMetaObject.connectSlotsByName(HomeScreen)

    def retranslateUi(self, HomeScreen):
        _translate = QtCore.QCoreApplication.translate
        HomeScreen.setWindowTitle(_translate("HomeScreen", "Form"))
from . import Spring_Serpent_Resources_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    HomeScreen = QtWidgets.QWidget()
    ui = Ui_HomeScreen()
    ui.setupUi(HomeScreen)
    HomeScreen.show()
    sys.exit(app.exec_())

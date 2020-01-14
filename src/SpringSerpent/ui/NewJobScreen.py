# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\Projects\Spring Serpent\Spring-Serpent\designer\NewJobScreen.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_NewJobScreen(object):
    def setupUi(self, NewJobScreen):
        NewJobScreen.setObjectName("NewJobScreen")
        NewJobScreen.resize(1360, 768)
        self.verticalLayout = QtWidgets.QVBoxLayout(NewJobScreen)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.Header = QtWidgets.QFrame(NewJobScreen)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Header.sizePolicy().hasHeightForWidth())
        self.Header.setSizePolicy(sizePolicy)
        self.Header.setMinimumSize(QtCore.QSize(0, 100))
        self.Header.setStyleSheet("QFrame {\n"
"    background-color: rgba(93, 173, 226, 1);\n"
"}")
        self.Header.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.Header.setFrameShadow(QtWidgets.QFrame.Plain)
        self.Header.setObjectName("Header")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.Header)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.back_button = QtWidgets.QPushButton(self.Header)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.back_button.sizePolicy().hasHeightForWidth())
        self.back_button.setSizePolicy(sizePolicy)
        self.back_button.setMinimumSize(QtCore.QSize(200, 65))
        self.back_button.setFocusPolicy(QtCore.Qt.NoFocus)
        self.back_button.setStyleSheet("QPushButton {\n"
"    image: url(:/buttons/buttons/back_button.png);\n"
"    background-color: rgba(165, 165, 165, 1);\n"
"    border-radius: 10px;\n"
"    font: 20pt \"Segoe UI\";\n"
" }\n"
"QPushButton:pressed {\n"
"    background-color: rgba(165, 165, 165, .7);\n"
"}\n"
"font: 20pt \"Segoe UI\";")
        self.back_button.setText("")
        self.back_button.setObjectName("back_button")
        self.horizontalLayout.addWidget(self.back_button)
        self.job_header = QtWidgets.QLabel(self.Header)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(48)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.job_header.setFont(font)
        self.job_header.setStyleSheet("color: rgb(255, 251, 244);")
        self.job_header.setObjectName("job_header")
        self.horizontalLayout.addWidget(self.job_header, 0, QtCore.Qt.AlignHCenter)
        self.proceed_button = QtWidgets.QPushButton(self.Header)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.proceed_button.sizePolicy().hasHeightForWidth())
        self.proceed_button.setSizePolicy(sizePolicy)
        self.proceed_button.setMinimumSize(QtCore.QSize(200, 65))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.proceed_button.setFont(font)
        self.proceed_button.setFocusPolicy(QtCore.Qt.NoFocus)
        self.proceed_button.setStyleSheet("QPushButton {\n"
"    image: url(:/buttons/buttons/proceed_button.png);\n"
"    background-color: rgba(165, 165, 165, 1);\n"
"    border-radius: 10px;\n"
"    font: 20pt \"Segoe UI\";\n"
" }\n"
"QPushButton:pressed {\n"
"    background-color: rgba(165, 165, 165, .7);\n"
"}")
        self.proceed_button.setText("")
        self.proceed_button.setObjectName("proceed_button")
        self.horizontalLayout.addWidget(self.proceed_button)
        self.verticalLayout.addWidget(self.Header)
        self.Screen = QtWidgets.QWidget(NewJobScreen)
        self.Screen.setStyleSheet("background-color: rgb(71, 79, 84);")
        self.Screen.setObjectName("Screen")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.Screen)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(25)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.project_info_frame = QtWidgets.QFrame(self.Screen)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(33)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.project_info_frame.sizePolicy().hasHeightForWidth())
        self.project_info_frame.setSizePolicy(sizePolicy)
        self.project_info_frame.setStyleSheet("QLabel {\n"
"    color: rgb(255, 251, 244);\n"
"}\n"
"QLineEdit {\n"
"    font: 16pt \"Segoe UI\";\n"
"    color: rgb(255, 251, 244);\n"
"}")
        self.project_info_frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.project_info_frame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.project_info_frame.setObjectName("project_info_frame")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.project_info_frame)
        self.verticalLayout_4.setSpacing(10)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.job_info_header = QtWidgets.QLabel(self.project_info_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.job_info_header.sizePolicy().hasHeightForWidth())
        self.job_info_header.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(24)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.job_info_header.setFont(font)
        self.job_info_header.setStyleSheet("color: rgb(255, 251, 244);")
        self.job_info_header.setObjectName("job_info_header")
        self.verticalLayout_4.addWidget(self.job_info_header, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        spacerItem = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_4.addItem(spacerItem)
        self.part_number_header = QtWidgets.QLabel(self.project_info_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.part_number_header.sizePolicy().hasHeightForWidth())
        self.part_number_header.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(18)
        self.part_number_header.setFont(font)
        self.part_number_header.setStyleSheet("")
        self.part_number_header.setObjectName("part_number_header")
        self.verticalLayout_4.addWidget(self.part_number_header, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.part_number = QtWidgets.QLineEdit(self.project_info_frame)
        self.part_number.setStyleSheet("")
        self.part_number.setObjectName("part_number")
        self.verticalLayout_4.addWidget(self.part_number)
        self.company_header = QtWidgets.QLabel(self.project_info_frame)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(18)
        self.company_header.setFont(font)
        self.company_header.setObjectName("company_header")
        self.verticalLayout_4.addWidget(self.company_header, 0, QtCore.Qt.AlignHCenter)
        self.company_name = QtWidgets.QLineEdit(self.project_info_frame)
        self.company_name.setObjectName("company_name")
        self.verticalLayout_4.addWidget(self.company_name)
        self.horizontalLayout_2.addWidget(self.project_info_frame, 0, QtCore.Qt.AlignTop)
        self.line = QtWidgets.QFrame(self.Screen)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.horizontalLayout_2.addWidget(self.line)
        self.spring_info_frame = QtWidgets.QFrame(self.Screen)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(33)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spring_info_frame.sizePolicy().hasHeightForWidth())
        self.spring_info_frame.setSizePolicy(sizePolicy)
        self.spring_info_frame.setStyleSheet("QLabel {\n"
"    color: rgb(255, 251, 244);\n"
"}\n"
"QLineEdit {\n"
"    font: 16pt \"Segoe UI\";\n"
"    color: rgb(255, 251, 244);\n"
"}\n"
"QComboBox {\n"
"    font: 16pt \"Segoe UI\";\n"
"    color: rgb(255, 251, 244);\n"
"}")
        self.spring_info_frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.spring_info_frame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.spring_info_frame.setObjectName("spring_info_frame")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.spring_info_frame)
        self.verticalLayout_10.setSpacing(10)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.spring_info_header = QtWidgets.QLabel(self.spring_info_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spring_info_header.sizePolicy().hasHeightForWidth())
        self.spring_info_header.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(24)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.spring_info_header.setFont(font)
        self.spring_info_header.setStyleSheet("color: rgb(255, 251, 244);")
        self.spring_info_header.setObjectName("spring_info_header")
        self.verticalLayout_10.addWidget(self.spring_info_header, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        spacerItem1 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_10.addItem(spacerItem1)
        self.spring_constant_header = QtWidgets.QLabel(self.spring_info_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spring_constant_header.sizePolicy().hasHeightForWidth())
        self.spring_constant_header.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(15)
        self.spring_constant_header.setFont(font)
        self.spring_constant_header.setStyleSheet("")
        self.spring_constant_header.setObjectName("spring_constant_header")
        self.verticalLayout_10.addWidget(self.spring_constant_header, 0, QtCore.Qt.AlignHCenter)
        self.spring_constant = QtWidgets.QLineEdit(self.spring_info_frame)
        self.spring_constant.setStyleSheet("")
        self.spring_constant.setObjectName("spring_constant")
        self.verticalLayout_10.addWidget(self.spring_constant)
        self.spring_length_header = QtWidgets.QLabel(self.spring_info_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spring_length_header.sizePolicy().hasHeightForWidth())
        self.spring_length_header.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(15)
        self.spring_length_header.setFont(font)
        self.spring_length_header.setStyleSheet("")
        self.spring_length_header.setObjectName("spring_length_header")
        self.verticalLayout_10.addWidget(self.spring_length_header, 0, QtCore.Qt.AlignHCenter)
        self.spring_length = QtWidgets.QLineEdit(self.spring_info_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spring_length.sizePolicy().hasHeightForWidth())
        self.spring_length.setSizePolicy(sizePolicy)
        self.spring_length.setStyleSheet("")
        self.spring_length.setObjectName("spring_length")
        self.verticalLayout_10.addWidget(self.spring_length)
        self.spring_type_header = QtWidgets.QLabel(self.spring_info_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spring_type_header.sizePolicy().hasHeightForWidth())
        self.spring_type_header.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(15)
        self.spring_type_header.setFont(font)
        self.spring_type_header.setStyleSheet("")
        self.spring_type_header.setObjectName("spring_type_header")
        self.verticalLayout_10.addWidget(self.spring_type_header, 0, QtCore.Qt.AlignHCenter)
        self.spring_type = QtWidgets.QComboBox(self.spring_info_frame)
        self.spring_type.setFocusPolicy(QtCore.Qt.NoFocus)
        self.spring_type.setStyleSheet("QComboBox {\n"
"    font: 16pt \"Segoe UI\";\n"
"    color: rgb(255, 251, 244);\n"
"}\n"
"QComboBox QAbstractItemView {\n"
"    font: 16pt \"Segoe UI\";\n"
"    color: rgb(255, 251, 244);\n"
"}")
        self.spring_type.setObjectName("spring_type")
        self.spring_type.addItem("")
        self.spring_type.addItem("")
        self.verticalLayout_10.addWidget(self.spring_type, 0, QtCore.Qt.AlignTop)
        self.spring_direction_header = QtWidgets.QLabel(self.spring_info_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spring_direction_header.sizePolicy().hasHeightForWidth())
        self.spring_direction_header.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(15)
        self.spring_direction_header.setFont(font)
        self.spring_direction_header.setStyleSheet("")
        self.spring_direction_header.setObjectName("spring_direction_header")
        self.verticalLayout_10.addWidget(self.spring_direction_header, 0, QtCore.Qt.AlignHCenter)
        self.spring_direction = QtWidgets.QComboBox(self.spring_info_frame)
        self.spring_direction.setFocusPolicy(QtCore.Qt.NoFocus)
        self.spring_direction.setStyleSheet("QComboBox {\n"
"    font: 16pt \"Segoe UI\";\n"
"    color: rgb(255, 251, 244);\n"
"}\n"
"QComboBox QAbstractItemView {\n"
"    font: 16pt \"Segoe UI\";\n"
"    color: rgb(255, 251, 244);\n"
"}")
        self.spring_direction.setObjectName("spring_direction")
        self.spring_direction.addItem("")
        self.spring_direction.addItem("")
        self.verticalLayout_10.addWidget(self.spring_direction, 0, QtCore.Qt.AlignTop)
        self.arbor_header = QtWidgets.QLabel(self.spring_info_frame)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(15)
        self.arbor_header.setFont(font)
        self.arbor_header.setObjectName("arbor_header")
        self.verticalLayout_10.addWidget(self.arbor_header, 0, QtCore.Qt.AlignHCenter)
        self.arbor_size = QtWidgets.QLineEdit(self.spring_info_frame)
        self.arbor_size.setObjectName("arbor_size")
        self.verticalLayout_10.addWidget(self.arbor_size)
        self.wire_diameter_header = QtWidgets.QLabel(self.spring_info_frame)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(15)
        self.wire_diameter_header.setFont(font)
        self.wire_diameter_header.setObjectName("wire_diameter_header")
        self.verticalLayout_10.addWidget(self.wire_diameter_header, 0, QtCore.Qt.AlignHCenter)
        self.wire_diameter = QtWidgets.QLineEdit(self.spring_info_frame)
        self.wire_diameter.setObjectName("wire_diameter")
        self.verticalLayout_10.addWidget(self.wire_diameter)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_10.addItem(spacerItem2)
        self.horizontalLayout_2.addWidget(self.spring_info_frame)
        self.spring_parameter_frame = QtWidgets.QFrame(self.Screen)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(33)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spring_parameter_frame.sizePolicy().hasHeightForWidth())
        self.spring_parameter_frame.setSizePolicy(sizePolicy)
        self.spring_parameter_frame.setStyleSheet("")
        self.spring_parameter_frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.spring_parameter_frame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.spring_parameter_frame.setObjectName("spring_parameter_frame")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.spring_parameter_frame)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.parameter_header = QtWidgets.QLabel(self.spring_parameter_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.parameter_header.sizePolicy().hasHeightForWidth())
        self.parameter_header.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(24)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.parameter_header.setFont(font)
        self.parameter_header.setStyleSheet("color: rgb(255, 251, 244);")
        self.parameter_header.setObjectName("parameter_header")
        self.verticalLayout_3.addWidget(self.parameter_header, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        spacerItem3 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_3.addItem(spacerItem3)
        self.feed_distance_frame = QtWidgets.QFrame(self.spring_parameter_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.feed_distance_frame.sizePolicy().hasHeightForWidth())
        self.feed_distance_frame.setSizePolicy(sizePolicy)
        self.feed_distance_frame.setStyleSheet("QLabel {\n"
"    font: 15pt \"Segoe UI\";\n"
"    color: rgb(255, 251, 244);\n"
"}")
        self.feed_distance_frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.feed_distance_frame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.feed_distance_frame.setObjectName("feed_distance_frame")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.feed_distance_frame)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.feed_distance_header = QtWidgets.QLabel(self.feed_distance_frame)
        self.feed_distance_header.setStyleSheet("")
        self.feed_distance_header.setObjectName("feed_distance_header")
        self.verticalLayout_9.addWidget(self.feed_distance_header, 0, QtCore.Qt.AlignHCenter)
        self.feed_distance_widget = QtWidgets.QWidget(self.feed_distance_frame)
        self.feed_distance_widget.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.feed_distance_widget.sizePolicy().hasHeightForWidth())
        self.feed_distance_widget.setSizePolicy(sizePolicy)
        self.feed_distance_widget.setStyleSheet("")
        self.feed_distance_widget.setObjectName("feed_distance_widget")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.feed_distance_widget)
        self.horizontalLayout_7.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.feed_distance_dec_button = QtWidgets.QPushButton(self.feed_distance_widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.feed_distance_dec_button.sizePolicy().hasHeightForWidth())
        self.feed_distance_dec_button.setSizePolicy(sizePolicy)
        self.feed_distance_dec_button.setMinimumSize(QtCore.QSize(54, 50))
        self.feed_distance_dec_button.setMaximumSize(QtCore.QSize(50, 50))
        font = QtGui.QFont()
        font.setFamily("Rockwell Condensed")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.feed_distance_dec_button.setFont(font)
        self.feed_distance_dec_button.setFocusPolicy(QtCore.Qt.NoFocus)
        self.feed_distance_dec_button.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.feed_distance_dec_button.setStyleSheet("QPushButton {\n"
"    border: 2px solid #8f8f91;\n"
"    border-bottom-left-radius: 10px;\n"
"    border-top-left-radius: 10px; \n"
"    background-color: rgb(193, 193, 193);\n"
"    min-width: 50px;\n"
" }\n"
"QPushButton:pressed {\n"
"    border: 2px solid #8f8f91;\n"
"    border-bottom-left-radius: 10px;\n"
"    border-top-left-radius: 10px; \n"
"    background-color: rgb(208, 208, 208);\n"
"    min-width: 50px;\n"
"}")
        self.feed_distance_dec_button.setObjectName("feed_distance_dec_button")
        self.horizontalLayout_7.addWidget(self.feed_distance_dec_button)
        self.feed_distance = QtWidgets.QLabel(self.feed_distance_widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.feed_distance.sizePolicy().hasHeightForWidth())
        self.feed_distance.setSizePolicy(sizePolicy)
        self.feed_distance.setMinimumSize(QtCore.QSize(90, 50))
        self.feed_distance.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(15)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.feed_distance.setFont(font)
        self.feed_distance.setStyleSheet("background-color: rgb(118, 118, 118);\n"
"color: rgb(255, 255, 245);\n"
"border-width: 0px;")
        self.feed_distance.setLineWidth(0)
        self.feed_distance.setAlignment(QtCore.Qt.AlignCenter)
        self.feed_distance.setObjectName("feed_distance")
        self.horizontalLayout_7.addWidget(self.feed_distance)
        self.feed_distance_inc_button = QtWidgets.QPushButton(self.feed_distance_widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.feed_distance_inc_button.sizePolicy().hasHeightForWidth())
        self.feed_distance_inc_button.setSizePolicy(sizePolicy)
        self.feed_distance_inc_button.setMinimumSize(QtCore.QSize(54, 50))
        self.feed_distance_inc_button.setMaximumSize(QtCore.QSize(50, 50))
        font = QtGui.QFont()
        font.setFamily("Rockwell Extra Bold")
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.feed_distance_inc_button.setFont(font)
        self.feed_distance_inc_button.setFocusPolicy(QtCore.Qt.NoFocus)
        self.feed_distance_inc_button.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.feed_distance_inc_button.setStyleSheet("QPushButton {\n"
"    border: 2px solid #8f8f91;\n"
"    border-bottom-right-radius: 10px;\n"
"    border-top-right-radius: 10px; \n"
"    background-color: rgb(193, 193, 193);\n"
"    min-width: 50px;\n"
"    text-align: center center;\n"
" }\n"
"QPushButton:pressed {\n"
"    border: 2px solid #8f8f91;\n"
"    border-bottom-right-radius: 10px;\n"
"    border-top-right-radius: 10px; \n"
"    background-color: rgb(208, 208, 208);\n"
"    min-width: 50px;\n"
"}")
        self.feed_distance_inc_button.setObjectName("feed_distance_inc_button")
        self.horizontalLayout_7.addWidget(self.feed_distance_inc_button, 0, QtCore.Qt.AlignVCenter)
        self.verticalLayout_9.addWidget(self.feed_distance_widget, 0, QtCore.Qt.AlignHCenter)
        self.verticalLayout_3.addWidget(self.feed_distance_frame)
        self.start_dead_turn_frame = QtWidgets.QFrame(self.spring_parameter_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.start_dead_turn_frame.sizePolicy().hasHeightForWidth())
        self.start_dead_turn_frame.setSizePolicy(sizePolicy)
        self.start_dead_turn_frame.setStyleSheet("QLabel {\n"
"    font: 15pt \"Segoe UI\";\n"
"    color: rgb(255, 251, 244);\n"
"}")
        self.start_dead_turn_frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.start_dead_turn_frame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.start_dead_turn_frame.setObjectName("start_dead_turn_frame")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.start_dead_turn_frame)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.start_dead_turn_header = QtWidgets.QLabel(self.start_dead_turn_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.start_dead_turn_header.sizePolicy().hasHeightForWidth())
        self.start_dead_turn_header.setSizePolicy(sizePolicy)
        self.start_dead_turn_header.setStyleSheet("")
        self.start_dead_turn_header.setObjectName("start_dead_turn_header")
        self.verticalLayout_7.addWidget(self.start_dead_turn_header, 0, QtCore.Qt.AlignHCenter)
        self.start_dead_turns_widget = QtWidgets.QWidget(self.start_dead_turn_frame)
        self.start_dead_turns_widget.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.start_dead_turns_widget.sizePolicy().hasHeightForWidth())
        self.start_dead_turns_widget.setSizePolicy(sizePolicy)
        self.start_dead_turns_widget.setStyleSheet("")
        self.start_dead_turns_widget.setObjectName("start_dead_turns_widget")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.start_dead_turns_widget)
        self.horizontalLayout_5.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.start_dead_turns_dec_button = QtWidgets.QPushButton(self.start_dead_turns_widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.start_dead_turns_dec_button.sizePolicy().hasHeightForWidth())
        self.start_dead_turns_dec_button.setSizePolicy(sizePolicy)
        self.start_dead_turns_dec_button.setMinimumSize(QtCore.QSize(54, 50))
        self.start_dead_turns_dec_button.setMaximumSize(QtCore.QSize(50, 50))
        font = QtGui.QFont()
        font.setFamily("Rockwell Condensed")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.start_dead_turns_dec_button.setFont(font)
        self.start_dead_turns_dec_button.setFocusPolicy(QtCore.Qt.NoFocus)
        self.start_dead_turns_dec_button.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.start_dead_turns_dec_button.setStyleSheet("QPushButton {\n"
"    border: 2px solid #8f8f91;\n"
"    border-bottom-left-radius: 10px;\n"
"    border-top-left-radius: 10px; \n"
"    background-color: rgb(193, 193, 193);\n"
"    min-width: 50px;\n"
" }\n"
"QPushButton:pressed {\n"
"    border: 2px solid #8f8f91;\n"
"    border-bottom-left-radius: 10px;\n"
"    border-top-left-radius: 10px; \n"
"    background-color: rgb(208, 208, 208);\n"
"    min-width: 50px;\n"
"}")
        self.start_dead_turns_dec_button.setObjectName("start_dead_turns_dec_button")
        self.horizontalLayout_5.addWidget(self.start_dead_turns_dec_button)
        self.start_dead_turns = QtWidgets.QLabel(self.start_dead_turns_widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.start_dead_turns.sizePolicy().hasHeightForWidth())
        self.start_dead_turns.setSizePolicy(sizePolicy)
        self.start_dead_turns.setMinimumSize(QtCore.QSize(90, 50))
        self.start_dead_turns.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(15)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.start_dead_turns.setFont(font)
        self.start_dead_turns.setStyleSheet("background-color: rgb(118, 118, 118);\n"
"color: rgb(255, 255, 245);\n"
"border-width: 0px;")
        self.start_dead_turns.setLineWidth(0)
        self.start_dead_turns.setAlignment(QtCore.Qt.AlignCenter)
        self.start_dead_turns.setObjectName("start_dead_turns")
        self.horizontalLayout_5.addWidget(self.start_dead_turns)
        self.start_dead_turns_inc_button = QtWidgets.QPushButton(self.start_dead_turns_widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.start_dead_turns_inc_button.sizePolicy().hasHeightForWidth())
        self.start_dead_turns_inc_button.setSizePolicy(sizePolicy)
        self.start_dead_turns_inc_button.setMinimumSize(QtCore.QSize(54, 50))
        self.start_dead_turns_inc_button.setMaximumSize(QtCore.QSize(50, 50))
        font = QtGui.QFont()
        font.setFamily("Rockwell Extra Bold")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.start_dead_turns_inc_button.setFont(font)
        self.start_dead_turns_inc_button.setFocusPolicy(QtCore.Qt.NoFocus)
        self.start_dead_turns_inc_button.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.start_dead_turns_inc_button.setStyleSheet("QPushButton {\n"
"    border: 2px solid #8f8f91;\n"
"    border-bottom-right-radius: 10px;\n"
"    border-top-right-radius: 10px; \n"
"    background-color: rgb(193, 193, 193);\n"
"    min-width: 50px;\n"
" }\n"
"QPushButton:pressed {\n"
"    border: 2px solid #8f8f91;\n"
"    border-bottom-right-radius: 10px;\n"
"    border-top-right-radius: 10px; \n"
"    background-color: rgb(208, 208, 208);\n"
"    min-width: 50px;\n"
"}")
        self.start_dead_turns_inc_button.setObjectName("start_dead_turns_inc_button")
        self.horizontalLayout_5.addWidget(self.start_dead_turns_inc_button)
        self.verticalLayout_7.addWidget(self.start_dead_turns_widget, 0, QtCore.Qt.AlignHCenter)
        self.verticalLayout_3.addWidget(self.start_dead_turn_frame)
        self.live_turn_frame = QtWidgets.QFrame(self.spring_parameter_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.live_turn_frame.sizePolicy().hasHeightForWidth())
        self.live_turn_frame.setSizePolicy(sizePolicy)
        self.live_turn_frame.setStyleSheet("QLabel {\n"
"    font: 15pt \"Segoe UI\";\n"
"    color: rgb(255, 251, 244);\n"
"}")
        self.live_turn_frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.live_turn_frame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.live_turn_frame.setObjectName("live_turn_frame")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.live_turn_frame)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.live_turn_header = QtWidgets.QLabel(self.live_turn_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.live_turn_header.sizePolicy().hasHeightForWidth())
        self.live_turn_header.setSizePolicy(sizePolicy)
        self.live_turn_header.setStyleSheet("")
        self.live_turn_header.setObjectName("live_turn_header")
        self.verticalLayout_8.addWidget(self.live_turn_header, 0, QtCore.Qt.AlignHCenter)
        self.live_turn_widget = QtWidgets.QWidget(self.live_turn_frame)
        self.live_turn_widget.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.live_turn_widget.sizePolicy().hasHeightForWidth())
        self.live_turn_widget.setSizePolicy(sizePolicy)
        self.live_turn_widget.setStyleSheet("")
        self.live_turn_widget.setObjectName("live_turn_widget")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.live_turn_widget)
        self.horizontalLayout_6.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.live_turn_dec_button = QtWidgets.QPushButton(self.live_turn_widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.live_turn_dec_button.sizePolicy().hasHeightForWidth())
        self.live_turn_dec_button.setSizePolicy(sizePolicy)
        self.live_turn_dec_button.setMinimumSize(QtCore.QSize(54, 50))
        self.live_turn_dec_button.setMaximumSize(QtCore.QSize(50, 50))
        font = QtGui.QFont()
        font.setFamily("Rockwell Condensed")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.live_turn_dec_button.setFont(font)
        self.live_turn_dec_button.setFocusPolicy(QtCore.Qt.NoFocus)
        self.live_turn_dec_button.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.live_turn_dec_button.setStyleSheet("QPushButton {\n"
"    border: 2px solid #8f8f91;\n"
"    border-bottom-left-radius: 10px;\n"
"    border-top-left-radius: 10px; \n"
"    background-color: rgb(193, 193, 193);\n"
"    min-width: 50px;\n"
" }\n"
"QPushButton:pressed {\n"
"    border: 2px solid #8f8f91;\n"
"    border-bottom-left-radius: 10px;\n"
"    border-top-left-radius: 10px; \n"
"    background-color: rgb(208, 208, 208);\n"
"    min-width: 50px;\n"
"}")
        self.live_turn_dec_button.setObjectName("live_turn_dec_button")
        self.horizontalLayout_6.addWidget(self.live_turn_dec_button)
        self.live_turns = QtWidgets.QLabel(self.live_turn_widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.live_turns.sizePolicy().hasHeightForWidth())
        self.live_turns.setSizePolicy(sizePolicy)
        self.live_turns.setMinimumSize(QtCore.QSize(90, 50))
        self.live_turns.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(15)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.live_turns.setFont(font)
        self.live_turns.setStyleSheet("background-color: rgb(118, 118, 118);\n"
"color: rgb(255, 255, 245);\n"
"border-width: 0px;")
        self.live_turns.setLineWidth(0)
        self.live_turns.setAlignment(QtCore.Qt.AlignCenter)
        self.live_turns.setObjectName("live_turns")
        self.horizontalLayout_6.addWidget(self.live_turns)
        self.live_turn_inc_button = QtWidgets.QPushButton(self.live_turn_widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.live_turn_inc_button.sizePolicy().hasHeightForWidth())
        self.live_turn_inc_button.setSizePolicy(sizePolicy)
        self.live_turn_inc_button.setMinimumSize(QtCore.QSize(54, 50))
        self.live_turn_inc_button.setMaximumSize(QtCore.QSize(50, 50))
        font = QtGui.QFont()
        font.setFamily("Rockwell Extra Bold")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.live_turn_inc_button.setFont(font)
        self.live_turn_inc_button.setFocusPolicy(QtCore.Qt.NoFocus)
        self.live_turn_inc_button.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.live_turn_inc_button.setStyleSheet("QPushButton {\n"
"    border: 2px solid #8f8f91;\n"
"    border-bottom-right-radius: 10px;\n"
"    border-top-right-radius: 10px; \n"
"    background-color: rgb(193, 193, 193);\n"
"    min-width: 50px;\n"
" }\n"
"QPushButton:pressed {\n"
"    border: 2px solid #8f8f91;\n"
"    border-bottom-right-radius: 10px;\n"
"    border-top-right-radius: 10px; \n"
"    background-color: rgb(208, 208, 208);\n"
"    min-width: 50px;\n"
"}")
        self.live_turn_inc_button.setObjectName("live_turn_inc_button")
        self.horizontalLayout_6.addWidget(self.live_turn_inc_button)
        self.verticalLayout_8.addWidget(self.live_turn_widget, 0, QtCore.Qt.AlignHCenter)
        self.verticalLayout_3.addWidget(self.live_turn_frame)
        self.live_turn_spacing_frame = QtWidgets.QFrame(self.spring_parameter_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.live_turn_spacing_frame.sizePolicy().hasHeightForWidth())
        self.live_turn_spacing_frame.setSizePolicy(sizePolicy)
        self.live_turn_spacing_frame.setStyleSheet("QLabel {\n"
"    font: 15pt \"Segoe UI\";\n"
"    color: rgb(255, 251, 244);\n"
"}")
        self.live_turn_spacing_frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.live_turn_spacing_frame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.live_turn_spacing_frame.setObjectName("live_turn_spacing_frame")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.live_turn_spacing_frame)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.live_turn_spacing_header = QtWidgets.QLabel(self.live_turn_spacing_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.live_turn_spacing_header.sizePolicy().hasHeightForWidth())
        self.live_turn_spacing_header.setSizePolicy(sizePolicy)
        self.live_turn_spacing_header.setStyleSheet("")
        self.live_turn_spacing_header.setObjectName("live_turn_spacing_header")
        self.verticalLayout_5.addWidget(self.live_turn_spacing_header, 0, QtCore.Qt.AlignHCenter)
        self.live_turn_spacing_widget = QtWidgets.QWidget(self.live_turn_spacing_frame)
        self.live_turn_spacing_widget.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.live_turn_spacing_widget.sizePolicy().hasHeightForWidth())
        self.live_turn_spacing_widget.setSizePolicy(sizePolicy)
        self.live_turn_spacing_widget.setStyleSheet("")
        self.live_turn_spacing_widget.setObjectName("live_turn_spacing_widget")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.live_turn_spacing_widget)
        self.horizontalLayout_3.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.live_turn_spacing_dec_button = QtWidgets.QPushButton(self.live_turn_spacing_widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.live_turn_spacing_dec_button.sizePolicy().hasHeightForWidth())
        self.live_turn_spacing_dec_button.setSizePolicy(sizePolicy)
        self.live_turn_spacing_dec_button.setMinimumSize(QtCore.QSize(54, 50))
        self.live_turn_spacing_dec_button.setMaximumSize(QtCore.QSize(50, 50))
        font = QtGui.QFont()
        font.setFamily("Rockwell Condensed")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.live_turn_spacing_dec_button.setFont(font)
        self.live_turn_spacing_dec_button.setFocusPolicy(QtCore.Qt.NoFocus)
        self.live_turn_spacing_dec_button.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.live_turn_spacing_dec_button.setStyleSheet("QPushButton {\n"
"    border: 2px solid #8f8f91;\n"
"    border-bottom-left-radius: 10px;\n"
"    border-top-left-radius: 10px; \n"
"    background-color: rgb(193, 193, 193);\n"
"    min-width: 50px;\n"
" }\n"
"QPushButton:pressed {\n"
"    border: 2px solid #8f8f91;\n"
"    border-bottom-left-radius: 10px;\n"
"    border-top-left-radius: 10px; \n"
"    background-color: rgb(208, 208, 208);\n"
"    min-width: 50px;\n"
"}")
        self.live_turn_spacing_dec_button.setObjectName("live_turn_spacing_dec_button")
        self.horizontalLayout_3.addWidget(self.live_turn_spacing_dec_button)
        self.live_turn_spacing = QtWidgets.QLabel(self.live_turn_spacing_widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.live_turn_spacing.sizePolicy().hasHeightForWidth())
        self.live_turn_spacing.setSizePolicy(sizePolicy)
        self.live_turn_spacing.setMinimumSize(QtCore.QSize(90, 50))
        self.live_turn_spacing.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(15)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.live_turn_spacing.setFont(font)
        self.live_turn_spacing.setStyleSheet("background-color: rgb(118, 118, 118);\n"
"color: rgb(255, 255, 245);\n"
"border-width: 0px;")
        self.live_turn_spacing.setLineWidth(0)
        self.live_turn_spacing.setAlignment(QtCore.Qt.AlignCenter)
        self.live_turn_spacing.setObjectName("live_turn_spacing")
        self.horizontalLayout_3.addWidget(self.live_turn_spacing)
        self.live_turn_spacing_inc_button = QtWidgets.QPushButton(self.live_turn_spacing_widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.live_turn_spacing_inc_button.sizePolicy().hasHeightForWidth())
        self.live_turn_spacing_inc_button.setSizePolicy(sizePolicy)
        self.live_turn_spacing_inc_button.setMinimumSize(QtCore.QSize(54, 50))
        self.live_turn_spacing_inc_button.setMaximumSize(QtCore.QSize(50, 50))
        font = QtGui.QFont()
        font.setFamily("Rockwell Extra Bold")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.live_turn_spacing_inc_button.setFont(font)
        self.live_turn_spacing_inc_button.setFocusPolicy(QtCore.Qt.NoFocus)
        self.live_turn_spacing_inc_button.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.live_turn_spacing_inc_button.setStyleSheet("QPushButton {\n"
"    border: 2px solid #8f8f91;\n"
"    border-bottom-right-radius: 10px;\n"
"    border-top-right-radius: 10px; \n"
"    background-color: rgb(193, 193, 193);\n"
"    min-width: 50px;\n"
" }\n"
"QPushButton:pressed {\n"
"    border: 2px solid #8f8f91;\n"
"    border-bottom-right-radius: 10px;\n"
"    border-top-right-radius: 10px; \n"
"    background-color: rgb(208, 208, 208);\n"
"    min-width: 50px;\n"
"}")
        self.live_turn_spacing_inc_button.setObjectName("live_turn_spacing_inc_button")
        self.horizontalLayout_3.addWidget(self.live_turn_spacing_inc_button)
        self.verticalLayout_5.addWidget(self.live_turn_spacing_widget, 0, QtCore.Qt.AlignHCenter)
        self.verticalLayout_3.addWidget(self.live_turn_spacing_frame)
        self.end_dead_turn_frame = QtWidgets.QFrame(self.spring_parameter_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.end_dead_turn_frame.sizePolicy().hasHeightForWidth())
        self.end_dead_turn_frame.setSizePolicy(sizePolicy)
        self.end_dead_turn_frame.setStyleSheet("QLabel {\n"
"    font: 15pt \"Segoe UI\";\n"
"    color: rgb(255, 251, 244);\n"
"}")
        self.end_dead_turn_frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.end_dead_turn_frame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.end_dead_turn_frame.setObjectName("end_dead_turn_frame")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.end_dead_turn_frame)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.end_dead_turn_header = QtWidgets.QLabel(self.end_dead_turn_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.end_dead_turn_header.sizePolicy().hasHeightForWidth())
        self.end_dead_turn_header.setSizePolicy(sizePolicy)
        self.end_dead_turn_header.setStyleSheet("")
        self.end_dead_turn_header.setObjectName("end_dead_turn_header")
        self.verticalLayout_6.addWidget(self.end_dead_turn_header, 0, QtCore.Qt.AlignHCenter)
        self.end_dead_turn_widget = QtWidgets.QWidget(self.end_dead_turn_frame)
        self.end_dead_turn_widget.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.end_dead_turn_widget.sizePolicy().hasHeightForWidth())
        self.end_dead_turn_widget.setSizePolicy(sizePolicy)
        self.end_dead_turn_widget.setStyleSheet("")
        self.end_dead_turn_widget.setObjectName("end_dead_turn_widget")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.end_dead_turn_widget)
        self.horizontalLayout_4.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.end_dead_turns_dec_button = QtWidgets.QPushButton(self.end_dead_turn_widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.end_dead_turns_dec_button.sizePolicy().hasHeightForWidth())
        self.end_dead_turns_dec_button.setSizePolicy(sizePolicy)
        self.end_dead_turns_dec_button.setMinimumSize(QtCore.QSize(54, 50))
        self.end_dead_turns_dec_button.setMaximumSize(QtCore.QSize(50, 50))
        font = QtGui.QFont()
        font.setFamily("Rockwell Condensed")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.end_dead_turns_dec_button.setFont(font)
        self.end_dead_turns_dec_button.setFocusPolicy(QtCore.Qt.NoFocus)
        self.end_dead_turns_dec_button.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.end_dead_turns_dec_button.setStyleSheet("QPushButton {\n"
"    border: 2px solid #8f8f91;\n"
"    border-bottom-left-radius: 10px;\n"
"    border-top-left-radius: 10px; \n"
"    background-color: rgb(193, 193, 193);\n"
"    min-width: 50px;\n"
" }\n"
"QPushButton:pressed {\n"
"    border: 2px solid #8f8f91;\n"
"    border-bottom-left-radius: 10px;\n"
"    border-top-left-radius: 10px; \n"
"    background-color: rgb(208, 208, 208);\n"
"    min-width: 50px;\n"
"}")
        self.end_dead_turns_dec_button.setObjectName("end_dead_turns_dec_button")
        self.horizontalLayout_4.addWidget(self.end_dead_turns_dec_button)
        self.end_dead_turns = QtWidgets.QLabel(self.end_dead_turn_widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.end_dead_turns.sizePolicy().hasHeightForWidth())
        self.end_dead_turns.setSizePolicy(sizePolicy)
        self.end_dead_turns.setMinimumSize(QtCore.QSize(90, 50))
        self.end_dead_turns.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(15)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.end_dead_turns.setFont(font)
        self.end_dead_turns.setStyleSheet("background-color: rgb(118, 118, 118);\n"
"color: rgb(255, 255, 245);\n"
"border-width: 0px;")
        self.end_dead_turns.setLineWidth(0)
        self.end_dead_turns.setAlignment(QtCore.Qt.AlignCenter)
        self.end_dead_turns.setObjectName("end_dead_turns")
        self.horizontalLayout_4.addWidget(self.end_dead_turns)
        self.end_dead_turns_inc_button = QtWidgets.QPushButton(self.end_dead_turn_widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.end_dead_turns_inc_button.sizePolicy().hasHeightForWidth())
        self.end_dead_turns_inc_button.setSizePolicy(sizePolicy)
        self.end_dead_turns_inc_button.setMinimumSize(QtCore.QSize(54, 50))
        self.end_dead_turns_inc_button.setMaximumSize(QtCore.QSize(50, 50))
        font = QtGui.QFont()
        font.setFamily("Rockwell Extra Bold")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.end_dead_turns_inc_button.setFont(font)
        self.end_dead_turns_inc_button.setFocusPolicy(QtCore.Qt.NoFocus)
        self.end_dead_turns_inc_button.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.end_dead_turns_inc_button.setStyleSheet("QPushButton {\n"
"    border: 2px solid #8f8f91;\n"
"    border-bottom-right-radius: 10px;\n"
"    border-top-right-radius: 10px; \n"
"    background-color: rgb(193, 193, 193);\n"
"    min-width: 50px;\n"
" }\n"
"QPushButton:pressed {\n"
"    border: 2px solid #8f8f91;\n"
"    border-bottom-right-radius: 10px;\n"
"    border-top-right-radius: 10px; \n"
"    background-color: rgb(208, 208, 208);\n"
"    min-width: 50px;\n"
"}")
        self.end_dead_turns_inc_button.setObjectName("end_dead_turns_inc_button")
        self.horizontalLayout_4.addWidget(self.end_dead_turns_inc_button)
        self.verticalLayout_6.addWidget(self.end_dead_turn_widget, 0, QtCore.Qt.AlignHCenter)
        self.verticalLayout_3.addWidget(self.end_dead_turn_frame)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem4)
        self.horizontalLayout_2.addWidget(self.spring_parameter_frame)
        self.verticalLayout.addWidget(self.Screen)

        self.retranslateUi(NewJobScreen)
        QtCore.QMetaObject.connectSlotsByName(NewJobScreen)

    def retranslateUi(self, NewJobScreen):
        _translate = QtCore.QCoreApplication.translate
        NewJobScreen.setWindowTitle(_translate("NewJobScreen", "Form"))
        self.job_header.setText(_translate("NewJobScreen", "New Job"))
        self.job_info_header.setText(_translate("NewJobScreen", "Job Info"))
        self.part_number_header.setText(_translate("NewJobScreen", "Part Number"))
        self.company_header.setText(_translate("NewJobScreen", "Company"))
        self.spring_info_header.setText(_translate("NewJobScreen", "Spring Info"))
        self.spring_constant_header.setText(_translate("NewJobScreen", "Spring Constant"))
        self.spring_length_header.setText(_translate("NewJobScreen", "Spring Length (in)"))
        self.spring_type_header.setText(_translate("NewJobScreen", "Spring Type"))
        self.spring_type.setItemText(0, _translate("NewJobScreen", "Compression"))
        self.spring_type.setItemText(1, _translate("NewJobScreen", "Extension"))
        self.spring_direction_header.setText(_translate("NewJobScreen", "Spring Wind Direction"))
        self.spring_direction.setItemText(0, _translate("NewJobScreen", "Left"))
        self.spring_direction.setItemText(1, _translate("NewJobScreen", "Right"))
        self.arbor_header.setText(_translate("NewJobScreen", "Arbor Size (in)"))
        self.wire_diameter_header.setText(_translate("NewJobScreen", "Wire Diameter (in)"))
        self.parameter_header.setText(_translate("NewJobScreen", "Spring Parameters"))
        self.feed_distance_header.setText(_translate("NewJobScreen", "Feed Distance (in)"))
        self.feed_distance_dec_button.setText(_translate("NewJobScreen", "-"))
        self.feed_distance.setText(_translate("NewJobScreen", "15"))
        self.feed_distance_inc_button.setText(_translate("NewJobScreen", "+"))
        self.start_dead_turn_header.setText(_translate("NewJobScreen", "Start Dead Turns"))
        self.start_dead_turns_dec_button.setText(_translate("NewJobScreen", "-"))
        self.start_dead_turns.setText(_translate("NewJobScreen", "15"))
        self.start_dead_turns_inc_button.setText(_translate("NewJobScreen", "+"))
        self.live_turn_header.setText(_translate("NewJobScreen", "Live Turns"))
        self.live_turn_dec_button.setText(_translate("NewJobScreen", "-"))
        self.live_turns.setText(_translate("NewJobScreen", "15"))
        self.live_turn_inc_button.setText(_translate("NewJobScreen", "+"))
        self.live_turn_spacing_header.setText(_translate("NewJobScreen", "Live Turn Spacing (in)"))
        self.live_turn_spacing_dec_button.setText(_translate("NewJobScreen", "-"))
        self.live_turn_spacing.setText(_translate("NewJobScreen", "15"))
        self.live_turn_spacing_inc_button.setText(_translate("NewJobScreen", "+"))
        self.end_dead_turn_header.setText(_translate("NewJobScreen", "End Dead Turns"))
        self.end_dead_turns_dec_button.setText(_translate("NewJobScreen", "-"))
        self.end_dead_turns.setText(_translate("NewJobScreen", "15"))
        self.end_dead_turns_inc_button.setText(_translate("NewJobScreen", "+"))
from . import Spring_Serpent_Resources_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    NewJobScreen = QtWidgets.QWidget()
    ui = Ui_NewJobScreen()
    ui.setupUi(NewJobScreen)
    NewJobScreen.show()
    sys.exit(app.exec_())

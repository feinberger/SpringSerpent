# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\Projects\Spring Serpent\Spring-Serpent\designer\JobLibraryScreen.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_JobLibraryScreen(object):
    def setupUi(self, JobLibraryScreen):
        JobLibraryScreen.setObjectName("JobLibraryScreen")
        JobLibraryScreen.resize(1360, 768)
        self.verticalLayout = QtWidgets.QVBoxLayout(JobLibraryScreen)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.Header = QtWidgets.QFrame(JobLibraryScreen)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Header.sizePolicy().hasHeightForWidth())
        self.Header.setSizePolicy(sizePolicy)
        self.Header.setMinimumSize(QtCore.QSize(0, 100))
        self.Header.setStyleSheet("QFrame {\n"
"    background-color: rgba(175, 122, 197,1);\n"
"}")
        self.Header.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.Header.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Header.setObjectName("Header")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.Header)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.home_button = QtWidgets.QPushButton(self.Header)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.home_button.sizePolicy().hasHeightForWidth())
        self.home_button.setSizePolicy(sizePolicy)
        self.home_button.setMinimumSize(QtCore.QSize(200, 65))
        self.home_button.setFocusPolicy(QtCore.Qt.NoFocus)
        self.home_button.setStyleSheet("QPushButton {\n"
"    image: url(:/buttons/buttons/home_button.png);\n"
"    background-color: rgba(165, 165, 165, 1);\n"
"    border-radius: 10px;\n"
"    font: 20pt \"Segoe UI\";\n"
" }\n"
"QPushButton:pressed {\n"
"    background-color: rgba(165, 165, 165, .7);\n"
"}\n"
"font: 20pt \"Segoe UI\";")
        self.home_button.setText("")
        self.home_button.setObjectName("home_button")
        self.horizontalLayout.addWidget(self.home_button)
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
        self.proceed_stack = QtWidgets.QStackedWidget(self.Header)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.proceed_stack.sizePolicy().hasHeightForWidth())
        self.proceed_stack.setSizePolicy(sizePolicy)
        self.proceed_stack.setObjectName("proceed_stack")
        self.proceed_widget = QtWidgets.QWidget()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.proceed_widget.sizePolicy().hasHeightForWidth())
        self.proceed_widget.setSizePolicy(sizePolicy)
        self.proceed_widget.setStyleSheet("background-color: rgba(175, 122, 197,1);")
        self.proceed_widget.setObjectName("proceed_widget")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.proceed_widget)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.proceed_button = QtWidgets.QPushButton(self.proceed_widget)
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
        self.horizontalLayout_3.addWidget(self.proceed_button)
        self.proceed_stack.addWidget(self.proceed_widget)
        self.spacer_widget = QtWidgets.QWidget()
        self.spacer_widget.setStyleSheet("background-color: rgba(175, 122, 197,1);")
        self.spacer_widget.setObjectName("spacer_widget")
        self.proceed_stack.addWidget(self.spacer_widget)
        self.horizontalLayout.addWidget(self.proceed_stack)
        self.verticalLayout.addWidget(self.Header)
        self.Screen = QtWidgets.QWidget(JobLibraryScreen)
        self.Screen.setStyleSheet("background-color: rgb(71, 79, 84);")
        self.Screen.setObjectName("Screen")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.Screen)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.search_frame = QtWidgets.QFrame(self.Screen)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(20)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.search_frame.sizePolicy().hasHeightForWidth())
        self.search_frame.setSizePolicy(sizePolicy)
        self.search_frame.setStyleSheet("QLineEdit {\n"
"    font: 16pt \"Segoe UI\";\n"
"    color: rgb(255, 251, 244);\n"
"}")
        self.search_frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.search_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.search_frame.setObjectName("search_frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.search_frame)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.filter_header = QtWidgets.QLabel(self.search_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.filter_header.sizePolicy().hasHeightForWidth())
        self.filter_header.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(24)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.filter_header.setFont(font)
        self.filter_header.setStyleSheet("color: rgb(255, 251, 244);")
        self.filter_header.setObjectName("filter_header")
        self.verticalLayout_2.addWidget(self.filter_header, 0, QtCore.Qt.AlignHCenter)
        spacerItem = QtWidgets.QSpacerItem(20, 15, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_2.addItem(spacerItem)
        self.part_number_filter_frame = QtWidgets.QFrame(self.search_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.part_number_filter_frame.sizePolicy().hasHeightForWidth())
        self.part_number_filter_frame.setSizePolicy(sizePolicy)
        self.part_number_filter_frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.part_number_filter_frame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.part_number_filter_frame.setObjectName("part_number_filter_frame")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.part_number_filter_frame)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.part_number_header = QtWidgets.QLabel(self.part_number_filter_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.part_number_header.sizePolicy().hasHeightForWidth())
        self.part_number_header.setSizePolicy(sizePolicy)
        self.part_number_header.setStyleSheet("QLabel {\n"
"    font: 16pt \"Segoe UI\";\n"
"    color: rgb(255, 251, 244);\n"
"}")
        self.part_number_header.setObjectName("part_number_header")
        self.verticalLayout_5.addWidget(self.part_number_header, 0, QtCore.Qt.AlignHCenter)
        self.part_number = QtWidgets.QLineEdit(self.part_number_filter_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.part_number.sizePolicy().hasHeightForWidth())
        self.part_number.setSizePolicy(sizePolicy)
        self.part_number.setMinimumSize(QtCore.QSize(325, 0))
        self.part_number.setMaximumSize(QtCore.QSize(325, 16777215))
        self.part_number.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.part_number.setText("")
        self.part_number.setAlignment(QtCore.Qt.AlignCenter)
        self.part_number.setObjectName("part_number")
        self.verticalLayout_5.addWidget(self.part_number)
        self.verticalLayout_2.addWidget(self.part_number_filter_frame)
        self.company_filter_frame = QtWidgets.QFrame(self.search_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.company_filter_frame.sizePolicy().hasHeightForWidth())
        self.company_filter_frame.setSizePolicy(sizePolicy)
        self.company_filter_frame.setStyleSheet("QLabel {\n"
"    font: 16pt \"Segoe UI\";\n"
"    color: rgb(255, 251, 244);\n"
"}\n"
"QLineEdit {\n"
"    font: 16pt \"Segoe UI\";\n"
"    color: rgb(255, 251, 244);\n"
"}")
        self.company_filter_frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.company_filter_frame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.company_filter_frame.setObjectName("company_filter_frame")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.company_filter_frame)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setSpacing(6)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.company_header = QtWidgets.QLabel(self.company_filter_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.company_header.sizePolicy().hasHeightForWidth())
        self.company_header.setSizePolicy(sizePolicy)
        self.company_header.setObjectName("company_header")
        self.verticalLayout_4.addWidget(self.company_header, 0, QtCore.Qt.AlignHCenter)
        self.company_name = QtWidgets.QLineEdit(self.company_filter_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.company_name.sizePolicy().hasHeightForWidth())
        self.company_name.setSizePolicy(sizePolicy)
        self.company_name.setMinimumSize(QtCore.QSize(325, 0))
        self.company_name.setMaximumSize(QtCore.QSize(150, 16777215))
        self.company_name.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.company_name.setText("")
        self.company_name.setAlignment(QtCore.Qt.AlignCenter)
        self.company_name.setObjectName("company_name")
        self.verticalLayout_4.addWidget(self.company_name)
        self.verticalLayout_2.addWidget(self.company_filter_frame)
        self.spring_type_filter_frame = QtWidgets.QFrame(self.search_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spring_type_filter_frame.sizePolicy().hasHeightForWidth())
        self.spring_type_filter_frame.setSizePolicy(sizePolicy)
        self.spring_type_filter_frame.setStyleSheet("QLabel {\n"
"    font: 16pt \"Segoe UI\";\n"
"    color: rgb(255, 251, 244);\n"
"}\n"
"QCheckBox {\n"
"    font: 16pt \"Segoe UI\";\n"
"    color: rgb(255, 251, 244);\n"
"}")
        self.spring_type_filter_frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.spring_type_filter_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.spring_type_filter_frame.setObjectName("spring_type_filter_frame")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.spring_type_filter_frame)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.spring_type_header = QtWidgets.QLabel(self.spring_type_filter_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spring_type_header.sizePolicy().hasHeightForWidth())
        self.spring_type_header.setSizePolicy(sizePolicy)
        self.spring_type_header.setObjectName("spring_type_header")
        self.verticalLayout_7.addWidget(self.spring_type_header, 0, QtCore.Qt.AlignHCenter)
        self.checkbox_frame = QtWidgets.QFrame(self.spring_type_filter_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkbox_frame.sizePolicy().hasHeightForWidth())
        self.checkbox_frame.setSizePolicy(sizePolicy)
        self.checkbox_frame.setStyleSheet("QCheckBox {\n"
"    font: 16pt \"Segoe UI\";\n"
"    color: rgb(255, 251, 244);\n"
"}")
        self.checkbox_frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.checkbox_frame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.checkbox_frame.setObjectName("checkbox_frame")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.checkbox_frame)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.compression_spring = QtWidgets.QCheckBox(self.checkbox_frame)
        self.compression_spring.setStyleSheet("")
        self.compression_spring.setObjectName("compression_spring")
        self.horizontalLayout_6.addWidget(self.compression_spring, 0, QtCore.Qt.AlignHCenter)
        self.extension_spring = QtWidgets.QCheckBox(self.checkbox_frame)
        self.extension_spring.setObjectName("extension_spring")
        self.horizontalLayout_6.addWidget(self.extension_spring, 0, QtCore.Qt.AlignHCenter)
        self.verticalLayout_7.addWidget(self.checkbox_frame, 0, QtCore.Qt.AlignHCenter)
        self.verticalLayout_2.addWidget(self.spring_type_filter_frame, 0, QtCore.Qt.AlignHCenter)
        spacerItem1 = QtWidgets.QSpacerItem(20, 60, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_2.addItem(spacerItem1)
        self.scan_code_button = QtWidgets.QPushButton(self.search_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scan_code_button.sizePolicy().hasHeightForWidth())
        self.scan_code_button.setSizePolicy(sizePolicy)
        self.scan_code_button.setMinimumSize(QtCore.QSize(250, 130))
        self.scan_code_button.setStyleSheet("QPushButton {\n"
"    background-color: rgba(52, 152, 219, 1);\n"
"    border-radius: 10px;\n"
"    font: 20pt \"Segoe UI\";\n"
"    color: rgb(255, 251, 244);\n"
" }\n"
"QPushButton:pressed {\n"
"    background-color: rgba(52, 152, 219, .7);\n"
"}\n"
"QPushButton:disabled {\n"
"    background-color: rgba(52, 152, 219, .7);\n"
"}")
        self.scan_code_button.setObjectName("scan_code_button")
        self.verticalLayout_2.addWidget(self.scan_code_button, 0, QtCore.Qt.AlignHCenter)
        self.barcode_edit = QtWidgets.QLineEdit(self.search_frame)
        self.barcode_edit.setAlignment(QtCore.Qt.AlignCenter)
        self.barcode_edit.setObjectName("barcode_edit")
        self.verticalLayout_2.addWidget(self.barcode_edit)
        spacerItem2 = QtWidgets.QSpacerItem(20, 80, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem2)
        self.horizontalLayout_2.addWidget(self.search_frame)
        self.line = QtWidgets.QFrame(self.Screen)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.horizontalLayout_2.addWidget(self.line)
        self.job_library_table_frame = QtWidgets.QFrame(self.Screen)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(80)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.job_library_table_frame.sizePolicy().hasHeightForWidth())
        self.job_library_table_frame.setSizePolicy(sizePolicy)
        self.job_library_table_frame.setMinimumSize(QtCore.QSize(0, 0))
        self.job_library_table_frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.job_library_table_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.job_library_table_frame.setObjectName("job_library_table_frame")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.job_library_table_frame)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.widget = QtWidgets.QWidget(self.job_library_table_frame)
        self.widget.setObjectName("widget")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem3 = QtWidgets.QSpacerItem(218, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem3)
        self.projects_header = QtWidgets.QLabel(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.projects_header.sizePolicy().hasHeightForWidth())
        self.projects_header.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.projects_header.setFont(font)
        self.projects_header.setStyleSheet("color: rgb(255, 251, 244);")
        self.projects_header.setObjectName("projects_header")
        self.horizontalLayout_4.addWidget(self.projects_header, 0, QtCore.Qt.AlignHCenter)
        self.delete_stack = QtWidgets.QStackedWidget(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.delete_stack.sizePolicy().hasHeightForWidth())
        self.delete_stack.setSizePolicy(sizePolicy)
        self.delete_stack.setMinimumSize(QtCore.QSize(0, 65))
        self.delete_stack.setObjectName("delete_stack")
        self.spacer_widget_2 = QtWidgets.QWidget()
        self.spacer_widget_2.setObjectName("spacer_widget_2")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.spacer_widget_2)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        spacerItem4 = QtWidgets.QSpacerItem(197, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem4)
        self.delete_stack.addWidget(self.spacer_widget_2)
        self.delete_widget = QtWidgets.QWidget()
        self.delete_widget.setObjectName("delete_widget")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.delete_widget)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.delete_button = QtWidgets.QPushButton(self.delete_widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.delete_button.sizePolicy().hasHeightForWidth())
        self.delete_button.setSizePolicy(sizePolicy)
        self.delete_button.setMinimumSize(QtCore.QSize(200, 40))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.delete_button.setFont(font)
        self.delete_button.setFocusPolicy(QtCore.Qt.NoFocus)
        self.delete_button.setStyleSheet("QPushButton {\n"
"    background-color: rgba(231, 76, 60, 1);\n"
"    border-radius: 10px;\n"
"    color: rgb(255, 251, 244);\n"
" }\n"
"QPushButton:pressed {\n"
"    background-color: rgba(231, 76, 60, .7);\n"
"}")
        self.delete_button.setObjectName("delete_button")
        self.horizontalLayout_5.addWidget(self.delete_button)
        self.delete_stack.addWidget(self.delete_widget)
        self.horizontalLayout_4.addWidget(self.delete_stack)
        self.verticalLayout_3.addWidget(self.widget)
        self.job_library_table = QtWidgets.QTableWidget(self.job_library_table_frame)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.job_library_table.setFont(font)
        self.job_library_table.setFocusPolicy(QtCore.Qt.NoFocus)
        self.job_library_table.setStyleSheet("QTableView::item\n"
"{\n"
"    border-bottom: 1px solid;\n"
"    border-color: rgb(223, 223, 223);\n"
"    color: rgb(255, 251, 244);\n"
"}\n"
"\n"
"QTableView::item::selected\n"
"{\n"
"    border-bottom: 1px solid;\n"
"    border-color: rgb(223, 223, 223);\n"
"    background-color: rgba(85, 170, 255, .5);    \n"
"    color: rgb(255, 251, 244);\n"
"}\n"
"\n"
"QHeaderView::section\n"
"{    \n"
"    border: 0px;\n"
"    background-color: rgba(0, 0, 0, .2);\n"
"    color: rgb(255, 251, 244);\n"
"}")
        self.job_library_table.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.job_library_table.setFrameShadow(QtWidgets.QFrame.Plain)
        self.job_library_table.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.job_library_table.setAlternatingRowColors(False)
        self.job_library_table.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.job_library_table.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.job_library_table.setObjectName("job_library_table")
        self.job_library_table.setColumnCount(5)
        self.job_library_table.setRowCount(1)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(15)
        item.setFont(font)
        self.job_library_table.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(15)
        item.setFont(font)
        item.setBackground(QtGui.QColor(184, 184, 184))
        self.job_library_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(15)
        item.setFont(font)
        item.setBackground(QtGui.QColor(184, 184, 184))
        self.job_library_table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(15)
        item.setFont(font)
        item.setBackground(QtGui.QColor(184, 184, 184))
        self.job_library_table.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(15)
        item.setFont(font)
        item.setBackground(QtGui.QColor(184, 184, 184))
        self.job_library_table.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(15)
        item.setFont(font)
        item.setBackground(QtGui.QColor(184, 184, 184))
        self.job_library_table.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.job_library_table.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.job_library_table.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.job_library_table.setItem(0, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.job_library_table.setItem(0, 3, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(17)
        item.setFont(font)
        self.job_library_table.setItem(0, 4, item)
        self.job_library_table.horizontalHeader().setDefaultSectionSize(190)
        self.job_library_table.verticalHeader().setVisible(False)
        self.job_library_table.verticalHeader().setDefaultSectionSize(40)
        self.job_library_table.verticalHeader().setMinimumSectionSize(23)
        self.verticalLayout_3.addWidget(self.job_library_table)
        self.horizontalLayout_2.addWidget(self.job_library_table_frame)
        self.verticalLayout.addWidget(self.Screen)

        self.retranslateUi(JobLibraryScreen)
        self.delete_stack.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(JobLibraryScreen)

    def retranslateUi(self, JobLibraryScreen):
        _translate = QtCore.QCoreApplication.translate
        JobLibraryScreen.setWindowTitle(_translate("JobLibraryScreen", "Form"))
        self.job_header.setText(_translate("JobLibraryScreen", "Job Library"))
        self.filter_header.setText(_translate("JobLibraryScreen", "Filters"))
        self.part_number_header.setText(_translate("JobLibraryScreen", "Part Number"))
        self.part_number.setPlaceholderText(_translate("JobLibraryScreen", "Part Number"))
        self.company_header.setText(_translate("JobLibraryScreen", "Company"))
        self.company_name.setPlaceholderText(_translate("JobLibraryScreen", "Company Name"))
        self.spring_type_header.setText(_translate("JobLibraryScreen", "Spring Type"))
        self.compression_spring.setText(_translate("JobLibraryScreen", "Compression"))
        self.extension_spring.setText(_translate("JobLibraryScreen", "Extension"))
        self.scan_code_button.setText(_translate("JobLibraryScreen", "Scan Job Code"))
        self.barcode_edit.setPlaceholderText(_translate("JobLibraryScreen", "Barcode Scanned"))
        self.projects_header.setText(_translate("JobLibraryScreen", "Projects"))
        self.delete_button.setText(_translate("JobLibraryScreen", "Delete"))
        item = self.job_library_table.verticalHeaderItem(0)
        item.setText(_translate("JobLibraryScreen", "1"))
        item = self.job_library_table.horizontalHeaderItem(0)
        item.setText(_translate("JobLibraryScreen", "Part Number"))
        item = self.job_library_table.horizontalHeaderItem(1)
        item.setText(_translate("JobLibraryScreen", "Company"))
        item = self.job_library_table.horizontalHeaderItem(2)
        item.setText(_translate("JobLibraryScreen", "Spring Constant"))
        item = self.job_library_table.horizontalHeaderItem(3)
        item.setText(_translate("JobLibraryScreen", "Spring Length"))
        item = self.job_library_table.horizontalHeaderItem(4)
        item.setText(_translate("JobLibraryScreen", "Spring Type"))
        __sortingEnabled = self.job_library_table.isSortingEnabled()
        self.job_library_table.setSortingEnabled(False)
        item = self.job_library_table.item(0, 0)
        item.setText(_translate("JobLibraryScreen", "1234"))
        item = self.job_library_table.item(0, 1)
        item.setText(_translate("JobLibraryScreen", "GlennCo"))
        item = self.job_library_table.item(0, 2)
        item.setText(_translate("JobLibraryScreen", "1.1"))
        item = self.job_library_table.item(0, 3)
        item.setText(_translate("JobLibraryScreen", "1.2"))
        item = self.job_library_table.item(0, 4)
        item.setText(_translate("JobLibraryScreen", "Extension"))
        self.job_library_table.setSortingEnabled(__sortingEnabled)
from . import Spring_Serpent_Resources_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    JobLibraryScreen = QtWidgets.QWidget()
    ui = Ui_JobLibraryScreen()
    ui.setupUi(JobLibraryScreen)
    JobLibraryScreen.show()
    sys.exit(app.exec_())

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'LEVELLING1.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(816, 725)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(400, 500))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.APP_NAME = QtWidgets.QLabel(self.centralwidget)
        self.APP_NAME.setFrameShape(QtWidgets.QFrame.Box)
        self.APP_NAME.setAlignment(QtCore.Qt.AlignCenter)
        self.APP_NAME.setObjectName("APP_NAME")
        self.horizontalLayout.addWidget(self.APP_NAME)
        self.verticalLayout.addLayout(self.horizontalLayout)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setMinimumSize(QtCore.QSize(0, 0))
        self.label.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.label.setObjectName("label")
        self.horizontalLayout_4.addWidget(self.label)
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout_4.addWidget(self.lineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3, 0, QtCore.Qt.AlignHCenter)
        self.tableWidget1 = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget1.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableWidget1.sizePolicy().hasHeightForWidth())
        self.tableWidget1.setSizePolicy(sizePolicy)
        self.tableWidget1.setMinimumSize(QtCore.QSize(17, 0))
        self.tableWidget1.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.tableWidget1.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.tableWidget1.setLineWidth(9)
        self.tableWidget1.setMidLineWidth(3)
        self.tableWidget1.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContentsOnFirstShow)
        self.tableWidget1.setRowCount(1000)
        self.tableWidget1.setObjectName("tableWidget1")
        self.tableWidget1.setColumnCount(4)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setStyleStrategy(QtGui.QFont.NoAntialias)
        item.setFont(font)
        self.tableWidget1.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget1.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget1.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget1.setHorizontalHeaderItem(3, item)
        self.tableWidget1.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget1.horizontalHeader().setDefaultSectionSize(267)
        self.tableWidget1.horizontalHeader().setHighlightSections(True)
        self.tableWidget1.horizontalHeader().setMinimumSectionSize(200)
        self.tableWidget1.horizontalHeader().setStretchLastSection(False)
        self.tableWidget1.verticalHeader().setDefaultSectionSize(31)
        self.tableWidget1.verticalHeader().setMinimumSectionSize(24)
        self.tableWidget1.verticalHeader().setSortIndicatorShown(True)
        self.verticalLayout.addWidget(self.tableWidget1)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_7.addWidget(self.label_2)
        self.comboBox_2 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.horizontalLayout_7.addWidget(self.comboBox_2)
        self.verticalLayout.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setMinimumSize(QtCore.QSize(80, 0))
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout_2.addWidget(self.pushButton_4, 0, QtCore.Qt.AlignHCenter)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setMinimumSize(QtCore.QSize(80, 23))
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_2.addWidget(self.pushButton, 0, QtCore.Qt.AlignHCenter)
        self.EXPORT_WGS_POINT_TO_EXCEL_BUTTON = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.EXPORT_WGS_POINT_TO_EXCEL_BUTTON.sizePolicy().hasHeightForWidth())
        self.EXPORT_WGS_POINT_TO_EXCEL_BUTTON.setSizePolicy(sizePolicy)
        self.EXPORT_WGS_POINT_TO_EXCEL_BUTTON.setMinimumSize(QtCore.QSize(75, 23))
        self.EXPORT_WGS_POINT_TO_EXCEL_BUTTON.setObjectName("EXPORT_WGS_POINT_TO_EXCEL_BUTTON")
        self.horizontalLayout_2.addWidget(self.EXPORT_WGS_POINT_TO_EXCEL_BUTTON, 0, QtCore.Qt.AlignHCenter)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem2)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout_5.addWidget(self.pushButton_3)
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.horizontalLayout_5.addWidget(self.comboBox)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem3)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4, 0, QtCore.Qt.AlignHCenter)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem4)
        self.tableWidget_2 = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget_2.setMinimumSize(QtCore.QSize(899, 161))
        self.tableWidget_2.setRowCount(1000)
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setColumnCount(5)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(4, item)
        self.tableWidget_2.horizontalHeader().setDefaultSectionSize(197)
        self.verticalLayout.addWidget(self.tableWidget_2)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem5)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.verticalLayout.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.GHANA_NATIONAL_COODINATE_UNIT_LABEL = QtWidgets.QLabel(self.centralwidget)
        self.GHANA_NATIONAL_COODINATE_UNIT_LABEL.setFrameShape(QtWidgets.QFrame.Box)
        self.GHANA_NATIONAL_COODINATE_UNIT_LABEL.setObjectName("GHANA_NATIONAL_COODINATE_UNIT_LABEL")
        self.horizontalLayout_3.addWidget(self.GHANA_NATIONAL_COODINATE_UNIT_LABEL)
        self.GHANA_NATIONAL_UNIT_COMBOBOX = QtWidgets.QComboBox(self.centralwidget)
        self.GHANA_NATIONAL_UNIT_COMBOBOX.setObjectName("GHANA_NATIONAL_UNIT_COMBOBOX")
        self.GHANA_NATIONAL_UNIT_COMBOBOX.addItem("")
        self.GHANA_NATIONAL_UNIT_COMBOBOX.addItem("")
        self.GHANA_NATIONAL_UNIT_COMBOBOX.addItem("")
        self.GHANA_NATIONAL_UNIT_COMBOBOX.addItem("")
        self.GHANA_NATIONAL_UNIT_COMBOBOX.addItem("")
        self.GHANA_NATIONAL_UNIT_COMBOBOX.addItem("")
        self.GHANA_NATIONAL_UNIT_COMBOBOX.addItem("")
        self.GHANA_NATIONAL_UNIT_COMBOBOX.addItem("")
        self.GHANA_NATIONAL_UNIT_COMBOBOX.addItem("")
        self.GHANA_NATIONAL_UNIT_COMBOBOX.addItem("")
        self.horizontalLayout_3.addWidget(self.GHANA_NATIONAL_UNIT_COMBOBOX)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout.addWidget(self.pushButton_2, 0, QtCore.Qt.AlignHCenter)
        self.GHANA_NATIONAL_POINT_EXPORT_TO_EXCEL_BUTTON = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.GHANA_NATIONAL_POINT_EXPORT_TO_EXCEL_BUTTON.sizePolicy().hasHeightForWidth())
        self.GHANA_NATIONAL_POINT_EXPORT_TO_EXCEL_BUTTON.setSizePolicy(sizePolicy)
        self.GHANA_NATIONAL_POINT_EXPORT_TO_EXCEL_BUTTON.setObjectName("GHANA_NATIONAL_POINT_EXPORT_TO_EXCEL_BUTTON")
        self.verticalLayout.addWidget(self.GHANA_NATIONAL_POINT_EXPORT_TO_EXCEL_BUTTON, 0, QtCore.Qt.AlignHCenter)
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem6)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 816, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.APP_NAME.setText(_translate("MainWindow", "LEVEL COMPUTATION"))
        self.label.setText(_translate("MainWindow", "Initial Elevation                                                                                                             "))
        self.label_3.setText(_translate("MainWindow", "INPUT TABLE"))
        item = self.tableWidget1.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "BACKSIGHT"))
        item = self.tableWidget1.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "INTERSIGHT"))
        item = self.tableWidget1.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "FORESIGHT"))
        item = self.tableWidget1.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "REMARKS"))
        self.label_2.setText(_translate("MainWindow", "METHOD"))
        self.comboBox_2.setItemText(0, _translate("MainWindow", "HEIGHT OF COLLIMATION"))
        self.comboBox_2.setItemText(1, _translate("MainWindow", "RISE AND FALL "))
        self.pushButton_4.setText(_translate("MainWindow", "IMPORT"))
        self.pushButton.setText(_translate("MainWindow", "CLEAR TABLE"))
        self.EXPORT_WGS_POINT_TO_EXCEL_BUTTON.setText(_translate("MainWindow", "EXPORT"))
        self.pushButton_3.setText(_translate("MainWindow", "COMPUTE"))
        self.comboBox.setItemText(0, _translate("MainWindow", "HEIGT OF COLLIMATION"))
        self.comboBox.setItemText(1, _translate("MainWindow", "RISE AND FALL METHOD"))
        self.label_4.setText(_translate("MainWindow", "OUTPUT TABLE"))
        item = self.tableWidget_2.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "BACKSIGHT"))
        item = self.tableWidget_2.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "FORESIGHT"))
        item = self.tableWidget_2.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "INTERSIGHT"))
        item = self.tableWidget_2.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "REDUCED LEVEL"))
        item = self.tableWidget_2.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "REMARKS"))
        self.GHANA_NATIONAL_COODINATE_UNIT_LABEL.setText(_translate("MainWindow", "PRECISION"))
        self.GHANA_NATIONAL_UNIT_COMBOBOX.setItemText(0, _translate("MainWindow", "1"))
        self.GHANA_NATIONAL_UNIT_COMBOBOX.setItemText(1, _translate("MainWindow", "2"))
        self.GHANA_NATIONAL_UNIT_COMBOBOX.setItemText(2, _translate("MainWindow", "3"))
        self.GHANA_NATIONAL_UNIT_COMBOBOX.setItemText(3, _translate("MainWindow", "4"))
        self.GHANA_NATIONAL_UNIT_COMBOBOX.setItemText(4, _translate("MainWindow", "5"))
        self.GHANA_NATIONAL_UNIT_COMBOBOX.setItemText(5, _translate("MainWindow", "6"))
        self.GHANA_NATIONAL_UNIT_COMBOBOX.setItemText(6, _translate("MainWindow", "7"))
        self.GHANA_NATIONAL_UNIT_COMBOBOX.setItemText(7, _translate("MainWindow", "8"))
        self.GHANA_NATIONAL_UNIT_COMBOBOX.setItemText(8, _translate("MainWindow", "9"))
        self.GHANA_NATIONAL_UNIT_COMBOBOX.setItemText(9, _translate("MainWindow", "10"))
        self.pushButton_2.setText(_translate("MainWindow", "CLEAR TABLE"))
        self.GHANA_NATIONAL_POINT_EXPORT_TO_EXCEL_BUTTON.setText(_translate("MainWindow", "EXPORT TO EXCEL"))

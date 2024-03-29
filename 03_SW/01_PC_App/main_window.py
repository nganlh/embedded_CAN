# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'BTL.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(417, 486)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(417, 486))
        MainWindow.setMaximumSize(QtCore.QSize(417, 486))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 421, 531))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setObjectName("tabWidget")
        self.home_tab = QtWidgets.QWidget()
        self.home_tab.setObjectName("home_tab")
        self.connect_grbox = QtWidgets.QGroupBox(self.home_tab)
        self.connect_grbox.setGeometry(QtCore.QRect(10, 0, 391, 61))
        self.connect_grbox.setObjectName("connect_grbox")
        self.com_select = QtWidgets.QComboBox(self.connect_grbox)
        self.com_select.setGeometry(QtCore.QRect(60, 10, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setUnderline(False)
        font.setKerning(True)
        self.com_select.setFont(font)
        self.com_select.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.com_select.setCurrentText("")
        self.com_select.setObjectName("com_select")
        self.connect_button = QtWidgets.QPushButton(self.connect_grbox)
        self.connect_button.setGeometry(QtCore.QRect(260, 10, 121, 31))
        self.connect_button.setObjectName("connect_button")
        self.label = QtWidgets.QLabel(self.connect_grbox)
        self.label.setGeometry(QtCore.QRect(10, 10, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setUnderline(False)
        font.setKerning(True)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.send_button = QtWidgets.QPushButton(self.home_tab)
        self.send_button.setGeometry(QtCore.QRect(10, 390, 391, 51))
        self.send_button.setObjectName("send_button")
        self.label_6 = QtWidgets.QLabel(self.home_tab)
        self.label_6.setGeometry(QtCore.QRect(10, 350, 61, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setUnderline(False)
        font.setKerning(True)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.device_select = QtWidgets.QComboBox(self.home_tab)
        self.device_select.setGeometry(QtCore.QRect(70, 351, 141, 31))
        self.device_select.setObjectName("device_select")
        self.label_7 = QtWidgets.QLabel(self.home_tab)
        self.label_7.setGeometry(QtCore.QRect(220, 350, 61, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setUnderline(False)
        font.setKerning(True)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.status_device = QtWidgets.QLabel(self.home_tab)
        self.status_device.setGeometry(QtCore.QRect(280, 350, 121, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.status_device.sizePolicy().hasHeightForWidth())
        self.status_device.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setUnderline(False)
        font.setKerning(True)
        self.status_device.setFont(font)
        self.status_device.setText("")
        self.status_device.setObjectName("status_device")
        self.type_peripheral = QtWidgets.QTabWidget(self.home_tab)
        self.type_peripheral.setGeometry(QtCore.QRect(10, 70, 391, 271))
        self.type_peripheral.setObjectName("type_peripheral")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.green_slider = QtWidgets.QSlider(self.tab)
        self.green_slider.setGeometry(QtCore.QRect(70, 160, 231, 31))
        self.green_slider.setOrientation(QtCore.Qt.Horizontal)
        self.green_slider.setObjectName("green_slider")
        self.sample_frame = QtWidgets.QFrame(self.tab)
        self.sample_frame.setGeometry(QtCore.QRect(10, 209, 251, 31))
        font = QtGui.QFont()
        font.setUnderline(False)
        font.setKerning(True)
        self.sample_frame.setFont(font)
        self.sample_frame.setFrameShape(QtWidgets.QFrame.Panel)
        self.sample_frame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.sample_frame.setMidLineWidth(1)
        self.sample_frame.setObjectName("sample_frame")
        self.rainbow_select = QtWidgets.QRadioButton(self.tab)
        self.rainbow_select.setGeometry(QtCore.QRect(20, 20, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setUnderline(False)
        font.setKerning(True)
        self.rainbow_select.setFont(font)
        self.rainbow_select.setCheckable(True)
        self.rainbow_select.setChecked(False)
        self.rainbow_select.setObjectName("rainbow_select")
        self.label_5 = QtWidgets.QLabel(self.tab)
        self.label_5.setGeometry(QtCore.QRect(10, 160, 61, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setUnderline(False)
        font.setKerning(True)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_3 = QtWidgets.QLabel(self.tab)
        self.label_3.setGeometry(QtCore.QRect(10, 63, 61, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setUnderline(False)
        font.setKerning(True)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.blue_slider = QtWidgets.QSlider(self.tab)
        self.blue_slider.setGeometry(QtCore.QRect(70, 110, 231, 31))
        self.blue_slider.setOrientation(QtCore.Qt.Horizontal)
        self.blue_slider.setObjectName("blue_slider")
        self.label_4 = QtWidgets.QLabel(self.tab)
        self.label_4.setGeometry(QtCore.QRect(10, 110, 61, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setUnderline(False)
        font.setKerning(True)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.random_select = QtWidgets.QRadioButton(self.tab)
        self.random_select.setGeometry(QtCore.QRect(130, 20, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setUnderline(False)
        font.setKerning(True)
        self.random_select.setFont(font)
        self.random_select.setObjectName("random_select")
        self.single_select = QtWidgets.QRadioButton(self.tab)
        self.single_select.setGeometry(QtCore.QRect(260, 20, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setUnderline(False)
        font.setKerning(True)
        self.single_select.setFont(font)
        self.single_select.setObjectName("single_select")
        self.red_value = QtWidgets.QLineEdit(self.tab)
        self.red_value.setGeometry(QtCore.QRect(310, 60, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setUnderline(False)
        font.setKerning(True)
        self.red_value.setFont(font)
        self.red_value.setObjectName("red_value")
        self.green_value = QtWidgets.QLineEdit(self.tab)
        self.green_value.setGeometry(QtCore.QRect(310, 160, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setUnderline(False)
        font.setKerning(True)
        self.green_value.setFont(font)
        self.green_value.setObjectName("green_value")
        self.blue_value = QtWidgets.QLineEdit(self.tab)
        self.blue_value.setGeometry(QtCore.QRect(310, 110, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setUnderline(False)
        font.setKerning(True)
        self.blue_value.setFont(font)
        self.blue_value.setObjectName("blue_value")
        self.red_slider = QtWidgets.QSlider(self.tab)
        self.red_slider.setGeometry(QtCore.QRect(70, 60, 231, 31))
        self.red_slider.setOrientation(QtCore.Qt.Horizontal)
        self.red_slider.setObjectName("red_slider")
        self.select_color = QtWidgets.QPushButton(self.tab)
        self.select_color.setEnabled(True)
        self.select_color.setGeometry(QtCore.QRect(270, 210, 111, 31))
        font = QtGui.QFont()
        font.setUnderline(False)
        font.setKerning(True)
        self.select_color.setFont(font)
        self.select_color.setObjectName("select_color")
        self.type_peripheral.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.groupBox = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 181, 111))
        self.groupBox.setObjectName("groupBox")
        self.led1_on = QtWidgets.QRadioButton(self.groupBox)
        self.led1_on.setGeometry(QtCore.QRect(20, 30, 82, 18))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.led1_on.setFont(font)
        self.led1_on.setObjectName("led1_on")
        self.led1_off = QtWidgets.QRadioButton(self.groupBox)
        self.led1_off.setGeometry(QtCore.QRect(20, 70, 82, 18))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.led1_off.setFont(font)
        self.led1_off.setObjectName("led1_off")
        self.groupBox_2 = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox_2.setGeometry(QtCore.QRect(200, 10, 181, 111))
        self.groupBox_2.setObjectName("groupBox_2")
        self.led2_off = QtWidgets.QRadioButton(self.groupBox_2)
        self.led2_off.setGeometry(QtCore.QRect(20, 70, 82, 18))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.led2_off.setFont(font)
        self.led2_off.setObjectName("led2_off")
        self.led2_on = QtWidgets.QRadioButton(self.groupBox_2)
        self.led2_on.setGeometry(QtCore.QRect(20, 30, 82, 18))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.led2_on.setFont(font)
        self.led2_on.setObjectName("led2_on")
        self.groupBox_3 = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox_3.setGeometry(QtCore.QRect(10, 130, 181, 111))
        self.groupBox_3.setObjectName("groupBox_3")
        self.led3_off = QtWidgets.QRadioButton(self.groupBox_3)
        self.led3_off.setGeometry(QtCore.QRect(20, 70, 82, 18))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.led3_off.setFont(font)
        self.led3_off.setObjectName("led3_off")
        self.led3_on = QtWidgets.QRadioButton(self.groupBox_3)
        self.led3_on.setGeometry(QtCore.QRect(20, 30, 82, 18))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.led3_on.setFont(font)
        self.led3_on.setObjectName("led3_on")
        self.groupBox_4 = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox_4.setGeometry(QtCore.QRect(200, 130, 181, 111))
        self.groupBox_4.setObjectName("groupBox_4")
        self.led4_off = QtWidgets.QRadioButton(self.groupBox_4)
        self.led4_off.setGeometry(QtCore.QRect(20, 70, 82, 18))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.led4_off.setFont(font)
        self.led4_off.setObjectName("led4_off")
        self.led4_on = QtWidgets.QRadioButton(self.groupBox_4)
        self.led4_on.setGeometry(QtCore.QRect(20, 30, 82, 18))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.led4_on.setFont(font)
        self.led4_on.setObjectName("led4_on")
        self.type_peripheral.addTab(self.tab_2, "")
        self.tabWidget.addTab(self.home_tab, "")
        self.device_list_tab = QtWidgets.QWidget()
        self.device_list_tab.setObjectName("device_list_tab")
        self.device_table = QtWidgets.QTableWidget(self.device_list_tab)
        self.device_table.setGeometry(QtCore.QRect(10, 10, 391, 421))
        self.device_table.setObjectName("device_table")
        self.device_table.setColumnCount(6)
        self.device_table.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.device_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.device_table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.device_table.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.device_table.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.device_table.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.device_table.setHorizontalHeaderItem(5, item)
        self.tabWidget.addTab(self.device_list_tab, "")
        self.about_tab = QtWidgets.QWidget()
        self.about_tab.setObjectName("about_tab")
        self.label_2 = QtWidgets.QLabel(self.about_tab)
        self.label_2.setGeometry(QtCore.QRect(10, 10, 281, 71))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setUnderline(False)
        font.setKerning(True)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.tabWidget.addTab(self.about_tab, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        self.type_peripheral.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "LED"))
        self.connect_grbox.setTitle(_translate("MainWindow", "Connect"))
        self.connect_button.setText(_translate("MainWindow", "DISCONNECT"))
        self.label.setText(_translate("MainWindow", "COM:"))
        self.send_button.setText(_translate("MainWindow", "SEND"))
        self.label_6.setText(_translate("MainWindow", "Device"))
        self.label_7.setText(_translate("MainWindow", "Status:"))
        self.rainbow_select.setText(_translate("MainWindow", "Rainbow"))
        self.label_5.setText(_translate("MainWindow", "Green"))
        self.label_3.setText(_translate("MainWindow", "Red"))
        self.label_4.setText(_translate("MainWindow", "Blue"))
        self.random_select.setText(_translate("MainWindow", "Random"))
        self.single_select.setText(_translate("MainWindow", "Single color"))
        self.select_color.setText(_translate("MainWindow", "SELECT COLOR"))
        self.type_peripheral.setTabText(self.type_peripheral.indexOf(self.tab), _translate("MainWindow", "Neopixel"))
        self.groupBox.setTitle(_translate("MainWindow", "Led 1"))
        self.led1_on.setText(_translate("MainWindow", "On"))
        self.led1_off.setText(_translate("MainWindow", "Off"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Led 2"))
        self.led2_off.setText(_translate("MainWindow", "Off"))
        self.led2_on.setText(_translate("MainWindow", "On"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Led 3"))
        self.led3_off.setText(_translate("MainWindow", "Off"))
        self.led3_on.setText(_translate("MainWindow", "On"))
        self.groupBox_4.setTitle(_translate("MainWindow", "Led 4"))
        self.led4_off.setText(_translate("MainWindow", "Off"))
        self.led4_on.setText(_translate("MainWindow", "On"))
        self.type_peripheral.setTabText(self.type_peripheral.indexOf(self.tab_2), _translate("MainWindow", "Led built-in"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.home_tab), _translate("MainWindow", "Home"))
        item = self.device_table.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "ID"))
        item = self.device_table.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "CAN ID"))
        item = self.device_table.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Status"))
        item = self.device_table.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Button"))
        item = self.device_table.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Mode"))
        item = self.device_table.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Led"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.device_list_tab), _translate("MainWindow", "Devices"))
        self.label_2.setText(_translate("MainWindow", "GVHD: TS. Nguyễn Vĩnh Hảo\n"
"Nhóm:12"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.about_tab), _translate("MainWindow", "About"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'designer/preferences.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(665, 403)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setStatusTip("")
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.tab)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.verticalGroupBox_3 = QtWidgets.QGroupBox(self.tab)
        self.verticalGroupBox_3.setObjectName("verticalGroupBox_3")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.verticalGroupBox_3)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.horizontalLayout_31 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_31.setObjectName("horizontalLayout_31")
        self.label = QtWidgets.QLabel(self.verticalGroupBox_3)
        self.label.setObjectName("label")
        self.horizontalLayout_31.addWidget(self.label)
        self.lineEdit_5 = QtWidgets.QLineEdit(self.verticalGroupBox_3)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.horizontalLayout_31.addWidget(self.lineEdit_5)
        self.label_19 = QtWidgets.QLabel(self.verticalGroupBox_3)
        self.label_19.setObjectName("label_19")
        self.horizontalLayout_31.addWidget(self.label_19)
        self.comboBox_3 = QtWidgets.QComboBox(self.verticalGroupBox_3)
        self.comboBox_3.setEditable(False)
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.horizontalLayout_31.addWidget(self.comboBox_3)
        self.verticalLayout_7.addLayout(self.horizontalLayout_31)
        self.horizontalLayout_30 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_30.setObjectName("horizontalLayout_30")
        self.label_18 = QtWidgets.QLabel(self.verticalGroupBox_3)
        self.label_18.setObjectName("label_18")
        self.horizontalLayout_30.addWidget(self.label_18)
        self.lineEdit_6 = QtWidgets.QLineEdit(self.verticalGroupBox_3)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.horizontalLayout_30.addWidget(self.lineEdit_6)
        self.verticalLayout_7.addLayout(self.horizontalLayout_30)
        self.verticalLayout_6.addWidget(self.verticalGroupBox_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.horizontalGroupBox = QtWidgets.QGroupBox(self.tab)
        self.horizontalGroupBox.setObjectName("horizontalGroupBox")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout(self.horizontalGroupBox)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_5 = QtWidgets.QLabel(self.horizontalGroupBox)
        self.label_5.setObjectName("label_5")
        self.gridLayout_3.addWidget(self.label_5, 0, 1, 1, 1)
        self.spinBox_2 = QtWidgets.QSpinBox(self.horizontalGroupBox)
        self.spinBox_2.setMinimum(1)
        self.spinBox_2.setObjectName("spinBox_2")
        self.gridLayout_3.addWidget(self.spinBox_2, 1, 2, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.horizontalGroupBox)
        self.label_6.setObjectName("label_6")
        self.gridLayout_3.addWidget(self.label_6, 1, 1, 1, 1)
        self.spinBox_3 = QtWidgets.QSpinBox(self.horizontalGroupBox)
        self.spinBox_3.setMinimum(1)
        self.spinBox_3.setObjectName("spinBox_3")
        self.gridLayout_3.addWidget(self.spinBox_3, 2, 2, 1, 1)
        self.spinBox = QtWidgets.QSpinBox(self.horizontalGroupBox)
        self.spinBox.setMinimum(1)
        self.spinBox.setObjectName("spinBox")
        self.gridLayout_3.addWidget(self.spinBox, 0, 2, 1, 1)
        self.label_13 = QtWidgets.QLabel(self.horizontalGroupBox)
        self.label_13.setObjectName("label_13")
        self.gridLayout_3.addWidget(self.label_13, 2, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem, 0, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem1, 0, 3, 1, 1)
        self.verticalLayout_12.addLayout(self.gridLayout_3)
        self.horizontalLayout_4.addWidget(self.horizontalGroupBox)
        self.horizontalGroupBox1 = QtWidgets.QGroupBox(self.tab)
        self.horizontalGroupBox1.setObjectName("horizontalGroupBox1")
        self.verticalLayout_13 = QtWidgets.QVBoxLayout(self.horizontalGroupBox1)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.checkBox_3 = QtWidgets.QCheckBox(self.horizontalGroupBox1)
        self.checkBox_3.setObjectName("checkBox_3")
        self.horizontalLayout.addWidget(self.checkBox_3)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.verticalLayout_13.addLayout(self.horizontalLayout)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.spinBox_8 = QtWidgets.QSpinBox(self.horizontalGroupBox1)
        self.spinBox_8.setObjectName("spinBox_8")
        self.gridLayout.addWidget(self.spinBox_8, 1, 2, 1, 1)
        self.spinBox_7 = QtWidgets.QSpinBox(self.horizontalGroupBox1)
        self.spinBox_7.setObjectName("spinBox_7")
        self.gridLayout.addWidget(self.spinBox_7, 0, 2, 1, 1)
        self.label_14 = QtWidgets.QLabel(self.horizontalGroupBox1)
        self.label_14.setObjectName("label_14")
        self.gridLayout.addWidget(self.label_14, 0, 1, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem4, 0, 3, 1, 1)
        self.label_15 = QtWidgets.QLabel(self.horizontalGroupBox1)
        self.label_15.setObjectName("label_15")
        self.gridLayout.addWidget(self.label_15, 1, 1, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem5, 0, 0, 1, 1)
        self.verticalLayout_13.addLayout(self.gridLayout)
        self.horizontalLayout_4.addWidget(self.horizontalGroupBox1)
        self.verticalLayout_6.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.tab)
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout_3.addWidget(self.pushButton_4)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem6)
        self.pushButton_3 = QtWidgets.QPushButton(self.tab)
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout_3.addWidget(self.pushButton_3)
        self.pushButton = QtWidgets.QPushButton(self.tab)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_3.addWidget(self.pushButton)
        self.verticalLayout_6.addLayout(self.horizontalLayout_3)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.tab_2)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.verticalGroupBox_4 = QtWidgets.QGroupBox(self.tab_2)
        self.verticalGroupBox_4.setObjectName("verticalGroupBox_4")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.verticalGroupBox_4)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.horizontalLayout_32 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_32.setObjectName("horizontalLayout_32")
        self.label_2 = QtWidgets.QLabel(self.verticalGroupBox_4)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_32.addWidget(self.label_2)
        self.lineEdit_7 = QtWidgets.QLineEdit(self.verticalGroupBox_4)
        self.lineEdit_7.setText("")
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.horizontalLayout_32.addWidget(self.lineEdit_7)
        self.label_21 = QtWidgets.QLabel(self.verticalGroupBox_4)
        self.label_21.setObjectName("label_21")
        self.horizontalLayout_32.addWidget(self.label_21)
        self.comboBox_4 = QtWidgets.QComboBox(self.verticalGroupBox_4)
        self.comboBox_4.setEditable(False)
        self.comboBox_4.setObjectName("comboBox_4")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.horizontalLayout_32.addWidget(self.comboBox_4)
        self.verticalLayout_10.addLayout(self.horizontalLayout_32)
        self.horizontalLayout_33 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_33.setObjectName("horizontalLayout_33")
        self.label_22 = QtWidgets.QLabel(self.verticalGroupBox_4)
        self.label_22.setObjectName("label_22")
        self.horizontalLayout_33.addWidget(self.label_22)
        self.lineEdit_8 = QtWidgets.QLineEdit(self.verticalGroupBox_4)
        self.lineEdit_8.setText("")
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.horizontalLayout_33.addWidget(self.lineEdit_8)
        self.verticalLayout_10.addLayout(self.horizontalLayout_33)
        self.verticalLayout_11.addWidget(self.verticalGroupBox_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.horizontalGroupBox_2 = QtWidgets.QGroupBox(self.tab_2)
        self.horizontalGroupBox_2.setObjectName("horizontalGroupBox_2")
        self.verticalLayout_14 = QtWidgets.QVBoxLayout(self.horizontalGroupBox_2)
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.label_7 = QtWidgets.QLabel(self.horizontalGroupBox_2)
        self.label_7.setObjectName("label_7")
        self.gridLayout_4.addWidget(self.label_7, 0, 1, 1, 1)
        self.spinBox_4 = QtWidgets.QSpinBox(self.horizontalGroupBox_2)
        self.spinBox_4.setMinimum(1)
        self.spinBox_4.setObjectName("spinBox_4")
        self.gridLayout_4.addWidget(self.spinBox_4, 1, 2, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.horizontalGroupBox_2)
        self.label_8.setObjectName("label_8")
        self.gridLayout_4.addWidget(self.label_8, 1, 1, 1, 1)
        self.spinBox_5 = QtWidgets.QSpinBox(self.horizontalGroupBox_2)
        self.spinBox_5.setMinimum(1)
        self.spinBox_5.setObjectName("spinBox_5")
        self.gridLayout_4.addWidget(self.spinBox_5, 2, 2, 1, 1)
        self.spinBox_6 = QtWidgets.QSpinBox(self.horizontalGroupBox_2)
        self.spinBox_6.setMinimum(1)
        self.spinBox_6.setObjectName("spinBox_6")
        self.gridLayout_4.addWidget(self.spinBox_6, 0, 2, 1, 1)
        self.label_16 = QtWidgets.QLabel(self.horizontalGroupBox_2)
        self.label_16.setObjectName("label_16")
        self.gridLayout_4.addWidget(self.label_16, 2, 1, 1, 1)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem7, 0, 0, 1, 1)
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem8, 0, 3, 1, 1)
        self.verticalLayout_14.addLayout(self.gridLayout_4)
        self.horizontalLayout_5.addWidget(self.horizontalGroupBox_2)
        self.horizontalGroupBox_3 = QtWidgets.QGroupBox(self.tab_2)
        self.horizontalGroupBox_3.setObjectName("horizontalGroupBox_3")
        self.verticalLayout_15 = QtWidgets.QVBoxLayout(self.horizontalGroupBox_3)
        self.verticalLayout_15.setObjectName("verticalLayout_15")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem9)
        self.checkBox_4 = QtWidgets.QCheckBox(self.horizontalGroupBox_3)
        self.checkBox_4.setObjectName("checkBox_4")
        self.horizontalLayout_2.addWidget(self.checkBox_4)
        spacerItem10 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem10)
        self.verticalLayout_15.addLayout(self.horizontalLayout_2)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.spinBox_9 = QtWidgets.QSpinBox(self.horizontalGroupBox_3)
        self.spinBox_9.setObjectName("spinBox_9")
        self.gridLayout_2.addWidget(self.spinBox_9, 1, 2, 1, 1)
        self.spinBox_10 = QtWidgets.QSpinBox(self.horizontalGroupBox_3)
        self.spinBox_10.setObjectName("spinBox_10")
        self.gridLayout_2.addWidget(self.spinBox_10, 0, 2, 1, 1)
        self.label_17 = QtWidgets.QLabel(self.horizontalGroupBox_3)
        self.label_17.setObjectName("label_17")
        self.gridLayout_2.addWidget(self.label_17, 0, 1, 1, 1)
        spacerItem11 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem11, 0, 3, 1, 1)
        self.label_20 = QtWidgets.QLabel(self.horizontalGroupBox_3)
        self.label_20.setObjectName("label_20")
        self.gridLayout_2.addWidget(self.label_20, 1, 1, 1, 1)
        spacerItem12 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem12, 0, 0, 1, 1)
        self.verticalLayout_15.addLayout(self.gridLayout_2)
        self.horizontalLayout_5.addWidget(self.horizontalGroupBox_3)
        self.verticalLayout_11.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.pushButton_6 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_6.setObjectName("pushButton_6")
        self.horizontalLayout_6.addWidget(self.pushButton_6)
        spacerItem13 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem13)
        self.pushButton_5 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_5.setObjectName("pushButton_5")
        self.horizontalLayout_6.addWidget(self.pushButton_5)
        self.pushButton_2 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_6.addWidget(self.pushButton_2)
        self.verticalLayout_11.addLayout(self.horizontalLayout_6)
        self.tabWidget.addTab(self.tab_2, "")
        self.verticalLayout.addWidget(self.tabWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.lineEdit_5, self.comboBox_3)
        MainWindow.setTabOrder(self.comboBox_3, self.lineEdit_6)
        MainWindow.setTabOrder(self.lineEdit_6, self.spinBox)
        MainWindow.setTabOrder(self.spinBox, self.spinBox_2)
        MainWindow.setTabOrder(self.spinBox_2, self.spinBox_3)
        MainWindow.setTabOrder(self.spinBox_3, self.checkBox_3)
        MainWindow.setTabOrder(self.checkBox_3, self.spinBox_7)
        MainWindow.setTabOrder(self.spinBox_7, self.spinBox_8)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.verticalGroupBox_3.setTitle(_translate("MainWindow", "Connection settings"))
        self.label.setText(_translate("MainWindow", "Nickname:"))
        self.lineEdit_5.setText(_translate("MainWindow", "Anonymous"))
        self.label_19.setText(_translate("MainWindow", "Connection mode:"))
        self.comboBox_3.setItemText(0, _translate("MainWindow", "Clearnet"))
        self.comboBox_3.setItemText(1, _translate("MainWindow", "Tor"))
        self.comboBox_3.setItemText(2, _translate("MainWindow", "I2P"))
        self.label_18.setText(_translate("MainWindow", "Introducer:"))
        self.lineEdit_6.setText(_translate("MainWindow", "pb://hckqqn4vq5ggzuukfztpuu4wykwefa6d@publictestgrid.twilightparadox.com:50213,publictestgrid.lukas-pirl.de:50213,publictestgrid.e271.net:50213,198.186.193.74:50213,68.34.102.231:50213/introducer"))
        self.horizontalGroupBox.setTitle(_translate("MainWindow", "Storage parameters"))
        self.label_5.setText(_translate("MainWindow", "Total shares (N):"))
        self.label_6.setText(_translate("MainWindow", "Needed shares (K):"))
        self.label_13.setText(_translate("MainWindow", "Servers of happiness (H):"))
        self.horizontalGroupBox1.setTitle(_translate("MainWindow", "Drive sharing"))
        self.checkBox_3.setText(_translate("MainWindow", "Share this computer\'s free space"))
        self.label_14.setText(_translate("MainWindow", "Size limit (GB)"))
        self.label_15.setText(_translate("MainWindow", "Time limit (days):"))
        self.pushButton_4.setStatusTip(_translate("MainWindow", "Share this grid with a friend..."))
        self.pushButton_4.setText(_translate("MainWindow", "Share..."))
        self.pushButton_3.setStatusTip(_translate("MainWindow", "Close without saving changes."))
        self.pushButton_3.setText(_translate("MainWindow", "Cancel"))
        self.pushButton.setStatusTip(_translate("MainWindow", "Save settings and reload."))
        self.pushButton.setText(_translate("MainWindow", "Apply"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Public Test Grid"))
        self.verticalGroupBox_4.setTitle(_translate("MainWindow", "Connection settings"))
        self.label_2.setText(_translate("MainWindow", "Nickname:"))
        self.label_21.setText(_translate("MainWindow", "Connection mode:"))
        self.comboBox_4.setItemText(0, _translate("MainWindow", "Clearnet"))
        self.comboBox_4.setItemText(1, _translate("MainWindow", "Tor"))
        self.comboBox_4.setItemText(2, _translate("MainWindow", "I2P"))
        self.label_22.setText(_translate("MainWindow", "Introducer:"))
        self.horizontalGroupBox_2.setTitle(_translate("MainWindow", "Storage parameters"))
        self.label_7.setText(_translate("MainWindow", "Total shares (N):"))
        self.label_8.setText(_translate("MainWindow", "Needed shares (K):"))
        self.label_16.setText(_translate("MainWindow", "Servers of happiness (H):"))
        self.horizontalGroupBox_3.setTitle(_translate("MainWindow", "Drive sharing"))
        self.checkBox_4.setText(_translate("MainWindow", "Share this computer\'s free space"))
        self.label_17.setText(_translate("MainWindow", "Size limit (GB)"))
        self.label_20.setText(_translate("MainWindow", "Time limit (days):"))
        self.pushButton_6.setText(_translate("MainWindow", "Share..."))
        self.pushButton_5.setText(_translate("MainWindow", "Cancel"))
        self.pushButton_2.setText(_translate("MainWindow", "Apply"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "+"))


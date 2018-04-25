# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_window.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.main_widget = QtWidgets.QWidget(self.centralwidget)
        self.main_widget.setGeometry(QtCore.QRect(0, 20, 811, 581))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.main_widget.sizePolicy().hasHeightForWidth())
        self.main_widget.setSizePolicy(sizePolicy)
        self.main_widget.setObjectName("main_widget")
        self.Table = QtWidgets.QTableWidget(self.main_widget)
        self.Table.setGeometry(QtCore.QRect(30, 40, 591, 341))
        self.Table.setStyleSheet("")
        self.Table.setObjectName("Table")
        self.Table.setColumnCount(0)
        self.Table.setRowCount(0)
        self.Button = QtWidgets.QPushButton(self.main_widget)
        self.Button.setGeometry(QtCore.QRect(700, 10, 99, 27))
        self.Button.setObjectName("Button")
        self.comboBox = QtWidgets.QComboBox(self.main_widget)
        self.comboBox.setGeometry(QtCore.QRect(660, 90, 85, 27))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 25))
        self.menubar.setObjectName("menubar")
        self.menuTables = QtWidgets.QMenu(self.menubar)
        self.menuTables.setObjectName("menuTables")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionShare = QtWidgets.QAction(MainWindow)
        self.actionShare.setObjectName("actionShare")
        self.actionRegion = QtWidgets.QAction(MainWindow)
        self.actionRegion.setObjectName("actionRegion")
        self.menuTables.addAction(self.actionShare)
        self.menuTables.addAction(self.actionRegion)
        self.menubar.addAction(self.menuTables.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Button.setText(_translate("MainWindow", "Tap, please"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Share"))
        self.comboBox.setItemText(1, _translate("MainWindow", "Region"))
        self.comboBox.setItemText(2, _translate("MainWindow", "User"))
        self.menuTables.setTitle(_translate("MainWindow", "Tables"))
        self.actionShare.setText(_translate("MainWindow", "Share"))
        self.actionRegion.setText(_translate("MainWindow", "Region"))


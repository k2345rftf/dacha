# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
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
        self.formLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.formLayoutWidget.setGeometry(QtCore.QRect(160, 180, 341, 158))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setObjectName("formLayout")
        self.login = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.login.setObjectName("login")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.login)
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.formLayoutWidget)
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.plainTextEdit)
        self.password = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.password.setObjectName("password")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.password)
        self.plainTextEdit_2 = QtWidgets.QPlainTextEdit(self.formLayoutWidget)
        self.plainTextEdit_2.setObjectName("plainTextEdit_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.plainTextEdit_2)
        self.sign_in = QtWidgets.QPushButton(self.centralwidget)
        self.sign_in.setGeometry(QtCore.QRect(300, 340, 99, 27))
        self.sign_in.setObjectName("sign_in")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 25))
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
        self.plainTextEdit.setPlainText(_translate("MainWindow", "Введите логин"))
        self.plainTextEdit_2.setPlainText(_translate("MainWindow", "Введите пароль"))
        self.sign_in.setText(_translate("MainWindow", "sign in"))


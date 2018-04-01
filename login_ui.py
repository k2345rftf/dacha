# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Login(object):
    def setupUi(self, Login):
        Login.setObjectName("Login")
        Login.resize(400, 337)
        self.formLayoutWidget = QtWidgets.QWidget(Login)
        self.formLayoutWidget.setGeometry(QtCore.QRect(30, 70, 341, 71))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setObjectName("formLayout")
        self.login = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.login.setObjectName("login")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.login)
        self.password = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.password.setObjectName("password")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.password)
        self.plainTextEdit_2 = QtWidgets.QPlainTextEdit(self.formLayoutWidget)
        self.plainTextEdit_2.setObjectName("plainTextEdit_2")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.plainTextEdit_2)
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.formLayoutWidget)
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.plainTextEdit)
        self.sign_in = QtWidgets.QPushButton(Login)
        self.sign_in.setGeometry(QtCore.QRect(150, 150, 99, 27))
        self.sign_in.setObjectName("sign_in")

        self.retranslateUi(Login)
        QtCore.QMetaObject.connectSlotsByName(Login)

    def retranslateUi(self, Login):
        _translate = QtCore.QCoreApplication.translate
        Login.setWindowTitle(_translate("Login", "Form"))
        self.plainTextEdit_2.setPlainText(_translate("Login", "Введите пароль"))
        self.plainTextEdit.setPlainText(_translate("Login", "Введите логин"))
        self.sign_in.setText(_translate("Login", "sign in"))


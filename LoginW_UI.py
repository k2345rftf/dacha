# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Login_widget.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Login_ui(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(443, 300)
        self.password = QtWidgets.QLineEdit(Form)
        self.password.setGeometry(QtCore.QRect(50, 140, 281, 27))
        self.password.setObjectName("password")
        self.login = QtWidgets.QLineEdit(Form)
        self.login.setGeometry(QtCore.QRect(50, 70, 281, 27))
        self.login.setObjectName("login")
        self.loginLable = QtWidgets.QLabel(Form)
        self.loginLable.setGeometry(QtCore.QRect(50, 40, 151, 17))
        self.loginLable.setObjectName("loginLable")
        self.passwordLable = QtWidgets.QLabel(Form)
        self.passwordLable.setGeometry(QtCore.QRect(50, 110, 151, 17))
        self.passwordLable.setObjectName("passwordLable")
        self.sign_in = QtWidgets.QPushButton(Form)
        self.sign_in.setGeometry(QtCore.QRect(50, 210, 99, 27))
        self.sign_in.setObjectName("sign_in")
        self.error = QtWidgets.QLabel(Form)
        self.error.setGeometry(QtCore.QRect(60, 180, 251, 17))
        self.error.setText("")
        self.error.setObjectName("error")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "СНТ-Веселое"))
        self.loginLable.setText(_translate("Form", "Введите логин"))
        self.passwordLable.setText(_translate("Form", "Введите пароль"))
        self.sign_in.setText(_translate("Form", "Войти"))


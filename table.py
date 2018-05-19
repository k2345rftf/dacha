# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Table.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!
from PyQt5 import QtCore, QtGui, QtWidgets


class Table(object):
    def setupUi(self, Form):
        
        Form.setObjectName("Form")
        Form.resize(711, 492)
        self.TableView = QtWidgets.QTableWidget(Form)
        self.TableView.setGeometry(QtCore.QRect(0, 40, 711, 451))
        self.TableView.setObjectName("TableView")
        self.TableView.setColumnCount(0)
        self.TableView.setRowCount(0)
        self.choose = QtWidgets.QComboBox(Form)
        self.choose.setGeometry(QtCore.QRect(10, 10, 181, 27))
        self.choose.setObjectName("choose")
        self.enter = QtWidgets.QPushButton(Form)
        self.enter.setGeometry(QtCore.QRect(530, 10, 99, 27))
        self.enter.setObjectName("enter")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.enter.setText(_translate("Form", "Показать"))


# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'setCounter.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class SetCounter(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(30, 240, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.classAccur = QtWidgets.QDoubleSpinBox(Dialog)
        self.classAccur.setGeometry(QtCore.QRect(70, 150, 271, 27))
        self.classAccur.setDecimals(6)
        self.classAccur.setMinimum(0.0)
        self.classAccur.setMaximum(0.999999)
        self.classAccur.setSingleStep(1e-06)
        self.classAccur.setObjectName("classAccur")
        self.typeCounter = QtWidgets.QLineEdit(Dialog)
        self.typeCounter.setGeometry(QtCore.QRect(70, 70, 271, 27))
        self.typeCounter.setObjectName("typeCounter")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(70, 30, 301, 17))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(70, 120, 281, 20))
        self.label_2.setObjectName("label_2")

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Добавление счетчика"))
        self.label.setText(_translate("Dialog", "Введите тип счетчика(за какую услугу)"))
        self.label_2.setText(_translate("Dialog", "Введите класс точности"))


# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'index.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(388, 183)
        self.GirisYap = QtWidgets.QPushButton(Form)
        self.GirisYap.setGeometry(QtCore.QRect(120, 120, 241, 31))
        self.GirisYap.setObjectName("GirisYap")
        self.layoutWidget = QtWidgets.QWidget(Form)
        self.layoutWidget.setGeometry(QtCore.QRect(60, 40, 301, 71))
        self.layoutWidget.setObjectName("layoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.layoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.leUsername = QtWidgets.QLineEdit(self.layoutWidget)
        self.leUsername.setStyleSheet("font: 75 10pt \"MS Shell Dlg 2\";")
        self.leUsername.setObjectName("leUsername")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.leUsername)
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.lePassword = QtWidgets.QLineEdit(self.layoutWidget)
        self.lePassword.setStyleSheet("font: 75 10pt \"MS Shell Dlg 2\";")
        self.lePassword.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lePassword.setObjectName("lePassword")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lePassword)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.GirisYap.setText(_translate("Form", "Giriş Yap"))
        self.label.setText(_translate("Form", "Username"))
        self.label_2.setText(_translate("Form", "Password"))
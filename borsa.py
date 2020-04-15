# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'borsa.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import requests
import sys


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(456, 362)
        self.horizontalLayoutWidget = QtWidgets.QWidget(Form)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 270, 441, 81))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.pushButton_2 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(30, 30, 71, 31))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(30, 70, 71, 41))
        self.label_2.setObjectName("label_2")
        self.comboBox = QtWidgets.QComboBox(Form)
        self.comboBox.setGeometry(QtCore.QRect(110, 40, 141, 22))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox_2 = QtWidgets.QComboBox(Form)
        self.comboBox_2.setGeometry(QtCore.QRect(110, 80, 141, 22))
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(30, 200, 221, 51))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(30, 120, 71, 21))
        self.label_4.setObjectName("label_4")
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(110, 120, 131, 21))
        self.lineEdit.setObjectName("lineEdit")

        self.retranslateUi(Form)
        self.url = "https://api.exchangeratesapi.io/latest?base="
        self.pushButton_2.clicked.connect(self.click)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton_2.setText(_translate("Form", "Çevir"))
        self.label.setText(_translate("Form", "1. Para birimi:"))
        self.label_2.setText(_translate("Form", "2. Para Birimi:"))
        self.comboBox.setItemText(0, _translate("Form", "TRY"))
        self.comboBox.setItemText(1, _translate("Form", "CAD"))
        self.comboBox.setItemText(2, _translate("Form", "USD"))
        self.comboBox.setItemText(3, _translate("Form", "EUR"))
        self.comboBox.setItemText(4, _translate("Form", "RUB"))
        self.comboBox_2.setItemText(0, _translate("Form", "TRY"))
        self.comboBox_2.setItemText(1, _translate("Form", "CAD"))
        self.comboBox_2.setItemText(2, _translate("Form", "USD"))
        self.comboBox_2.setItemText(3, _translate("Form", "EUR"))
        self.comboBox_2.setItemText(4, _translate("Form", "RUB"))
        self.label_3.setText(_translate("Form", "Çevirmek istediğiniz birimleri seçiniz."))
        self.label_4.setText(_translate("Form", "Miktar:"))

    def click(self):
        a = self.comboBox.currentText()
        b = self.comboBox_2.currentText()
        response = requests.get(self.url + a)
        json_verisi = response.json()
        miktar = float(self.lineEdit.text())
        sonuc = str(json_verisi["rates"][b] * miktar)
        self.label_3.setText(sonuc)
        print(sonuc)
        

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())


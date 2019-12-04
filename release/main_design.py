# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Design_main(object):
    def setupUi(self, main):
        main.setObjectName("main")
        main.resize(770, 361)
        self.CoffeeTable = QtWidgets.QTableWidget(main)
        self.CoffeeTable.setGeometry(QtCore.QRect(10, 10, 751, 281))
        self.CoffeeTable.setObjectName("CoffeeTable")
        self.CoffeeTable.setColumnCount(0)
        self.CoffeeTable.setRowCount(0)
        self.pushButton = QtWidgets.QPushButton(main)
        self.pushButton.setGeometry(QtCore.QRect(10, 300, 751, 51))
        self.pushButton.setStyleSheet("font: 24pt \"Calibri\";")
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(main)
        QtCore.QMetaObject.connectSlotsByName(main)

    def retranslateUi(self, main):
        _translate = QtCore.QCoreApplication.translate
        main.setWindowTitle(_translate("main", "Form"))
        self.pushButton.setText(_translate("main", "Добавить сорт кофе."))

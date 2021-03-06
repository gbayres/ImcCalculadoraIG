# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'imcdesign2.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets



class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(306, 311)
        MainWindow.setStyleSheet("")
        self.label = QtWidgets.QLabel(MainWindow)
        self.label.setGeometry(QtCore.QRect(100, 10, 111, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(MainWindow)
        self.label_2.setGeometry(QtCore.QRect(70, 130, 47, 13))
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(MainWindow)
        self.lineEdit.setGeometry(QtCore.QRect(70, 160, 51, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.label_3 = QtWidgets.QLabel(MainWindow)
        self.label_3.setGeometry(QtCore.QRect(180, 130, 47, 13))
        self.label_3.setObjectName("label_3")
        self.lineEdit_2 = QtWidgets.QLineEdit(MainWindow)
        self.lineEdit_2.setGeometry(QtCore.QRect(180, 160, 51, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton = QtWidgets.QPushButton(MainWindow)
        self.pushButton.setGeometry(QtCore.QRect(120, 200, 75, 23))
        self.pushButton.clicked.connect(self.calculo)
        self.pushButton.setObjectName("pushButton")
        self.label_4 = QtWidgets.QLabel(MainWindow)
        self.label_4.setGeometry(QtCore.QRect(50, 250, 211, 20))
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(MainWindow)
        self.label_5.setGeometry(QtCore.QRect(70, 60, 61, 16))
        self.label_5.setObjectName("label_5")
        self.lineEdit_3 = QtWidgets.QLineEdit(MainWindow)
        self.lineEdit_3.setGeometry(QtCore.QRect(70, 90, 51, 20))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(MainWindow)
        self.lineEdit_4.setGeometry(QtCore.QRect(180, 90, 51, 20))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.label_6 = QtWidgets.QLabel(MainWindow)
        self.label_6.setGeometry(QtCore.QRect(190, 60, 47, 13))
        self.label_6.setObjectName("label_6")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def calculo(self):

        self.peso = float(self.lineEdit.text())
        self.altura = float(self.lineEdit_2.text())
        self.gen = str(self.lineEdit_3.text()).upper()
        self.idade = int(self.lineEdit_4.text())
        self.imcval = self.peso / (self.altura * self.altura)

        if self.gen == "M":
            if self.idade == 1:
                if self.imcval > 19.6:
                    self.label_4.setText(str(f"O seu IMC é {self.imcval:.2f} e tem obesidade"))
                elif self.imcval >= 18.2:
                    self.label_4.setText(str(f"O seu IMC é {self.imcval:.2f} e tem sobrepeso"))
                elif self.imcval >= 14.5:
                    self.label_4.setText(str(f"O seu IMC é {self.imcval:.2f} e tem um peso normal"))
                else:
                    self.label_4.setText(str(f"O seu IMC é {self.imcval:.2f} e tem um peso abaixo do normal"))
            if self.idade == 2:
                if self.imcval > 18.7:
                    self.label_4.setText(str(f"O seu IMC é {self.imcval:.2f} e tem obesidade"))
                elif self.imcval >= 17.4:
                    self.label_4.setText(str(f"O seu IMC é {self.imcval:.2f} e tem sobrepeso"))
                elif self.imcval >= 14:
                    self.label_4.setText(str(f"O seu IMC é {self.imcval:.2f} e tem um peso normal"))
                else:
                    self.label_4.setText(str(f"O seu IMC é {self.imcval:.2f} e tem um peso abaixo do normal"))
            if self.idade == 3:
                if self.imcval > 18.2:
                    self.label_4.setText(str(f"O seu IMC é {self.imcval:.2f} e tem obesidade"))
                elif self.imcval >= 17:
                    self.label_4.setText(str(f"O seu IMC é {self.imcval:.2f} e tem sobrepeso"))
                elif self.imcval >= 13.4:
                    self.label_4.setText(str(f"O seu IMC é {self.imcval:.2f} e tem um peso normal"))
                else:
                    self.label_4.setText(str(f"O seu IMC é {self.imcval:.2f} e tem um peso abaixo do normal"))
            if self.idade == 4:
                if self.imcval > 18:
                    self.label_4.setText(str(f"O seu IMC é {self.imcval:.2f} e tem obesidade"))
                elif self.imcval >= 16.7:
                    self.label_4.setText(str(f"O seu IMC é {self.imcval:.2f} e tem sobrepeso"))
                elif self.imcval >= 13.2:
                    self.label_4.setText(str(f"O seu IMC é {self.imcval:.2f} e tem um peso normal"))
                else:
                    self.label_4.setText(str(f"O seu IMC é {self.imcval:.2f} e tem um peso abaixo do normal"))
            if self.idade == 5:
                if self.imcval > 18.1:
                    self.label_4.setText(str(f"O seu IMC é {self.imcval:.2f} e tem obesidade"))
                elif self.imcval >= 16.7:
                    self.label_4.setText(str(f"O seu IMC é {self.imcval:.2f} e tem sobrepeso"))
                elif self.imcval >= 13:
                    self.label_4.setText(str(f"O seu IMC é {self.imcval:.2f} e tem um peso normal"))
                else:
                    self.label_4.setText(str(f"O seu IMC é {self.imcval:.2f} e tem um peso abaixo do normal"))
            if self.idade == 6:
                if self.imcval > 18.4:
                    self.label_4.setText(str(f"O seu IMC é {self.imcval:.2f} e tem obesidade"))
                elif self.imcval >= 16.9:
                    self.label_4.setText(str(f"O seu IMC é {self.imcval:.2f} e tem sobrepeso"))
                elif self.imcval >= 13.2:
                    self.label_4.setText(str(f"O seu IMC é {self.imcval:.2f} e tem um peso normal"))
                else:
                    self.label_4.setText(str(f"O seu IMC é {self.imcval:.2f} e tem um peso abaixo do normal"))
            if self.idade == 7:
                if self.imcval > 18.7:
                    self.label_4.setText(str(f"O seu IMC é {self.imcval:.2f} e tem obesidade"))
                elif self.imcval >= 17.2:
                    self.label_4.setText(str(f"O seu IMC é {self.imcval:.2f} e tem sobrepeso"))
                elif self.imcval >= 13.3:
                    self.label_4.setText(str(f"O seu IMC é {self.imcval:.2f} e tem um peso normal"))
                else:
                    self.label_4.setText(str(f"O seu IMC é {self.imcval:.2f} e tem um peso abaixo do normal"))
            if self.idade == 8:
                if self.imcval > 19.4:
                    self.label_4.setText(str(f"O seu IMC é {self.imcval:.2f} e tem obesidade"))
                elif self.imcval >= 17.5:
                    self.label_4.setText(str(f"O seu IMC é {self.imcval:.2f} e tem sobrepeso"))
                elif self.imcval >= 13.5:
                    self.label_4.setText(str(f"O seu IMC é {self.imcval:.2f} e tem um peso normal"))
                else:
                    self.label_4.setText(str(f"O seu IMC é {self.imcval:.2f} e tem um peso abaixo do normal"))
            if self.idade == 9:
                if self.imcval > 20.1:
                    self.label_4.setText(str(f"O seu IMC é {self.imcval:.2f} e tem obesidade"))
                elif self.imcval >= 18:
                    self.label_4.setText(str(f"O seu IMC é {self.imcval:.2f} e tem sobrepeso"))
                elif self.imcval >= 13.6:
                    self.label_4.setText(str(f"O seu IMC é {self.imcval:.2f} e tem um peso normal"))
                else:
                    self.label_4.setText(str(f"O seu IMC é {self.imcval:.2f} e tem um peso abaixo do normal"))
            if self.idade == 10:
                if self.imcval > 28.6:
                    self.label_4.setText(str(f"O seu IMC é {self.imcval:.2f} e tem obesidade"))
                elif self.imcval >= 25:
                    self.label_4.setText(str(f"O seu IMC é {self.imcval:.2f} e tem sobrepeso"))
                elif self.imcval >= 17.5:
                    self.label_4.setText(str(f"O seu IMC é {self.imcval:.2f} e tem um peso normal"))
                else:
                    self.label_4.setText(str(f"O seu IMC é {self.imcval:.2f} e tem um peso abaixo do normal"))
            if self.idade == 11:
                if self.imcval > 22:
                    self.label_4.setText(str(f"O seu IMC é {self.imcval:.2f} e tem obesidade"))
                elif self.imcval >= 19.3:
                    self.label_4.setText(str(f"O seu IMC é {self.imcval:.2f} e tem sobrepeso"))
                elif self.imcval >= 14.2:
                    self.label_4.setText(str(f"O seu IMC é {self.imcval:.2f} e tem um peso normal"))
                else:
                    self.label_4.setText(str(f"O seu IMC é {self.imcval:.2f} e tem um peso abaixo do normal"))
            if self.idade == 12:
                if self.imcval > 23:
                    self.label_4.setText(str(f"O seu IMC é {self.imcval:.2f} e tem obesidade"))
                elif self.imcval >= 20:
                    self.label_4.setText(str(f"O seu IMC é {self.imcval:.2f} e tem sobrepeso"))
                elif self.imcval >= 14.6:
                    self.label_4.setText(str(f"O seu IMC é {self.imcval:.2f} e tem um peso normal"))
                else:
                    self.label_4.setText(str(f"O seu IMC é {self.imcval:.2f} e tem um peso abaixo do normal"))
            if self.idade == 13:
                if self.imcval > 24.2:
                    self.label_4.setText(str(f"O seu IMC é {self.imcval:.2f} e tem obesidade"))
                elif self.imcval >= 21:
                    self.label_4.setText(str(f"O seu IMC é {self.imcval:.2f} e tem sobrepeso"))
                elif self.imcval >= 15:
                    self.label_4.setText(str(f"O seu IMC é {self.imcval:.2f} e tem um peso normal"))
                else:
                    self.label_4.setText(str(f"O seu IMC é {self.imcval:.2f} e tem um peso abaixo do normal"))
            if self.idade == 14:
                if self.imcval > 25.3:
                    self.label_4.setText(str(f"O seu IMC é {self.imcval:.2f} e tem obesidade"))
                elif self.imcval >= 21.9:
                    self.label_4.setText(str(f"O seu IMC é {self.imcval:.2f} e tem sobrepeso"))
                elif self.imcval >= 15.6:
                    self.label_4.setText(str(f"O seu IMC é {self.imcval:.2f} e tem um peso normal"))
                else:
                    self.label_4.setText(str(f"O seu IMC é {self.imcval:.2f} e tem um peso abaixo do normal"))
            if self.idade == 15:
                if self.imcval > 26.4:
                    self.label_4.setText(str(f"O seu IMC é {self.imcval:.2f} e tem obesidade"))
                elif self.imcval >= 22.8:
                    self.label_4.setText(str(f"O seu IMC é {self.imcval:.2f} e tem sobrepeso"))
                elif self.imcval >= 16.2:
                    self.label_4.setText(str(f"O seu IMC é {self.imcval:.2f} e tem um peso normal"))
                else:
                    self.label_4.setText(str(f"O seu IMC é {self.imcval:.2f} e tem um peso abaixo do normal"))
            if self.idade == 16:
                if self.imcval > 27.3:
                    self.label_4.setText(str(f"O seu IMC é {self.imcval:.2f} e tem obesidade"))
                elif self.imcval >= 23.7:
                    self.label_4.setText(str(f"O seu IMC é {self.imcval:.2f} e tem sobrepeso"))
                elif self.imcval >= 16.7:
                    self.label_4.setText(str(f"O seu IMC é {self.imcval:.2f} e tem um peso normal"))
                else:
                    self.label_4.setText(str(f"O seu IMC é {self.imcval:.2f} e tem um peso abaixo do normal"))
            if self.idade == 17:
                if self.imcval > 28:
                    self.label_4.setText(str(f"O seu IMC é {self.imcval:.2f} e tem obesidade"))
                elif self.imcval >= 24.5:
                    self.label_4.setText(str(f"O seu IMC é {self.imcval:.2f} e tem sobrepeso"))
                elif self.imcval >= 17.2:
                    self.label_4.setText(str(f"O seu IMC é {self.imcval:.2f} e tem um peso normal"))
                else:
                    self.label_4.setText(str(f"O seu IMC é {self.imcval:.2f} e tem um peso abaixo do normal"))
            if self.idade == 18:
                if self.imcval > 28.6:
                    self.label_4.setText(str(f"O seu IMC é {self.imcval:.2f} e tem obesidade"))
                elif self.imcval >= 25:
                    self.label_4.setText(str(f"O seu IMC é {self.imcval:.2f} e tem sobrepeso"))
                elif self.imcval >= 17.5:
                    self.label_4.setText(str(f"O seu IMC é {self.imcval:.2f} e tem um peso normal"))
                else:
                    self.label_4.setText(str(f"O seu IMC é {self.imcval:.2f} e tem um peso abaixo do normal"))
            if self.idade >= 19:
                if self.imcval > 30:
                    self.label_4.setText(str(f"O seu IMC é {self.imcval:.2f} e tem obesidade"))
                elif self.imcval >= 25:
                    self.label_4.setText(str(f"O seu IMC é {self.imcval:.2f} e tem sobrepeso"))
                elif self.imcval >= 18.5:
                    self.label_4.setText(str(f"O seu IMC é {self.imcval:.2f} e tem um peso normal"))
                else:
                    self.label_4.setText(str(f"O seu IMC é {self.imcval:.2f} e tem um peso abaixo do normal"))


        if self.gen == "F":
            if self.idade == 1:
                if self.imcval > 19.4:
                    self.label_4.setText(str(f"O seu IMC é {self.imcval:.2f} e tem obesidade"))
                elif self.imcval >= 17.9:
                    self.label_4.setText(str(f"O seu IMC é {self.imcval:.2f} e tem sobrepeso"))
                elif self.imcval >= 13.9:
                    self.label_4.setText(str(f"O seu IMC é {self.imcval:.2f} e tem um peso normal"))
                else:
                    self.label_4.setText(str(f"O seu IMC é {self.imcval:.2f} e tem um peso abaixo do normal"))
            if self.idade == 2:
                if self.imcval > 18.5:
                    self.label_4.setText(str(f"O seu IMC é {self.imcval:.2f} e tem obesidade"))
                elif self.imcval >= 17.2:
                    self.label_4.setText(str(f"O seu IMC é {self.imcval:.2f} e tem sobrepeso"))
                elif self.imcval >= 13.5:
                    self.label_4.setText(str(f"O seu IMC é {self.imcval:.2f} e tem um peso normal"))
                else:
                    self.label_4.setText(str(f"O seu IMC é {self.imcval:.2f} e tem um peso abaixo do normal"))
            if self.idade == 3:
                if self.imcval > 18.2:
                    self.label_4.setText(str(f"O seu IMC é {self.imcval:.2f} e tem obesidade"))
                elif self.imcval >= 16.8:
                    self.label_4.setText(str(f"O seu IMC é {self.imcval:.2f} e tem sobrepeso"))
                elif self.imcval >= 13.2:
                    self.label_4.setText(str(f"O seu IMC é {self.imcval:.2f} e tem um peso normal"))
                else:
                    self.label_4.setText(str(f"O seu IMC é {self.imcval:.2f} e tem um peso abaixo do normal"))
            if self.idade == 4:
                if self.imcval > 18.3:
                    self.label_4.setText(str(f"O seu IMC é {self.imcval:.2f} e tem obesidade"))
                elif self.imcval >= 16.8:
                    self.label_4.setText(str(f"O seu IMC é {self.imcval:.2f} e tem sobrepeso"))
                elif self.imcval >= 13:
                    self.label_4.setText(str(f"O seu IMC é {self.imcval:.2f} e tem um peso normal"))
                else:
                    self.label_4.setText(str(f"O seu IMC é {self.imcval:.2f} e tem um peso abaixo do normal"))
            if self.idade == 5:
                if self.imcval > 18.6:
                    self.label_4.setText(str(f"O seu IMC é {self.imcval:.2f} e tem obesidade"))
                elif self.imcval >= 17:
                    self.label_4.setText(str(f"O seu IMC é {self.imcval:.2f} e tem sobrepeso"))
                elif self.imcval >= 12.8:
                    self.label_4.setText(str(f"O seu IMC é {self.imcval:.2f} e tem um peso normal"))
                else:
                    self.label_4.setText(str(f"O seu IMC é {self.imcval:.2f} e tem um peso abaixo do normal"))
            if self.idade == 6:
                if self.imcval > 18.9:
                    self.label_4.setText(str(f"O seu IMC é {self.imcval:.2f} e tem obesidade"))
                elif self.imcval >= 17.1:
                    self.label_4.setText(str(f"O seu IMC é {self.imcval:.2f} e tem sobrepeso"))
                elif self.imcval >= 12.8:
                    self.label_4.setText(str(f"O seu IMC é {self.imcval:.2f} e tem um peso normal"))
                else:
                    self.label_4.setText(str(f"O seu IMC é {self.imcval:.2f} e tem um peso abaixo do normal"))
            if self.idade == 7:
                if self.imcval > 19.5:
                    self.label_4.setText(str(f"O seu IMC é {self.imcval:.2f} e tem obesidade"))
                elif self.imcval >= 17.4:
                    self.label_4.setText(str(f"O seu IMC é {self.imcval:.2f} e tem sobrepeso"))
                elif self.imcval >= 12.9:
                    self.label_4.setText(str(f"O seu IMC é {self.imcval:.2f} e tem um peso normal"))
                else:
                    self.label_4.setText(str(f"O seu IMC é {self.imcval:.2f} e tem um peso abaixo do normal"))
            if self.idade == 8:
                if self.imcval > 20.1:
                    self.label_4.setText(str(f"O seu IMC é {self.imcval:.2f} e tem obesidade"))
                elif self.imcval >= 17.8:
                    self.label_4.setText(str(f"O seu IMC é {self.imcval:.2f} e tem sobrepeso"))
                elif self.imcval >= 13:
                    self.label_4.setText(str(f"O seu IMC é {self.imcval:.2f} e tem um peso normal"))
                else:
                    self.label_4.setText(str(f"O seu IMC é {self.imcval:.2f} e tem um peso abaixo do normal"))
            if self.idade == 9:
                if self.imcval > 21:
                    self.label_4.setText(str(f"O seu IMC é {self.imcval:.2f} e tem obesidade"))
                elif self.imcval >= 18.5:
                    self.label_4.setText(str(f"O seu IMC é {self.imcval:.2f} e tem sobrepeso"))
                elif self.imcval >= 13.3:
                    self.label_4.setText(str(f"O seu IMC é {self.imcval:.2f} e tem um peso normal"))
                else:
                    self.label_4.setText(str(f"O seu IMC é {self.imcval:.2f} e tem um peso abaixo do normal"))
            if self.idade == 10:
                if self.imcval > 22:
                    self.label_4.setText(str(f"O seu IMC é {self.imcval:.2f} e tem obesidade"))
                elif self.imcval >= 19.1:
                    self.label_4.setText(str(f"O seu IMC é {self.imcval:.2f} e tem sobrepeso"))
                elif self.imcval >= 13.6:
                    self.label_4.setText(str(f"O seu IMC é {self.imcval:.2f} e tem um peso normal"))
                else:
                    self.label_4.setText(str(f"O seu IMC é {self.imcval:.2f} e tem um peso abaixo do normal"))
            if self.idade == 11:
                if self.imcval > 23.2:
                    self.label_4.setText(str(f"O seu IMC é {self.imcval:.2f} e tem obesidade"))
                elif self.imcval >= 20:
                    self.label_4.setText(str(f"O seu IMC é {self.imcval:.2f} e tem sobrepeso"))
                elif self.imcval >= 14:
                    self.label_4.setText(str(f"O seu IMC é {self.imcval:.2f} e tem um peso normal"))
                else:
                    self.label_4.setText(str(f"O seu IMC é {self.imcval:.2f} e tem um peso abaixo do normal"))
            if self.idade == 12:
                if self.imcval > 24.4:
                    self.label_4.setText(str(f"O seu IMC é {self.imcval:.2f} e tem obesidade"))
                elif self.imcval >= 20.9:
                    self.label_4.setText(str(f"O seu IMC é {self.imcval:.2f} e tem sobrepeso"))
                elif self.imcval >= 14.5:
                    self.label_4.setText(str(f"O seu IMC é {self.imcval:.2f} e tem um peso normal"))
                else:
                    self.label_4.setText(str(f"O seu IMC é {self.imcval:.2f} e tem um peso abaixo do normal"))
            if self.idade == 13:
                if self.imcval > 25.6:
                    self.label_4.setText(str(f"O seu IMC é {self.imcval:.2f} e tem obesidade"))
                elif self.imcval >= 22:
                    self.label_4.setText(str(f"O seu IMC é {self.imcval:.2f} e tem sobrepeso"))
                elif self.imcval >= 15.1:
                    self.label_4.setText(str(f"O seu IMC é {self.imcval:.2f} e tem um peso normal"))
                else:
                    self.label_4.setText(str(f"O seu IMC é {self.imcval:.2f} e tem um peso abaixo do normal"))
            if self.idade == 14:
                if self.imcval > 26.6:
                    self.label_4.setText(str(f"O seu IMC é {self.imcval:.2f} e tem obesidade"))
                elif self.imcval >= 22.9:
                    self.label_4.setText(str(f"O seu IMC é {self.imcval:.2f} e tem sobrepeso"))
                elif self.imcval >= 15.6:
                    self.label_4.setText(str(f"O seu IMC é {self.imcval:.2f} e tem um peso normal"))
                else:
                    self.label_4.setText(str(f"O seu IMC é {self.imcval:.2f} e tem um peso abaixo do normal"))
            if self.idade == 15:
                if self.imcval > 27.6:
                    self.label_4.setText(str(f"O seu IMC é {self.imcval:.2f} e tem obesidade"))
                elif self.imcval >= 23.6:
                    self.label_4.setText(str(f"O seu IMC é {self.imcval:.2f} e tem sobrepeso"))
                elif self.imcval >= 16.1:
                    self.label_4.setText(str(f"O seu IMC é {self.imcval:.2f} e tem um peso normal"))
                else:
                    self.label_4.setText(str(f"O seu IMC é {self.imcval:.2f} e tem um peso abaixo do normal"))
            if self.idade == 16:
                if self.imcval > 28.3:
                    self.label_4.setText(str(f"O seu IMC é {self.imcval:.2f} e tem obesidade"))
                elif self.imcval >= 24.3:
                    self.label_4.setText(str(f"O seu IMC é {self.imcval:.2f} e tem sobrepeso"))
                elif self.imcval >= 16.4:
                    self.label_4.setText(str(f"O seu IMC é {self.imcval:.2f} e tem um peso normal"))
                else:
                    self.label_4.setText(str(f"O seu IMC é {self.imcval:.2f} e tem um peso abaixo do normal"))
            if self.idade == 17:
                if self.imcval > 28.6:
                    self.label_4.setText(str(f"O seu IMC é {self.imcval:.2f} e tem obesidade"))
                elif self.imcval >= 24.6:
                    self.label_4.setText(str(f"O seu IMC é {self.imcval:.2f} e tem sobrepeso"))
                elif self.imcval >= 16.6:
                    self.label_4.setText(str(f"O seu IMC é {self.imcval:.2f} e tem um peso normal"))
                else:
                    self.label_4.setText(str(f"O seu IMC é {self.imcval:.2f} e tem um peso abaixo do normal"))
            if self.idade == 18:
                if self.imcval > 28.9:
                    self.label_4.setText(str(f"O seu IMC é {self.imcval:.2f} e tem obesidade"))
                elif self.imcval >= 24.9:
                    self.label_4.setText(str(f"O seu IMC é {self.imcval:.2f} e tem sobrepeso"))
                elif self.imcval >= 16.7:
                    self.label_4.setText(str(f"O seu IMC é {self.imcval:.2f} e tem um peso normal"))
                else:
                    self.label_4.setText(str(f"O seu IMC é {self.imcval:.2f} e tem um peso abaixo do normal"))
            if self.idade >= 19:
                if self.imcval > 30:
                    self.label_4.setText(str(f"O seu IMC é {self.imcval:.2f} e tem obesidade"))
                elif self.imcval >= 24.9:
                    self.label_4.setText(str(f"O seu IMC é {self.imcval:.2f} e tem sobrepeso"))
                elif self.imcval >= 18.5:
                    self.label_4.setText(str(f"O seu IMC é {self.imcval:.2f} e tem um peso normal"))
                else:
                    self.label_4.setText(str(f"O seu IMC é {self.imcval:.2f} e tem um peso abaixo do normal"))




    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Dialog"))
        self.label.setText(_translate("MainWindow", "CALCULADORA DE IMC"))
        self.label_2.setText(_translate("MainWindow", "Peso(Kg)"))
        self.label_3.setText(_translate("MainWindow", "Altura(m)"))
        self.pushButton.setText(_translate("MainWindow", "CALCULAR"))
        self.label_5.setText(_translate("MainWindow", "Gênero(M/F)"))
        self.label_6.setText(_translate("MainWindow", "Idade"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    app.exec_()
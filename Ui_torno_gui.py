# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\Radar y simulacion\Desktop\Torno\torno_gui.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 300)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.mov_x_l = QtWidgets.QLabel(self.centralwidget)
        self.mov_x_l.setGeometry(QtCore.QRect(40, 100, 141, 16))
        font = QtGui.QFont()
        font.setFamily("MS Gothic")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.mov_x_l.setFont(font)
        self.mov_x_l.setObjectName("mov_x_l")
        self.mov_y_l = QtWidgets.QLabel(self.centralwidget)
        self.mov_y_l.setGeometry(QtCore.QRect(40, 130, 141, 16))
        font = QtGui.QFont()
        font.setFamily("MS Gothic")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.mov_y_l.setFont(font)
        self.mov_y_l.setObjectName("mov_y_l")
        self.mov_x_value = QtWidgets.QLabel(self.centralwidget)
        self.mov_x_value.setGeometry(QtCore.QRect(430, 110, 71, 16))
        font = QtGui.QFont()
        font.setFamily("MS Gothic")
        font.setPointSize(12)
        self.mov_x_value.setFont(font)
        self.mov_x_value.setObjectName("mov_x_value")
        self.mov_y_value = QtWidgets.QLabel(self.centralwidget)
        self.mov_y_value.setGeometry(QtCore.QRect(430, 140, 71, 16))
        font = QtGui.QFont()
        font.setFamily("MS Gothic")
        font.setPointSize(12)
        self.mov_y_value.setFont(font)
        self.mov_y_value.setObjectName("mov_y_value")
        self.torno = QtWidgets.QLabel(self.centralwidget)
        self.torno.setGeometry(QtCore.QRect(250, 10, 71, 51))
        font = QtGui.QFont()
        font.setFamily("MS Gothic")
        font.setPointSize(19)
        font.setBold(True)
        font.setWeight(75)
        self.torno.setFont(font)
        self.torno.setObjectName("torno")
        self.tare = QtWidgets.QPushButton(self.centralwidget)
        self.tare.setGeometry(QtCore.QRect(410, 170, 111, 23))
        font = QtGui.QFont()
        font.setFamily("MS Gothic")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.tare.setFont(font)
        self.tare.setAutoFillBackground(False)
        self.tare.setStyleSheet("")
        self.tare.setObjectName("tare")
        self.input_x = QtWidgets.QLineEdit(self.centralwidget)
        self.input_x.setGeometry(QtCore.QRect(190, 100, 113, 20))
        font = QtGui.QFont()
        font.setFamily("MS Gothic")
        font.setPointSize(10)
        self.input_x.setFont(font)
        self.input_x.setObjectName("input_x")
        self.input_y = QtWidgets.QLineEdit(self.centralwidget)
        self.input_y.setGeometry(QtCore.QRect(190, 130, 113, 20))
        font = QtGui.QFont()
        font.setFamily("MS Gothic")
        font.setPointSize(10)
        self.input_y.setFont(font)
        self.input_y.setObjectName("input_y")
        self.mover_x = QtWidgets.QPushButton(self.centralwidget)
        self.mover_x.setGeometry(QtCore.QRect(310, 100, 75, 23))
        font = QtGui.QFont()
        font.setFamily("MS Gothic")
        font.setPointSize(10)
        self.mover_x.setFont(font)
        self.mover_x.setObjectName("mover_x")
        self.mover_y = QtWidgets.QPushButton(self.centralwidget)
        self.mover_y.setGeometry(QtCore.QRect(310, 130, 75, 23))
        font = QtGui.QFont()
        font.setFamily("MS Gothic")
        font.setPointSize(10)
        self.mover_y.setFont(font)
        self.mover_y.setObjectName("mover_y")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 600, 21))
        self.menubar.setObjectName("menubar")
        self.menuSalir = QtWidgets.QMenu(self.menubar)
        self.menuSalir.setObjectName("menuSalir")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionSalir = QtWidgets.QAction(MainWindow)
        self.actionSalir.setObjectName("actionSalir")
        self.menuSalir.addAction(self.actionSalir)
        self.menubar.addAction(self.menuSalir.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "TORNO"))
        self.mov_x_l.setText(_translate("MainWindow", "Movimiento en X:"))
        self.mov_y_l.setText(_translate("MainWindow", "Movimiento en Y:"))
        self.mov_x_value.setText(_translate("MainWindow", "TextLabel"))
        self.mov_y_value.setText(_translate("MainWindow", "TextLabel"))
        self.torno.setText(_translate("MainWindow", "TORNO"))
        self.tare.setText(_translate("MainWindow", "Tare"))
        self.mover_x.setText(_translate("MainWindow", "Mover X"))
        self.mover_y.setText(_translate("MainWindow", "Mover Y"))
        self.menuSalir.setTitle(_translate("MainWindow", "Opciones"))
        self.actionSalir.setText(_translate("MainWindow", "Salir"))

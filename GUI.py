from xmlrpc.client import Server
from PyQt5 import QtCore, QtGui, QtWidgets
from Ui_torno_gui import Ui_MainWindow
import sys
from threading import Thread
import keyboard
import time
import serial
import serial.tools.list_ports

myports = [tuple(p) for p in list(serial.tools.list_ports.comports())]

class MainWindowTorno(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        self.threadFlag = False
        self.connThread = Thread(target=self.mainLoop)
        self.connThread.start()
        self.mov_x_value.setText("0 mm")
        self.mov_y_value.setText("0 mm")
        self.value_x = 0
        self.value_y = 1
        self.tare.clicked.connect(self.tare_)
        self.mover_x.clicked.connect(self.mover_x_fun)
        self.mover_y.clicked.connect(self.mover_y_fun)
        self.ports= ['','']
        print(myports)
        for p, n, l in myports:
            if 'LOCATION=1-1' in l:
                self.ports[0] = p
            if 'LOCATION=1-6' in l:
                self.ports[1] = p
        self.motor1 = serial.Serial(self.ports[1], 9600, timeout=1)
        

                

    def closeEvent(self, event):
        print("User has clicked the red x on the main window")
        self.threadFlag = True
        event.accept()

    def mainLoop(self):
        while self.threadFlag == False:
            '''
            if keyboard.is_pressed('d'):
                self.value_x +=1
                self.mov_x_value.setText(str(self.value_x) + " mm")
                self.write_data(1, self.motor1)
                time.sleep(0.25)
            if keyboard.is_pressed('a'):
                self.value_x -=1
                self.mov_x_value.setText(str(self.value_x) + " mm")
                self.write_data(-1, self.motor1)
                time.sleep(0.25)
            if keyboard.is_pressed('w'):
                self.value_y +=1
                self.mov_y_value.setText(str(self.value_y) + " mm")
                time.sleep(0.25)
            if keyboard.is_pressed('s'):
                self.value_y -=1
                self.mov_y_value.setText(str(self.value_y) + " mm")
                time.sleep(0.25)
            '''
    def tare_(self):
        self.value_y=0
        self.value_x=0
        self.mov_x_value.setText(str(self.value_x) + " mm")
        self.mov_y_value.setText(str(self.value_y) + " mm")
    def write_data(self, data, motor):
        motor.reset_output_buffer()
        motor.write((str(data)+'\n').encode("utf-8"))
        motor.flush()
    def mover_x_fun(self):
        if self.input_x.text()[0] == '-':
            if self.input_x.text()[1:].isnumeric():
                print(self.input_x.text())
                self.write_data(self.input_x.text(), self.motor1)
                self.value_x += int(self.input_x.text())
                self.mov_x_value.setText(str(self.value_x) + " mm")
                self.input_x.setText("")
        elif self.input_x.text().isnumeric():
                print(self.input_x.text())
                self.write_data(self.input_x.text(), self.motor1)
                self.value_x += int(self.input_x.text())
                self.mov_x_value.setText(str(self.value_x) + " mm")
                self.input_x.setText("")
    def mover_y_fun(self):
        pass
if __name__ == "__main__":
    stop_threads = False
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = MainWindowTorno()
    MainWindow.show()
    sys.exit(app.exec_())
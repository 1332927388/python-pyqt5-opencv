from UI import mywindow
import sys
from PyQt5 import QtWidgets
from command import command
from MySerial import MySerial
import threading
import time

class main_window(mywindow):
    def __init__(self):
        super().__init__()
        self.initwindow()
    def initwindow(self):
        self.ser = MySerial()
        self.cmd=command()
        self.cmdlist=self.cmd.getCommand()
        self.BOOL=False
        self.workmodule1.clicked.connect(self.workmodule_1)
        self.workmodule2.clicked.connect(self.workmodule_2)
        self.workmodule3.clicked.connect(self.workmodule_3)
        print(self.ser.ReadData())
        #threading.Thread(target=self.workmodule_1,).start()
        #threading.Thread(target=self.workmodule_2).start()
        threading.Thread(target=self.workmodule_3).start()
    def workmodule_1(self):
        text = ''
        text = self.ser.receivedata
        for i in range(len(self.cmdlist)):
            for m in range(len(self.cmdlist[i])):
                if 'step' in text:
                    self.ser.SendData(self.cmdlist[i][m])
                    ser.write(bytes.fromhex('0D 0A'))
                    time.sleep(1)
                    text=''
                while (~('step' in text)):
                    text=self.ser.receivedata
                    continue
    def workmodule_2(self):
        text = ''
        text = self.ser.receivedata
        for i in range(len(self.cmdlist)):
            for m in range(len(self.cmdlist[i])):
                if 'step' in text:
                    self.ser.SendData(self.cmdlist[i][m])
                    ser.write(bytes.fromhex('0D 0A'))
                    print('why')
                    time.sleep(1)
                    text=''
                while (~('step' in text)):
                    text=self.ser.receivedata
                    continue
    def workmodule_3(self):
        # while True:
        #     i=len(self.cmdlist)
        text = ''
        text = self.ser.receivedata
        print('why')
        for i in range(len(self.cmdlist)):
            for m in range(len(self.cmdlist[i])):
                if 'step' in text:
                    self.ser.SendData(self.cmdlist[i][m])
                    ser.write(bytes.fromhex('0D 0A'))
                    print(text)
                    time.sleep(1)
                    text=''

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = main_window()
    # cmd=command()#获取所有指令集,大小为7*n的二维矩阵
    # print(cmd.getCommand())
    sys.exit(app.exec_())
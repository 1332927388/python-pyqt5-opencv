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
        #print(self.cmdlist)
        self.BOOL=False
        self.workmodule1.clicked.connect(self.workmodule_1)
        self.workmodule2.clicked.connect(self.workmodule_2)
        self.workmodule3.clicked.connect(self.workmodule_3)
    
    #点击按钮后    打开指令发送线程
    def workmodule_1(self):
        threading.Thread(target=self.workmodule_31).start()
    def workmodule_2(self):
        threading.Thread(target=self.workmodule_32).start()
    def workmodule_3(self):
        threading.Thread(target=self.workmodule_33).start()
    
    
    
    #按顺序发送指令
    def workmodule_31(self):
        print('why')
        for i in range(len(self.cmdlist)):
            for m in range(len(self.cmdlist[i])):
                self.ser.SendData(self.cmdlist[i][m])
                text=''
                while not('STEP' in text):
                    print(self.cmdlist[i][m])
                    text = self.ser.ReadData()
                    print(text)
    def workmodule_32(self):
        print('why')
        for i in range(len(self.cmdlist)):
            for m in range(len(self.cmdlist[i])):
                self.ser.SendData(self.cmdlist[i][m])
                text=''
                while not('STEP' in text):
                    print(self.cmdlist[i][m])
                    text = self.ser.ReadData()
                    print(text)
    def workmodule_33(self):
        # while True:
        #     i=len(self.cmdlist)
        #self.ser.SendData('AA A0 01 01 00 00 10 ff ')
        # text = ''
        # text = self.ser.ReadData()
        print('why')
        for i in range(len(self.cmdlist)):
            for m in range(len(self.cmdlist[i])):
                #if 'STEP' in text:
                    # while ('step in text')
                    #self.ser.SendData(self.cmdlist[i][m])
                #self.ser.SendData('AA A0 01 01 00 00 10 ff ')
                    #ser.write(bytes.fromhex('0D 0A'))
                    # text=self.ser.ReadData()
                    # print(text+'why')
                        #time.sleep(1)
                #print(self.cmdlist[i][m])
                self.ser.SendData(self.cmdlist[i][m])
                text=''
                while not('STEP' in text):
                    #time.sleep(0.6)
                    #threading.Thread(target=self.ser.SendData,args=self.cmdlist[i][m])
                    #self.ser.SendData(self.cmdlist[i][m])
                    print(self.cmdlist[i][m])
                    text = self.ser.ReadData()
                    print(text)



if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = main_window()
    sys.exit(app.exec_())
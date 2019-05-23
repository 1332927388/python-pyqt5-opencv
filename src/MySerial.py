import serial
import serial.tools.list_ports
import re
import time
import threading

class MySerial():
    def __init__(self):
        super().__init__()
        self.receivedata='pok'
        self.initSerial()
    def initSerial(self):
        self.comnumber = self.getcom()
        self.ser=serial.Serial(self.comnumber,115200,timeout=0.5)
        threading.Thread(target=self.ReadData).start()
        #n=self.ReadData()
        print(self.ser.is_open)
        #print(self.receivedata)
        # print(ser.isOpen())
        # #ser.isOpen()
        # print(self.comnumber)
        # print(type(self.comnumber))
    
    #系统自动获取当前连接的COM口
    def getcom(self):
        port_list = list(serial.tools.list_ports.comports())
        p1 = re.compile(r'[(](.*?)[)]', re.S)
        com=''
        if len(port_list) == 1:
            for i in range(0,len(port_list)):
                com=(re.findall(p1,str(port_list[i]))[0])
        print(com)
        return com

    def ReadData(self):
        while True:
        # n=self.ser.inWaiting()
        # print(n)
        #if self.ser.is_open():
        #self.receivedata = self.ser.read(self.ser.inWaiting).decode("UTF-8")
            self.ser.flush()
            self.ser.flushInput()
            time.sleep(2)
            self.receivedata = self.ser.readline()#.decode("UTF-8")
            #print(self.receivedata)
        #self.ser.close()
        return self.receivedata
    
    def SendData(self,data):
        self.ser.write(bytes.fromhex(data))
        time.sleep(0.6)
        self.ser.write(bytes.fromhex('0D 0A'))
        print('qedq')

if __name__ == "__main__":
    sad=MySerial()
    while True:
        #time.sleep(2)
        n=sad.ReadData()
        print(n)
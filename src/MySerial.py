import serial
import serial.tools.list_ports
import re


class MySerial():
    def __init__(self):
        super().__init__()
        self.initSerial()
    def initSerial(self):
        self.comnumber = self.getcom()
        self.ser=serial.Serial(self.comnumber,115200,timeout=0.5)
        print(ser.isOpen())
        #ser.isOpen()
        print(self.comnumber)
        print(type(self.comnumber))
    
    #系统自动获取当前连接的COM口
    def getcom(self):
        port_list = list(serial.tools.list_ports.comports())
        p1 = re.compile(r'[(](.*?)[)]', re.S)
        if len(port_list) == 1:
            for i in range(0,len(port_list)):
                com=(re.findall(p1,str(port_list[i]))[0])
        return com

    def senddata(self,data):








if  __name__ == "__main__":
    myserial=MySerial()


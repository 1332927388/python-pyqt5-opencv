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
        self.ser=serial.Serial(self.comnumber,115200,timeout=0.8)
        threading.Thread(target=self.ReadData).start()
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
            #self.ser.flush()
            #self.ser.flushInput()
            time.sleep(0.8)
            self.receivedata = self.ser.read(self.ser.in_waiting).decode("UTF-8")
            #print(self.receivedata.replace('\r\n',''))
            #self.ser.close()
            return self.receivedata.replace('\r\n','')
    
    def SendData(self,data):

        #32接收到的消息是以\r\n***\r\n格式的
        self.ser.write(bytes.fromhex('0D 0A'))
        self.ser.write(bytes.fromhex(data))
        #time.sleep(0.6)
        self.ser.write(bytes.fromhex('0D 0A'))

if __name__ == "__main__":
    sad=MySerial()
    # while True:
    sad.SendData('AA A0 01 01 00 00 10 ff ')
    n=sad.ReadData()
    print(n.replace('\r\n',''))
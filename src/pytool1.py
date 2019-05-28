import serial #导入模块
import threading
import xlrd
import os


STRGLO="" #读取的数据
BOOL=True  #读取标志位
sendStrlist=[]
recFlag=False
sendNote=[]
fileList = []

# 所有xls文件
def printPath():
    XLS='.xls'
    # 返回一个列表，其中包含在目录条目的名称
    files = os.listdir(os.getcwd())
    # 先添加目录级别
    for f in files:
        if(XLS in f):
            # 添加文件
            fileList.append(f)
    for f in range(len(fileList)):
            print(f,' ',fileList[f])
    ch=input('choose one:')
    print("open:",fileList[int(ch)])
    return ch

#读数代码本体实现
def ReadData(ser):
    global STRGLO,BOOL,recFlag
    # 循环接收数据，此为死循环，可用线程实现
    while BOOL:
        if ser.in_waiting:
            STRGLO = ser.readline(ser.in_waiting).decode("UTF-8")
            print(STRGLO.replace('\r\n', ''))
            recFlag=True

#打开串口
# 端口，GNU / Linux上的/ dev / ttyUSB0 等 或 Windows上的 COM3 等
# 波特率，标准值之一：50,75,110,134,150,200,300,600,1200,1800,2400,4800,9600,19200,38400,57600,115200
# 超时设置,None：永远等待操作，0为立即返回请求结果，其他值为等待超时时间(单位为秒）
def DOpenPort(portx,bps,timeout):
    ret=False
    try:
        # 打开串口，并得到串口对象
        ser = serial.Serial(portx, bps, timeout=timeout)
        #判断是否打开成功
        if(ser.is_open):
           ret=True
           threading.Thread(target=ReadData, args=(ser,)).start()
    except Exception as e:
        print("---异常---：", e)
    return ser,ret

#关闭串口
def DColsePort(ser):
    global BOOL
    BOOL=False
    ser.close()

#写数据
def DWritePort(ser,text):
    result = ser.write(text.encode("gbk"))  # 写数据
    return result
#try:
#count=DWritePort(ser,"我是东小东，哈哈")

#读数据
def DReadPort():
    global STRGLO,recFlag
    while BOOL:
        if(recFlag == True):
            str0=STRGLO
            str1=str0
            STRGLO=""#清空当次读取
            recFlag = False
            return str0,str1

if __name__=="__main__":
    ser,ret=DOpenPort("COM8",9600,1)
    STEP='STEP'
    GET='GET'
    if(ret==True):#判断串口是否成功打开
        print("open success:",ser.name)
        #print(ser.baudrate ) # 波特率
        #print(ser.bytesize)  # 字节大小
        #print(ser.parity)  # 校验位N－无校验，E－偶校验，O－奇校验
        #print(ser.stopbits)  # 停止位
        #print(ser.timeout)  # 读超时设置
        #print(ser.writeTimeout)  # 写超时
        #print(ser.interCharTimeout) # 字符间隔超时
        ch = printPath();
        readbook = xlrd.open_workbook(fileList[int(ch)])
        sheet = readbook.sheet_by_index(0)
        sendStrlist = sheet.col_values(0)
        sendNote= sheet.col_values(1)
        for data in range(len(sendStrlist)):
            n = ser.write(bytes.fromhex(sendStrlist[data])) # 十六进制数据
            print('now:',sendNote[data])
            ser.write(bytes.fromhex('0D 0A'))
            while True:
                str0,str1=DReadPort()
                if ((STEP in str0) or (STEP in str1)):
                    break
        print("Send DATA Finish")
        DColsePort(ser)  #关闭串口
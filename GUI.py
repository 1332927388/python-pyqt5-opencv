import sys  
from PyQt5 import QtWidgets  
from PyQt5.QtWidgets import QSplitter,QFrame,QLabel,QPushButton,QLineEdit,QComboBox
from PyQt5.QtWidgets import QHBoxLayout,QVBoxLayout,QGridLayout,QFormLayout
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtCore import  Qt
from PyQt5.QtGui import QIcon,QPixmap

  
class MyWindow(QtWidgets.QWidget):  

    def __init__(self):  
        super().__init__()        
        # 开始：
        wlayout = QtWidgets.QHBoxLayout() # 全局布局（1个）：水平
        
        hlayout = QHBoxLayout() # 局部布局（4个）：水平、竖直、网格、表单
        
        vlayout = QGridLayout()
        vlayout.setDefaultPositioning(100,100)
        vlayout.setAlignment(Qt.AlignTop)
        vlayout.setVerticalSpacing(30)
        
        glayout = QGridLayout()
        glayout.setAlignment(Qt.AlignLeft)
        glayout.setRowStretch
        glayout.setHorizontalSpacing(80) 
        flayout = QFormLayout()
        
        baud = ['12800','115200','230400','256000','460800','921600','1382400']
        serials = ['COM1','COM2','COM3','COM4','COM5','COM6','COM7','COM8',
                        'COM9','COM10','COM11']
        self.fasong_btn1 = QPushButton('发送', self)
        self.fasong_btn2 = QPushButton('发送',self)
        self.fasong_btn3 = QPushButton('发送',self)
        self.receive_btn = QPushButton("接收",self)
        self.receive_btn.setFixedSize(80,60)
        self.com_box = QComboBox()
        self.com_box.addItems(baud)
        #self.bel = QLabel("串口选择")
        self.c_baud = QLabel("波特率")
        
        self.line_text1 = QLineEdit()
        self.line_text2 = QLineEdit()
        self.line_text3 = QLineEdit()

        self.hwg_pic = QLabel(self) # 准备四个部件
        self.hwg_pic.setPixmap(QPixmap("Icon/meidui.jpg"))
        self.hwg_pic.setScaledContents(True)
       
        hlayout.addWidget(self.hwg_pic)
       
        vlayout.setDefaultPositioning(10,10)
        #vlayout.addWidget(self.bel,0,0)
        vlayout.addWidget(self.receive_btn,0,0)
        vlayout.addWidget(self.com_box,1,1)
        vlayout.addWidget(self.c_baud,1,0)

        glayout.addWidget(self.line_text1,0,0)
        glayout.addWidget(self.fasong_btn1,0,1)
        glayout.addWidget(self.line_text2,1,0)
        glayout.addWidget(self.fasong_btn2,1,1)
        glayout.addWidget(self.line_text3,2,0)
        glayout.addWidget(self.fasong_btn3,2,1)
     
        #菜单和工具栏
        tools_bar = QMainWindow(self)
        menubar = tools_bar.menuBar()
        #menubar = tools_bar.menuBar()
        
        
        
        
        hwg = QFrame(self)
        hwg.setFrameShape(QFrame.StyledPanel)
        hwg.setMinimumSize(100,100)


        vwg = QFrame(self)
        vwg.setFrameShape(QFrame.StyledPanel)
        vwg.setMinimumSize(100,100)

        gwg = QFrame(self)
        gwg.setFrameShape(QFrame.StyledPanel)
        gwg.setMinimumSize(100,100)

        hwg.setLayout(hlayout)
        vwg.setLayout(vlayout)
        gwg.setLayout(glayout)
        
        
        splitter1 = QSplitter(Qt.Horizontal)
        splitter1.addWidget(hwg)
        splitter1.addWidget(vwg)
        splitter1.setSizes([600,140])
        splitter2=QSplitter(Qt.Vertical)
        splitter2.addWidget(splitter1)
        splitter2.addWidget(gwg)
        splitter2.setSizes([600,140])
        
        wlayout.addWidget(splitter2)
        self.setLayout(wlayout) # 窗体本尊设置全局布局
        
        self.setGeometry(300, 300, 800, 800)
        self.setWindowTitle('吴洪岩') 
        self.setWindowIcon(QIcon('Icon/meidui.JPG'))
        self.show()

if __name__=="__main__":
    app = QtWidgets.QApplication(sys.argv)    
    win = MyWindow()  
    win.show()  
    sys.exit(app.exec_())
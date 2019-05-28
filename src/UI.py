import sys
from PyQt5 import QtCore, QtGui,QtWidgets
from PyQt5.QtCore import  Qt,QBasicTimer
from PyQt5.QtWidgets import QWidget,QMessageBox,QStackedWidget,QProgressBar
from PyQt5.QtWidgets import QPushButton,QHBoxLayout,QVBoxLayout,QStackedLayout,QGridLayout
from PyQt5.QtWidgets import QFrame,QSplitter,QTextEdit,QLineEdit,QSplitter
from PyQt5.QtGui import QIcon
from PyQt5.Qt import QSize,QFont
from MyFigure import MyFigure
import threading
class mywindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        self.F = MyFigure(width=1,height=1,dpi=100)
        self.F.plotsin()

        self.timer = QBasicTimer()
        self.step = 0
        
        
        #self.workmodule1.clicked.connect(self.workmodule_1)

        
        #全局布局
        self.GlobalLayout=QHBoxLayout()
        #三个按钮
        self.fasong_btn1 = QPushButton('存储', self)
        self.fasong_btn1.setFont(QFont("微软雅黑",20,QFont.Bold))
        self.fasong_btn1.setFixedSize(140,60)
        self.fasong_btn1.clicked.connect(self.cunchu)
        self.fasong_btn2 = QPushButton('温度',self)
        self.fasong_btn2.setFont(QFont("微软雅黑",20,QFont.Bold))
        self.fasong_btn2.setFixedSize(140,60)
        self.fasong_btn2.clicked.connect(self.wendu)
        self.fasong_btn3 = QPushButton('工作状态',self)
        self.fasong_btn3.setFont(QFont("微软雅黑",12,QFont.Bold))
        self.fasong_btn3.setFixedSize(140,60)
        self.fasong_btn3.clicked.connect(self.work)
        
        #工作模式按钮
        self.workmodule1=QPushButton('模式1',self)
        self.workmodule1.setFont(QFont("微软雅黑",18,QFont.Bold))
        self.workmodule1.setFixedSize(100,100)
        #self.workmodule1.clicked.connect(self.workmodule_1)
        self.workmodule1.clicked.connect(self.doAction)
        self.workmodule2=QPushButton('模式2',self)
        self.workmodule2.setFont(QFont("微软雅黑",18,QFont.Bold))
        self.workmodule2.setFixedSize(100,100)
        self.workmodule3=QPushButton('模式3',self)
        self.workmodule3.setFont(QFont("微软雅黑",18,QFont.Bold))
        self.workmodule3.setFixedSize(100,100)
        
        #存储按钮
        self.cunchu_btn1 = QPushButton('',self)
        self.cunchu_btn1.clicked.connect(self.cunchu_btn1_1)
        self.cunchu_btn1.setFixedSize(90,90)
        self.cunchu_btn1.setStyleSheet("QPushButton{color:black}"
                                  "QPushButton:hover{color:red}"
                                  "QPushButton{background-color:rgb(255,0,0)}"
                                  "QPushButton{border:2px}"
                                  "QPushButton{border-radius:10px}"
                                  "QPushButton{padding:2px 4px}")
        self.cunchu_btn2 = QPushButton('',self)
        self.cunchu_btn2.setFixedSize(90,90)
        self.cunchu_btn3 = QPushButton('',self)
        self.cunchu_btn3.setFixedSize(90,90)
        self.cunchu_btn4 = QPushButton('',self)
        self.cunchu_btn4.setFixedSize(90,90)
        self.cunchu_btn5 = QPushButton('',self)
        self.cunchu_btn5.setFixedSize(90,90)
        self.cunchu_btn6 = QPushButton('',self)
        self.cunchu_btn6.setFixedSize(90,90)
        self.cunchu_btn7 = QPushButton('',self)
        self.cunchu_btn7.setFixedSize(90,90)
        self.cunchu_btn8 = QPushButton('',self)
        self.cunchu_btn8.setFixedSize(90,90)
        self.cunchu_btn9 = QPushButton('',self)
        self.cunchu_btn9.setFixedSize(90,90)
        self.cunchu_btn10 = QPushButton('',self)
        self.cunchu_btn10.setFixedSize(90,90)
        self.cunchu_btn11 = QPushButton('',self)
        self.cunchu_btn11.setFixedSize(90,90)
        self.cunchu_btn12 = QPushButton('',self)
        self.cunchu_btn12.setFixedSize(90,90)
        self.cunchu_btn13 = QPushButton('',self)
        self.cunchu_btn13.setFixedSize(90,90)
        self.cunchu_btn14 = QPushButton('',self)
        self.cunchu_btn14.setFixedSize(90,90)
        self.cunchu_btn15 = QPushButton('',self)
        self.cunchu_btn15.setFixedSize(90,90)
        self.cunchu_btn16 = QPushButton('',self)
        self.cunchu_btn16.setFixedSize(90,90)
        self.cunchu_btn17 = QPushButton('',self)
        self.cunchu_btn17.setFixedSize(90,90)
        self.cunchu_btn18 = QPushButton('',self)
        self.cunchu_btn18.setFixedSize(90,90)
        self.cunchu_btn19 = QPushButton('',self)
        self.cunchu_btn19.setFixedSize(90,90)
        self.cunchu_btn20 = QPushButton('',self)
        self.cunchu_btn20.setFixedSize(90,90)
        self.cunchu_btn21 = QPushButton('',self)
        self.cunchu_btn21.setFixedSize(90,90)
        self.cunchu_btn22 = QPushButton('',self)
        self.cunchu_btn22.setFixedSize(90,90)
        self.cunchu_btn23 = QPushButton('',self)
        self.cunchu_btn23.setFixedSize(90,90)
        self.cunchu_btn24 = QPushButton('',self)
        self.cunchu_btn24.setFixedSize(90,90)
        self.cunchu_btn25 = QPushButton('',self)
        self.cunchu_btn25.setFixedSize(90,90)
        self.cunchu_btn26 = QPushButton('',self)
        self.cunchu_btn26.setFixedSize(90,90)
        self.cunchu_btn27 = QPushButton('',self)
        self.cunchu_btn27.setFixedSize(90,90)
        self.cunchu_btn28 = QPushButton('',self)
        self.cunchu_btn28.setFixedSize(90,90)
        self.cunchu_btn29 = QPushButton('',self)
        self.cunchu_btn29.setFixedSize(90,90)
        self.cunchu_btn30 = QPushButton('',self)
        self.cunchu_btn30.setFixedSize(90,90)
        self.cunchu_btn31 = QPushButton('',self)
        self.cunchu_btn31.setFixedSize(90,90)
        self.cunchu_btn32 = QPushButton('',self)
        self.cunchu_btn32.setFixedSize(90,90)
        self.cunchu_btn33 = QPushButton('',self)
        self.cunchu_btn33.setFixedSize(90,90)
        self.cunchu_btn34 = QPushButton('',self)
        self.cunchu_btn34.setFixedSize(90,90)
        self.cunchu_btn35 = QPushButton('',self)
        self.cunchu_btn35.setFixedSize(90,90)
        self.cunchu_btn36 = QPushButton('',self)
        self.cunchu_btn36.setFixedSize(90,90)

        self.cunchu_btn2.setStyleSheet("QPushButton{color:black}"
                            "QPushButton:hover{color:red}"
                            "QPushButton{background-color:rgb(255,0,0)}"
                            "QPushButton{border:2px}"
                            "QPushButton{border-radius:10px}"
                            "QPushButton{padding:2px 4px}")
        self.cunchu_btn3.setStyleSheet("QPushButton{color:black}"
                            "QPushButton:hover{color:red}"
                            "QPushButton{background-color:rgb(255,0,0)}"
                            "QPushButton{border:2px}"
                            "QPushButton{border-radius:10px}"
                            "QPushButton{padding:2px 4px}")
        self.cunchu_btn4.setStyleSheet("QPushButton{color:black}"
                            "QPushButton:hover{color:red}"
                            "QPushButton{background-color:rgb(255,0,0)}"
                            "QPushButton{border:2px}"
                            "QPushButton{border-radius:10px}"
                            "QPushButton{padding:2px 4px}")
        self.cunchu_btn5.setStyleSheet("QPushButton{color:black}"
                            "QPushButton:hover{color:red}"
                            "QPushButton{background-color:rgb(255,0,0)}"
                            "QPushButton{border:2px}"
                            "QPushButton{border-radius:10px}"
                            "QPushButton{padding:2px 4px}")
        self.cunchu_btn6.setStyleSheet("QPushButton{color:black}"
                            "QPushButton:hover{color:red}"
                            "QPushButton{background-color:rgb(255,0,0)}"
                            "QPushButton{border:2px}"
                            "QPushButton{border-radius:10px}"
                            "QPushButton{padding:2px 4px}")
        self.cunchu_btn7.setStyleSheet("QPushButton{color:black}"
                            "QPushButton:hover{color:red}"
                            "QPushButton{background-color:rgb(255,0,0)}"
                            "QPushButton{border:2px}"
                            "QPushButton{border-radius:10px}"
                            "QPushButton{padding:2px 4px}")
        self.cunchu_btn8.setStyleSheet("QPushButton{color:black}"
                            "QPushButton:hover{color:red}"
                            "QPushButton{background-color:rgb(255,0,0)}"
                            "QPushButton{border:2px}"
                            "QPushButton{border-radius:10px}"
                            "QPushButton{padding:2px 4px}")
        self.cunchu_btn9.setStyleSheet("QPushButton{color:black}"
                            "QPushButton:hover{color:red}"
                            "QPushButton{background-color:rgb(255,0,0)}"
                            "QPushButton{border:2px}"
                            "QPushButton{border-radius:10px}"
                            "QPushButton{padding:2px 4px}")
        self.cunchu_btn10.setStyleSheet("QPushButton{color:black}"
                            "QPushButton:hover{color:red}"
                            "QPushButton{background-color:rgb(255,0,0)}"
                            "QPushButton{border:2px}"
                            "QPushButton{border-radius:10px}"
                            "QPushButton{padding:2px 4px}")
        self.cunchu_btn11.setStyleSheet("QPushButton{color:black}"
                            "QPushButton:hover{color:red}"
                            "QPushButton{background-color:rgb(255,0,0)}"
                            "QPushButton{border:2px}"
                            "QPushButton{border-radius:10px}"
                            "QPushButton{padding:2px 4px}")
        self.cunchu_btn12.setStyleSheet("QPushButton{color:black}"
                            "QPushButton:hover{color:red}"
                            "QPushButton{background-color:rgb(255,0,0)}"
                            "QPushButton{border:2px}"
                            "QPushButton{border-radius:10px}"
                            "QPushButton{padding:2px 4px}")

        self.cunchu_btn13.setStyleSheet("QPushButton{color:black}"
                            "QPushButton:hover{color:red}"
                            "QPushButton{background-color:rgb(255,0,0)}"
                            "QPushButton{border:2px}"
                            "QPushButton{border-radius:10px}"
                            "QPushButton{padding:2px 4px}")
        self.cunchu_btn14.setStyleSheet("QPushButton{color:black}"
                            "QPushButton:hover{color:red}"
                            "QPushButton{background-color:rgb(255,0,0)}"
                            "QPushButton{border:2px}"
                            "QPushButton{border-radius:10px}"
                            "QPushButton{padding:2px 4px}")
        self.cunchu_btn15.setStyleSheet("QPushButton{color:black}"
                            "QPushButton:hover{color:red}"
                            "QPushButton{background-color:rgb(255,0,0)}"
                            "QPushButton{border:2px}"
                            "QPushButton{border-radius:10px}"
                            "QPushButton{padding:2px 4px}")
        self.cunchu_btn16.setStyleSheet("QPushButton{color:black}"
                            "QPushButton:hover{color:red}"
                            "QPushButton{background-color:rgb(255,0,0)}"
                            "QPushButton{border:2px}"
                            "QPushButton{border-radius:10px}"
                            "QPushButton{padding:2px 4px}")
        self.cunchu_btn17.setStyleSheet("QPushButton{color:black}"
                            "QPushButton:hover{color:red}"
                            "QPushButton{background-color:rgb(255,0,0)}"
                            "QPushButton{border:2px}"
                            "QPushButton{border-radius:10px}"
                            "QPushButton{padding:2px 4px}")
        self.cunchu_btn18.setStyleSheet("QPushButton{color:black}"
                            "QPushButton:hover{color:red}"
                            "QPushButton{background-color:rgb(255,0,0)}"
                            "QPushButton{border:2px}"
                            "QPushButton{border-radius:10px}"
                            "QPushButton{padding:2px 4px}")
        self.cunchu_btn19.setStyleSheet("QPushButton{color:black}"
                            "QPushButton:hover{color:red}"
                            "QPushButton{background-color:rgb(255,0,0)}"
                            "QPushButton{border:2px}"
                            "QPushButton{border-radius:10px}"
                            "QPushButton{padding:2px 4px}")
        self.cunchu_btn20.setStyleSheet("QPushButton{color:black}"
                            "QPushButton:hover{color:red}"
                            "QPushButton{background-color:rgb(255,0,0)}"
                            "QPushButton{border:2px}"
                            "QPushButton{border-radius:10px}"
                            "QPushButton{padding:2px 4px}")
        self.cunchu_btn21.setStyleSheet("QPushButton{color:black}"
                            "QPushButton:hover{color:red}"
                            "QPushButton{background-color:rgb(255,0,0)}"
                            "QPushButton{border:2px}"
                            "QPushButton{border-radius:10px}"
                            "QPushButton{padding:2px 4px}")
        self.cunchu_btn22.setStyleSheet("QPushButton{color:black}"
                            "QPushButton:hover{color:red}"
                            "QPushButton{background-color:rgb(255,0,0)}"
                            "QPushButton{border:2px}"
                            "QPushButton{border-radius:10px}"
                            "QPushButton{padding:2px 4px}")
        self.cunchu_btn23.setStyleSheet("QPushButton{color:black}"
                            "QPushButton:hover{color:red}"
                            "QPushButton{background-color:rgb(255,0,0)}"
                            "QPushButton{border:2px}"
                            "QPushButton{border-radius:10px}"
                            "QPushButton{padding:2px 4px}")
        self.cunchu_btn24.setStyleSheet("QPushButton{color:black}"
                            "QPushButton:hover{color:red}"
                            "QPushButton{background-color:rgb(255,0,0)}"
                            "QPushButton{border:2px}"
                            "QPushButton{border-radius:10px}"
                            "QPushButton{padding:2px 4px}")
        self.cunchu_btn25.setStyleSheet("QPushButton{color:black}"
                            "QPushButton:hover{color:red}"
                            "QPushButton{background-color:rgb(255,0,0)}"
                            "QPushButton{border:2px}"
                            "QPushButton{border-radius:10px}"
                            "QPushButton{padding:2px 4px}")
        self.cunchu_btn26.setStyleSheet("QPushButton{color:black}"
                            "QPushButton:hover{color:red}"
                            "QPushButton{background-color:rgb(255,0,0)}"
                            "QPushButton{border:2px}"
                            "QPushButton{border-radius:10px}"
                            "QPushButton{padding:2px 4px}")
        self.cunchu_btn27.setStyleSheet("QPushButton{color:black}"
                            "QPushButton:hover{color:red}"
                            "QPushButton{background-color:rgb(255,0,0)}"
                            "QPushButton{border:2px}"
                            "QPushButton{border-radius:10px}"
                            "QPushButton{padding:2px 4px}")
        self.cunchu_btn28.setStyleSheet("QPushButton{color:black}"
                            "QPushButton:hover{color:red}"
                            "QPushButton{background-color:rgb(255,0,0)}"
                            "QPushButton{border:2px}"
                            "QPushButton{border-radius:10px}"
                            "QPushButton{padding:2px 4px}")
        self.cunchu_btn29.setStyleSheet("QPushButton{color:black}"
                            "QPushButton:hover{color:red}"
                            "QPushButton{background-color:rgb(255,0,0)}"
                            "QPushButton{border:2px}"
                            "QPushButton{border-radius:10px}"
                            "QPushButton{padding:2px 4px}")
        self.cunchu_btn30.setStyleSheet("QPushButton{color:black}"
                            "QPushButton:hover{color:red}"
                            "QPushButton{background-color:rgb(255,0,0)}"
                            "QPushButton{border:2px}"
                            "QPushButton{border-radius:10px}"
                            "QPushButton{padding:2px 4px}")
        self.cunchu_btn31.setStyleSheet("QPushButton{color:black}"
                            "QPushButton:hover{color:red}"
                            "QPushButton{background-color:rgb(255,0,0)}"
                            "QPushButton{border:2px}"
                            "QPushButton{border-radius:10px}"
                            "QPushButton{padding:2px 4px}")
        self.cunchu_btn32.setStyleSheet("QPushButton{color:black}"
                            "QPushButton:hover{color:red}"
                            "QPushButton{background-color:rgb(255,0,0)}"
                            "QPushButton{border:2px}"
                            "QPushButton{border-radius:10px}"
                            "QPushButton{padding:2px 4px}")
        self.cunchu_btn33.setStyleSheet("QPushButton{color:black}"
                            "QPushButton:hover{color:red}"
                            "QPushButton{background-color:rgb(255,0,0)}"
                            "QPushButton{border:2px}"
                            "QPushButton{border-radius:10px}"
                            "QPushButton{padding:2px 4px}")
        self.cunchu_btn34.setStyleSheet("QPushButton{color:black}"
                            "QPushButton:hover{color:red}"
                            "QPushButton{background-color:rgb(255,0,0)}"
                            "QPushButton{border:2px}"
                            "QPushButton{border-radius:10px}"
                            "QPushButton{padding:2px 4px}")
        self.cunchu_btn35.setStyleSheet("QPushButton{color:black}"
                            "QPushButton:hover{color:red}"
                            "QPushButton{background-color:rgb(255,0,0)}"
                            "QPushButton{border:2px}"
                            "QPushButton{border-radius:10px}"
                            "QPushButton{padding:2px 4px}")
        self.cunchu_btn36.setStyleSheet("QPushButton{color:black}"
                            "QPushButton:hover{color:red}"
                            "QPushButton{background-color:rgb(255,0,0)}"
                            "QPushButton{border:2px}"
                            "QPushButton{border-radius:10px}"
                            "QPushButton{padding:2px 4px}")
        #左边框
        vlayout = QVBoxLayout(self)
        vlayout.addWidget(self.fasong_btn1)
        vlayout.addWidget(self.fasong_btn2)
        vlayout.addWidget(self.fasong_btn3)
        

        
        #hbox = QHBoxLayout(self)
        ###将界面分割成可以自由拉伸的三个窗口
        #第一个,左上角,图像显示框
        self.topleft = QFrame(self)
        self.topleft.setFrameShape(QFrame.StyledPanel)
        self.topleft.setLayout(vlayout)
        #第二个,右上角串口选择框
        
        self.topright = QStackedWidget(self)
        self.topright.setStyleSheet("background:url(:Icon/meidui.jpg)")

        CunFrame = QFrame()
        CunFrame.setFrameShape(QFrame.StyledPanel)

        Cunlayout = QGridLayout()
        Cunlayout.addWidget(self.cunchu_btn1,0,0)
        Cunlayout.addWidget(self.cunchu_btn2,0,1)
        Cunlayout.addWidget(self.cunchu_btn3,0,2)
        Cunlayout.addWidget(self.cunchu_btn4,0,3)
        Cunlayout.addWidget(self.cunchu_btn5,0,4)
        Cunlayout.addWidget(self.cunchu_btn6,0,5)

        Cunlayout.addWidget(self.cunchu_btn7,1,0)
        Cunlayout.addWidget(self.cunchu_btn8,1,1)
        Cunlayout.addWidget(self.cunchu_btn9,1,2)
        Cunlayout.addWidget(self.cunchu_btn10,1,3)
        Cunlayout.addWidget(self.cunchu_btn11,1,4)
        Cunlayout.addWidget(self.cunchu_btn12,1,5)

        Cunlayout.addWidget(self.cunchu_btn13,2,0)
        Cunlayout.addWidget(self.cunchu_btn14,2,1)
        Cunlayout.addWidget(self.cunchu_btn15,2,2)
        Cunlayout.addWidget(self.cunchu_btn16,2,3)
        Cunlayout.addWidget(self.cunchu_btn17,2,4)
        Cunlayout.addWidget(self.cunchu_btn18,2,5)

        Cunlayout.addWidget(self.cunchu_btn19,3,0)
        Cunlayout.addWidget(self.cunchu_btn20,3,1)
        Cunlayout.addWidget(self.cunchu_btn21,3,2)
        Cunlayout.addWidget(self.cunchu_btn22,3,3)
        Cunlayout.addWidget(self.cunchu_btn23,3,4)
        Cunlayout.addWidget(self.cunchu_btn24,3,5)

        Cunlayout.addWidget(self.cunchu_btn25,4,0)
        Cunlayout.addWidget(self.cunchu_btn26,4,1)
        Cunlayout.addWidget(self.cunchu_btn27,4,2)
        Cunlayout.addWidget(self.cunchu_btn28,4,3)
        Cunlayout.addWidget(self.cunchu_btn29,4,4)
        Cunlayout.addWidget(self.cunchu_btn30,4,5)

        Cunlayout.addWidget(self.cunchu_btn31,5,0)
        Cunlayout.addWidget(self.cunchu_btn32,5,1)
        Cunlayout.addWidget(self.cunchu_btn33,5,2)
        Cunlayout.addWidget(self.cunchu_btn34,5,3)
        Cunlayout.addWidget(self.cunchu_btn35,5,4)
        Cunlayout.addWidget(self.cunchu_btn36,5,5)

        CunFrame.setLayout(Cunlayout)
        self.topright.addWidget(CunFrame)

        #温度
        WenFrame = QFrame(self)
        WenFrame.setFrameShape(QFrame.StyledPanel)
        Wenlayout = QHBoxLayout()
        Wenlayout.addWidget(self.F)
        WenFrame.setLayout(Wenlayout)
        self.topright.addWidget(WenFrame)
        
        
        #工作状态
        WorkFrame = QFrame(self)
        WorkFrame.setFrameShape(QFrame.StyledPanel)
        Worklayout = QVBoxLayout()

        
        self.WeiZhi_btn = QPushButton('未知血型',self)
        self.WeiZhi_btn.setFont(QFont("微软雅黑",16,QFont.Bold))
        self.WeiZhi_btn.setFixedSize(140,80)
        self.YiZhi_btn = QPushButton('已知血型',self)
        self.YiZhi_btn.setFont(QFont("微软雅黑",16,QFont.Bold))
        self.YiZhi_btn.setFixedSize(140,80)
        self.ChuXue_btn = QPushButton('直接出血',self)
        self.ChuXue_btn.setFont(QFont("微软雅黑",16,QFont.Bold))
        self.ChuXue_btn.setFixedSize(140,80)
        
        hFrame = QFrame()
        vFrame = QFrame()
        #vFrame.setFocus()
        hwg = QHBoxLayout()
        vwg = QVBoxLayout()

        hwg.addWidget(self.WeiZhi_btn)
        hwg.addWidget(self.YiZhi_btn)
        hwg.addWidget(self.ChuXue_btn)

        self.prsbar = QProgressBar(self)
        self.jindu_btn = QPushButton(self)
        self.jindu_btn.setFixedSize(180,80)
        #self.lb1 = QLineEdit(self)
        #vwg.setAlignment(Qt.AlignVCenter)
        vwg.setAlignment(Qt.AlignHCenter)
        #vwg.addWidget(self.jindu_btn)
        vwg.addWidget(self.prsbar,Qt.AlignHCenter)
        #vwg.addWidget(self.lb1,Qt.AlignHCenter)
        vwg.addWidget(self.jindu_btn)

        hFrame.setLayout(hwg)
        vFrame.setLayout(vwg)
        
        Worklayout.addWidget(hFrame)
        Worklayout.addWidget(vFrame)
        
        WorkFrame.setLayout(Worklayout)
        self.topright.addWidget(WorkFrame)
        
        
        #第三个,底部,串口通信框
        self.bottom = QFrame(self)
        self.bottom.setFrameShape(QFrame.StyledPanel)
        bwg=QHBoxLayout()
        bwg.addWidget(self.workmodule1)
        bwg.addWidget(self.workmodule2)
        bwg.addWidget(self.workmodule3)
        self.bottom.setLayout(bwg)
        self.bottom.setStyleSheet("#MainWindow{border-image:url(Icon/xinbo.png);}")


        #调用splitter控件,使窗口可以拖动起来
        splitter1 = QSplitter(Qt.Horizontal)
        splitter1.addWidget(self.topleft)
        splitter1.addWidget(self.topright)
        splitter1.setSizes([80,600])
        splitter2=QSplitter(Qt.Vertical)
        splitter2.addWidget(splitter1)
        splitter2.addWidget(self.bottom)
        splitter2.setSizes([800,200])
        self.GlobalLayout.addWidget(splitter2)
        #topright.setLayout(hbox)
        self.setLayout(self.GlobalLayout)
               

        self.setGeometry(300, 300, 800, 600)
        self.setWindowTitle('莘博医疗') 
        self.setWindowIcon(QIcon('Icon\senbo.jpg'))
        self.show()
    
    def cunchu_btn1_1(self):
        self.cunchu_btn1.setStyleSheet("QPushButton{color:black}"
                            "QPushButton:hover{color:red}"
                            "QPushButton{background-color:rgb(175,238,238)}"
                            "QPushButton{border:2px}"
                            "QPushButton{border-radius:10px}"
                            "QPushButton{padding:2px 4px}")

    
    
    
    def workmodule_31(self):
        print(self.step)
        #self.jindu_btn.setText('jiaocha')
        if self.step == 18 :
            #print('asdas')
            self.jindu_btn.setText('交叉配血')
            self.jindu_btn.setFont(QFont("微软雅黑",20,QFont.Bold))
        elif self.step == 40:
            self.jindu_btn.setText('孵育')
            self.jindu_btn.setFont(QFont("微软雅黑",20,QFont.Bold))
        elif self.step == 60:
            self.jindu_btn.setText('离心')
            self.jindu_btn.setFont(QFont("微软雅黑",20,QFont.Bold))
        elif self.step ==80:
            self.jindu_btn.setText('图像处理')
            self.jindu_btn.setFont(QFont("微软雅黑",20,QFont.Bold))
    
    
    def timerEvent(self, e):
        if self.step == 100:
            self.jindu_btn.setText('检测完毕')
            self.jindu_btn.setFont(QFont("微软雅黑",20,QFont.Bold))
            self.timer.stop()
            #return
        self.step = self.step+1
        self.workmodule_31()
        
        # print('jwhy')
        # if(int(self.step) >= 100):
        #     self.jindu_btn.setText('离心')
        #     print('jwhy')
        #     self.lb1.setText('djaoisdj')
        self.prsbar.setValue(self.step)

    def doAction(self, value):
        if self.timer.isActive():
            self.timer.stop()
        else:
            self.timer.start(700, self)
            self.jindu_btn.setText('离心')
            self.jindu_btn.setFont(QFont("微软雅黑",20,QFont.Bold))
    def closeEvent(self, event):
        reply = QMessageBox.question(self, '提示',
            "Are you sure to quit?", QMessageBox.Yes | 
            QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()


    def cunchu(self):
        self.topright.setCurrentIndex(0)
    def wendu(self):
        self.topright.setCurrentIndex(1)
    def work(self):
        self.topright.setCurrentIndex(2)



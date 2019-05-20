#生成折线图

import matplotlib 
matplotlib.use("QT5Agg")
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import numpy as np 


#创建一个matplotlib图形绘制类
class MyFigure(FigureCanvas):
    def __init__(self,width=1, height=1, dpi=100):
        #第一步：创建一个创建Figure
        self.fig = Figure(figsize=(width, height), dpi=dpi)
        #第二步：在父类中激活Figure窗口
        super(MyFigure,self).__init__(self.fig) #此句必不可少，否则不能显示图形
        #第三步：创建一个子图，用于绘制图形用，111表示子图编号，如matlab的subplot(1,1,1)
        #self.axes = self.fig.add_subplot(111)
    #第四步：就是画图，【可以在此类中画，也可以在其它类中画】
    def plotsin(self):
        self.axes0 = self.fig.add_subplot(111)
        # t = np.arange(0.0, 3.0, 0.01)
        # s = np.sin(2 * np.pi * t)
        # self.axes0.plot(t, s)

        x=(0,1,2,3,4,5,6,7,8)
        y1=(1,3,2,4,56,7,7,7,5)
        self.axes0.plot(x,y1)

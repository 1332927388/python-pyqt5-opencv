import serial
import serial.tools.list_ports
import re
port_list = list(serial.tools.list_ports.comports())
p1 = re.compile(r'[(](.*?)[)]', re.S)
if len(port_list) == 1:
    for i in range(0,len(port_list)):
        print(re.findall(p1,str(port_list[i]))[0])




# # coding=utf-8

# import sys
# from PyQt5.QtWidgets import *
# from PyQt5.QtCore import *
# from PyQt5.QtGui import *


# class Example(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.initUI()

#     def initUI(self):
#         hbox = QHBoxLayout(self)
#         left = QFrame(self)
#         # QFrame 控件添加StyledPanel样式能使QFrame 控件之间的界限更加明显
#         #left.setFrameShape(QFrame.StyledPanel)
#         right = QFrame(self)
#         #right.setFrameShape(QFrame.StyledPanel)
#         splitter1 = QSplitter(Qt.Horizontal)
#         splitter1.addWidget(left)
#         splitter1.setSizes([20,]) #设置分隔条位置
#         splitter1.addWidget(right)
#         hbox.addWidget(splitter1)
#         self.setLayout(hbox)


#         # 树
#         self.tree = QTreeWidget(left)
#         self.tree.setStyleSheet("background-color:#eeeeee;border:outset;color:#215b63;")
#         self.tree.setAutoScroll(True)
#         self.tree.setEditTriggers(QAbstractItemView.DoubleClicked | QAbstractItemView.EditKeyPressed)
#         self.tree.setTextElideMode(Qt.ElideMiddle)
#         #self.tree.setIndentation(30)
#         self.tree.setRootIsDecorated(True)
#         self.tree.setUniformRowHeights(False)
#         self.tree.setItemsExpandable(True)
#         self.tree.setAnimated(False)
#         self.tree.setHeaderHidden(True)
#         self.tree.setExpandsOnDoubleClick(True)
#         self.tree.setObjectName("tree")


#         # 设置根节点
#         root = QTreeWidgetItem(self.tree)
#         root.setText(0, '系统管理')
#         # 设置树形控件的列的宽度
#         #self.tree.setColumnWidth(0, 150)
#         # 设置子节点1
#         child1 = QTreeWidgetItem()
#         child1.setText(0, '增加人员信息')
#         root.addChild(child1)
#         # 设置子节点2
#         child2 = QTreeWidgetItem(root)
#         child2.setText(0, '查询人员信息')
#         # 加载根节点的所有属性与子控件
#         self.tree.addTopLevelItem(root)
#         # 设置stackedWidget
#         self.stackedWidget = QStackedWidget(right)

#         # 设置第一个面板
#         self.form1 = QWidget()
#         self.formLayout1 = QHBoxLayout(self.form1)
#         self.label1 = QLabel()
#         self.label1.setText("增加人员信息面板")
#         self.label1.setSizePolicy(QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding))
#         self.label1.setAlignment(Qt.AlignCenter)
#         self.label1.setFont(QFont("Roman times", 50, QFont.Bold))
#         self.formLayout1.addWidget(self.label1)

#         # 设置第二个面板
#         self.form2 = QWidget()
#         self.formLayout2 = QHBoxLayout(self.form2)
#         self.label2 = QLabel()
#         self.label2.setText("查询人员信息面板")
#         self.label2.setSizePolicy(QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding))
#         self.label2.setAlignment(Qt.AlignCenter)
#         self.label2.setFont(QFont("Roman times", 50, QFont.Bold))
#         self.formLayout2.addWidget(self.label2)

#         # 将两个面板，加入stackedWidget
#         self.stackedWidget.addWidget(self.form1)
#         self.stackedWidget.addWidget(self.form2)

#         # 树节点监听事件
#         self.tree.clicked.connect(self.onClicked)


#         # 窗口最大化
#         self.showMaximized()
#         self.setWindowTitle('树窗口分隔案列')
#         self.show()

#     def onClicked(self,qmodeLindex):
#         item=self.tree.currentItem()
#         print('Key=%s,value=%s'%(item.text(0),item.text(1)))
#         if item.text(0) == '增加人员信息':
#             self.on_pushButton1_clicked()
#         elif item.text(0) == '查询人员信息':
#             self.on_pushButton2_clicked()
#         else:
#             print('返回主界面')


#     # 按钮一：打开第一个面板
#     def on_pushButton1_clicked(self):
#         self.stackedWidget.setCurrentIndex(0)

#     # 按钮二：打开第二个面板
#     def on_pushButton2_clicked(self):
#         self.stackedWidget.setCurrentIndex(1)


# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     ex = Example()
#     sys.exit(app.exec_())


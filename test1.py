import sys
from PyQt5.QtWidgets import QMainWindow, QPushButton, QApplication
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt,QSize
 
 
class First(QMainWindow):
 
    def __init__(self):
        super().__init__()
 
        self.initUI()
 
    def initUI(self):
        self.btn = QPushButton("", self)
        self.btn.setFixedSize(60,60)
        self.btn.setIconSize(QSize(60,80))
        self.btn.setIcon(QIcon('Icon/meidui.jpg'))
        self.btn.move(30, 50) 
 
        self.setGeometry(300, 300, 500, 500)
        self.setWindowTitle('Event sender')
        self.show()
    
    

class Second(QMainWindow):
    def __init__(self):
        super().__init__()
 
        self.initUI()
 
    def initUI(self):
        self.setGeometry(300, 300, 290, 150)
        self.setWindowTitle('Get sender')
 
 
if __name__ == '__main__':
    app = QApplication(sys.argv)
    a = First()
    b = Second()
    a.show()
    a.btn.clicked.connect(b.show)
    sys.exit(app.exec_())
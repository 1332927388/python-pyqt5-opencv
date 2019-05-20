from UI import mywindow
import sys
from PyQt5 import QtWidgets
import serial














if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = mywindow()
    sys.exit(app.exec_())
from UI import mywindow
import sys
from PyQt5 import QtWidgets
import serial
from command import command

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = mywindow()
    cmd=command()
    print(cmd.getCommand())
    sys.exit(app.exec_())
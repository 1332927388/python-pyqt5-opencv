import sys
from PyQt5.QtCore import (Qt)
from PyQt5.QtWidgets import (QApplication, QComboBox, QDialog,
        QDialogButtonBox, QFrame, QGridLayout, QHBoxLayout, QLabel,
        QSpinBox, QStackedWidget, QVBoxLayout, QWidget)

class VehicleRentalDlg(QDialog):

    def __init__(self, parent=None):
        super(VehicleRentalDlg, self).__init__(parent)

        vehicleLabel = QLabel("&Vehicle Type:")
        self.vehicleComboBox = QComboBox()
        vehicleLabel.setBuddy(self.vehicleComboBox)
        self.vehicleComboBox.addItems(["Car", "Van"])
        colorLabel = QLabel("Co&lor:")
        self.colorComboBox = QComboBox()
        colorLabel.setBuddy(self.colorComboBox)
        self.colorComboBox.addItems(["Black", "Blue", "Green", "Red",
                                     "Silver", "White", "Yellow"])
        seatsLabel = QLabel("&Seats:")
        self.seatsSpinBox = QSpinBox()
        seatsLabel.setBuddy(self.seatsSpinBox)
        self.seatsSpinBox.setRange(2, 12)
        self.seatsSpinBox.setValue(4)
        self.seatsSpinBox.setAlignment(Qt.AlignRight|Qt.AlignVCenter)
        weightLabel = QLabel("&Weight:")
        self.weightSpinBox = QSpinBox()
        weightLabel.setBuddy(self.weightSpinBox)
        self.weightSpinBox.setRange(1, 8)
        self.weightSpinBox.setValue(1)
        self.weightSpinBox.setAlignment(Qt.AlignRight|Qt.AlignVCenter)
        self.weightSpinBox.setSuffix(" tons")
        volumeLabel = QLabel("Volu&me")
        self.volumeSpinBox = QSpinBox()
        volumeLabel.setBuddy(self.volumeSpinBox)
        self.volumeSpinBox.setRange(4, 22)
        self.volumeSpinBox.setValue(10)
        self.volumeSpinBox.setAlignment(Qt.AlignRight|Qt.AlignVCenter)
        self.volumeSpinBox.setSuffix(" cu m")
        mileageLabel = QLabel("Max. Mileage")
        self.mileageLabel = QLabel("1000 miles")
        self.mileageLabel.setAlignment(Qt.AlignRight|Qt.AlignVCenter)
        self.mileageLabel.setFrameStyle(QFrame.StyledPanel|QFrame.Sunken)
        self.buttonBox = QDialogButtonBox(QDialogButtonBox.Ok|
                                          QDialogButtonBox.Cancel)

        self.stackedWidget = QStackedWidget()
        carWidget = QWidget()
        carLayout = QGridLayout()
        carLayout.addWidget(colorLabel, 0, 0)
        carLayout.addWidget(self.colorComboBox, 0, 1)
        carLayout.addWidget(seatsLabel, 1, 0)
        carLayout.addWidget(self.seatsSpinBox, 1, 1)
        carWidget.setLayout(carLayout)
        self.stackedWidget.addWidget(carWidget)
        vanWidget = QWidget()
        vanLayout = QGridLayout()
        vanLayout.addWidget(weightLabel, 0, 0)
        vanLayout.addWidget(self.weightSpinBox, 0, 1)
        vanLayout.addWidget(volumeLabel, 1, 0)
        vanLayout.addWidget(self.volumeSpinBox, 1, 1)
        vanWidget.setLayout(vanLayout)
        self.stackedWidget.addWidget(vanWidget)

        topLayout = QHBoxLayout()
        topLayout.addWidget(vehicleLabel)
        topLayout.addWidget(self.vehicleComboBox)
        bottomLayout = QHBoxLayout()
        bottomLayout.addWidget(mileageLabel)
        bottomLayout.addWidget(self.mileageLabel)
        layout = QVBoxLayout()
        layout.addLayout(topLayout)
        layout.addWidget(self.stackedWidget)
        layout.addLayout(bottomLayout)
        layout.addWidget(self.buttonBox)
        self.setLayout(layout)


        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)
        self.vehicleComboBox.currentIndexChanged[str].connect(self.setWidgetStack)
        self.weightSpinBox.valueChanged[int].connect(self.weightChanged)

        self.setWindowTitle("Vehicle Rental")


    def setWidgetStack(self, text):
        if text == "Car":
            self.stackedWidget.setCurrentIndex(0)
            self.mileageLabel.setText("1000 miles")
        else:
            self.stackedWidget.setCurrentIndex(1)
            self.weightChanged(self.weightSpinBox.value())


    def weightChanged(self, amount):
        self.mileageLabel.setText("{0} miles".format(8000 / amount))


app = QApplication(sys.argv)
form = VehicleRentalDlg()
form.show()
app.exec_()
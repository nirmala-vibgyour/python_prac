from PyQt6.QtWidgets import QWidget, \
    QApplication, QGridLayout, QLineEdit, \
    QLabel, QPushButton, QComboBox
import sys


class SpeedCalculator(QWidget):
    def __init__(self):
        super().__init__()

        """ window name """
        self.setWindowTitle("Average Speed Calculator")

        """ creating class instance of QGridLayout """
        grid = QGridLayout()
        self.setLayout(grid)

        """ Distance button """
        distanceLabel = QLabel("Distance:")
        self.distanceInput = QLineEdit()
        grid.addWidget(distanceLabel, 0, 0)
        grid.addWidget(self.distanceInput, 0, 1)

        """ Options button """
        self.unitCombo = QComboBox()
        self.unitCombo.addItems(['Imperial (miles)', 'Metric (km)'])
        grid.addWidget(self.unitCombo, 0, 2)

        """ Time button """
        timeLabel = QLabel("Time(hours):")
        self.timeInput = QLineEdit()
        grid.addWidget(timeLabel, 1, 0)
        grid.addWidget(self.timeInput, 1, 1)

        """ Calculate push button """
        calculateButton = QPushButton("Calculate Speed")
        calculateButton.clicked.connect(self.speedCalculator)
        grid.addWidget(calculateButton, 2, 1)

        """ Output label button """
        self.outputLabel = QLabel("")
        grid.addWidget(self.outputLabel, 3, 0, 1, 2)

    def speedCalculator(self):
        if self.unitCombo.currentText() == 'Imperial (miles)':
            distance = (float(self.distanceInput.text())*0.621371)
            speed = distance/(float(self.timeInput.text()))
            speed = round(speed, 2)
            self.outputLabel.setText(f"Average speed is {speed} mph.")

        if self.unitCombo.currentText() == 'Metric (km)':
            speed = float(self.distanceInput.text())/float(self.timeInput.text())
            speed = round(speed, 2)
            self.outputLabel.setText(f"Average speed is {speed} km/h.")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    speed_calculator = SpeedCalculator()
    speed_calculator.show()
    sys.exit(app.exec())

# Imperial (miles)
# Metric (km)
# mph... km/h


import sys
from PyQt6 import QtWidgets

class demowind(QtWidgets.QWidget):
    
    def __init__(self, parent=None):
        
        super().__init__(parent)
        self.setGeometry(300, 300, 200, 200)
        self.setWindowTitle('Demo window')

        quit = QtWidgets.QPushButton('Quit', self)
        quit.setGeometry(10, 10, 70, 40)

        quit.clicked.connect(QtWidgets.QApplication.quit)



app = QtWidgets.QApplication(sys.argv)
dw = demowind()
dw.show()
sys.exit(app.exec())
import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QWidget

__version__ = '0.1'
__author__ = 'Abhishek Kumar Sisodiya'

#sublcass of QMainWindow to setup the calculator's GUI
class PyCalcUi(QMainWindow):
    #PyCalc's View (GUI)
    def __init__(self):
        #View initializer
        super().__init__()
        #main window's properties
        self.setWindowTitle('Calc v'+__version__)
        self.setFixedSize(235,235)
        #set central widget
        self._centralWidget = QWidget(self)
        self.setCentralWidget(self._centralWidget)

#Client code
def main():
    #instance of QApplication
    pycalc = QApplication(sys.argv)
    view = PyCalcUi() #show the calculator's GUI
    view.show()
    #Executes the calculator's main loop
    sys.exit(pycalc.exec_())

if __name__ == '__main__':
    main()

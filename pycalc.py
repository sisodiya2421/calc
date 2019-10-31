import sys
from functools import partial
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QGridLayout
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QVBoxLayout

__version__ = '0.1'
__author__ = 'Abhishek Kumar Sisodiya'
ERROR_MSG = "ERROR"


#sublcass of QMainWindow to setup the calculator's GUI
class PyCalcUi(QMainWindow):
    #PyCalc's View (GUI)
    def __init__(self):
        #View initializer
        super().__init__()
        #main window's properties
        self.setWindowTitle('Calc v'+__version__)
        self.setFixedSize(235,235)
        self.generalLayout = QVBoxLayout() #general Layout
        #set central widget
        self._centralWidget = QWidget(self)
        self.setCentralWidget(self._centralWidget)
        self._centralWidget.setLayout(self.generalLayout)
        #display and buttons
        self._createDisplay()
        self._createButtons()

    def _createDisplay(self):
        #display widget
        self.display = QLineEdit()
        #widget properties
        self.display.setFixedHeight(35)
        self.display.setAlignment(Qt.AlignRight)
        self.display.setReadOnly(True)
        #display added to genral layout
        self.generalLayout.addWidget(self.display)

    def _createButtons(self):
        self.buttons = {}
        buttonsLayout = QGridLayout()
        #Button text | position on the QGrid Layout
        buttons = {'7': (0, 0),
                   '8': (0, 1),
                   '9': (0, 2),
                   '/': (0, 3),
                   'C': (0, 4),
                   '4': (1, 0),
                   '5': (1, 1),
                   '6': (1, 2),
                   '*': (1, 3),
                   '(': (1, 4),
                   '1': (2, 0),
                   '2': (2, 1),
                   '3': (2, 2),
                   '-': (2, 3),
                   ')': (2, 4),
                   '0': (3, 0),
                   '00': (3, 1),
                   '.': (3, 2),
                   '+': (3, 3),
                   '=': (3, 4),
                   }
        for btnText, pos in buttons.items():
            self.buttons[btnText] = QPushButton(btnText)
            self.buttons[btnText].setFixedSize(40, 40)
            buttonsLayout.addWidget(self.buttons[btnText], pos[0], pos[1])
        #add buttonsLayout to general layout
        self.generalLayout.addLayout(buttonsLayout)

    def setDisplayText(self, text):
        self.display.setText(text)
        self.display.setFocus()

    def displayText(self):
        return self.display.text()

    def clearDisplay(self):
        self.setDisplayText('')

def evaluateExpression(expression):
    try:
        result = str(eval(expression, {}, {})) #work to be on later stage
    except Exception:
        result = ERROR_MSG

    return result

class PyCalcCntrl:
    def __init__(self, model, view):
        self._evaluate = model
        self._view = view #controller initializer
        self._connectSignals() #connects signals and slots
    
    def _calculateResult(self):
        result = self._evaluate(expression=self._view.displayText())
        self._view.setDisplayText(result)

    def _buildExpression(self, sub_exp):
        if self._view.displayText() == ERROR_MSG:
            self._view.clearDisplay()

        expression = self._view.displayText() + sub_exp
        self._view.setDisplayText(expression)

    def _connectSignals(self):
        for btnText, btn in self._view.buttons.items():
            if btnText not in {'=', 'C'}:
                btn.clicked.connect(partial(self._buildExpression, btnText))
        self._view.buttons['='].clicked.connect(self._calculateResult)
        self._view.display.returnPressed.connect(self._calculateResult)
        self._view.buttons['C'].clicked.connect(self._view.clearDisplay)
#Client code
def main():
    #instance of QApplication
    pycalc = QApplication(sys.argv)
    view = PyCalcUi() #show the calculator's GUI
    view.show()
    #instance of model and controller
    model = evaluateExpression
    PyCalcCntrl(model=model, view=view)
    #Executes the calculator's main loop
    sys.exit(pycalc.exec_())

if __name__ == '__main__':
    main()

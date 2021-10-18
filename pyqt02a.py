from PyQt5.QtWidgets import *

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        # Your code here
        
        '''Layout
        '''
        self.layout1 = QVBoxLayout()
        self.setLayout(self.layout1)

        self.layout2 = QHBoxLayout()
        self.label1 = QLabel('Enter x')
        self.lineEditX = QLineEdit()
        self.layout2.addWidget(self.label1)
        self.layout2.addWidget(self.lineEditX)
        self.layout1.addLayout(self.layout2)

        self.layout3 = QHBoxLayout()
        self.label2 = QLabel('Enter y')
        self.lineEditY = QLineEdit()
        self.layout3.addWidget(self.label2)
        self.layout3.addWidget(self.lineEditY)
        self.layout1.addLayout(self.layout3)

        
        '''Condition
        '''
        self.buttonAdd = QPushButton('Add')
        self.buttonAdd.clicked.connect(self.actionAdd)
        self.layout1.addWidget(self.buttonAdd)

        self.buttonSubtrac = QPushButton('Subtrac')
        self.buttonSubtrac.clicked.connect(self.actionSubtrac)
        self.layout1.addWidget(self.buttonSubtrac)

        self.buttonMultiply = QPushButton('Multiply')
        self.buttonMultiply.clicked.connect(self.actionMultiply)
        self.layout1.addWidget(self.buttonMultiply)

        self.buttonDivide = QPushButton('Divide')
        self.buttonDivide.clicked.connect(self.actionDivide)
        self.layout1.addWidget(self.buttonDivide)



        '''Settext
        '''
        self.layout4 = QHBoxLayout()
        self.label3 = QLabel('x+y = ')
        self.labelResult = QLabel()
        self.layout4.addWidget(self.label3)
        self.layout4.addWidget(self.labelResult)
        self.layout1.addLayout(self.layout4)

        

    ''' Methods
    '''
    def actionAdd(self):
        self.label3.setText('x+y =')
        x = int(self.lineEditX.text())
        y = int(self.lineEditY.text())
        z = x+y
        self.labelResult.setText(str(z))

    def actionSubtrac(self):
        self.label3.setText('x-y =')
        x = int(self.lineEditX.text())
        y = int(self.lineEditY.text())
        z = x-y
        self.labelResult.setText(str(z))

    def actionMultiply(self):
        self.label3.setText('x*y =')
        x = int(self.lineEditX.text())
        y = int(self.lineEditY.text())
        z = x*y
        self.labelResult.setText(str(z))\
    
    def actionDivide(self):
        self.label3.setText('x/y =')
        x = int(self.lineEditX.text())
        y = int(self.lineEditY.text())
        z = round((x/y), 2)
        self.labelResult.setText(str(z))


    


app = QApplication([])
myWindow = MyWindow()
myWindow.show()
app.exec()

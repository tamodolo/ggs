import sys
from PyQt5.QtWidgets import QLabel, QApplication, QTextEdit, QFileDialog, QAction, qApp, QMainWindow, QToolTip, QPushButton
from PyQt5.QtGui import QFont, QIcon
import random


data = str('texto')

class main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        QToolTip.setFont(QFont('SansSerif', 10))

        btn = QPushButton('Abrir Lista de Jogos', self)
        btn.setToolTip('Abra sua lista de jogos aqui')
        btn.resize(btn.sizeHint())
        btn.move(50,50)
        btn.clicked.connect(self.abrir)

        self.lbl1 = QLabel('Seu próximo jogo vai aparecer aqui',self)
        self.lbl1.resize(250,20)
        self.lbl1.move(200,50)

        self.setGeometry(300, 300, 500, 200)
        self.setWindowTitle('Escolhe Jogo')    
        self.show()


    def abrir(self):
        fname = QFileDialog.getOpenFileName(self, 'Abrir Lista', '.')
        f = open(fname[0])
        data = f.read().split("\n")
        pick = random.choice(data)
        self.lbl1.setText('Comece a jogar ' + str(pick))
        
            

        
app = QApplication(sys.argv)

ex = main()
    
sys.exit(app.exec_())

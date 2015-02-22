import sys
from PyQt5.QtWidgets import QLabel, QApplication, QTextEdit, QFileDialog, QAction, QActionGroup, qApp, QMainWindow, QToolTip, QPushButton
from PyQt5.QtGui import QFont, QIcon
import random
import gettext

#making gettext global, set folder and text code
t = gettext.install('ggs','./locale')

#set any extra language here (author will mantain only en and pt-br)
#english = gettext.translation('ggs', languages=['en'])
#brazilianportuguese = gettext.translation('ggs', languages=['pt-br'])


class ggs(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        #tooltip font
        QToolTip.setFont(QFont('SansSerif', 10))


        #button to open custom game list
        btn = QPushButton(_('Open File'), self)
        btn.setToolTip(_('Open your game list here'))
        btn.resize(btn.sizeHint())
        btn.move(50,50)
        btn.clicked.connect(self.openfile)

        #shows next game (very early and ugly)
        self.lbl1 = QLabel(_('Your next game will be showed here'),self)
        self.lbl1.resize(250,20)
        self.lbl1.move(200,50)

        #basic windows config (this must be set as the last in code order)
        self.setGeometry(300, 300, 500, 200)
        self.setWindowTitle('Generic Game Selector')    
        self.show()

    def openfile(self):  #open file and choose game
        fname = QFileDialog.getOpenFileName(self, _('Open List'), '.')
        f = open(fname[0])
        data = f.read().split("\n")
        pick = random.choice(data)
        self.lbl1.setText(_('Start to play ') + str(pick))
        


#some code to make things happen        
app = QApplication(sys.argv) #startup from shell
ex = ggs()
sys.exit(app.exec_()) #mainloop and clean exit

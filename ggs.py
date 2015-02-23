import sys
from PyQt5.QtWidgets import QLabel, QApplication, QTextEdit, QFileDialog, QAction, QActionGroup, qApp, QMainWindow, QToolTip, QPushButton
from PyQt5.QtGui import QFont, QIcon
import random
import gettext

#making gettext global, set folder and text code
gettext.install('ggs', localedir='locale', codeset='unicode')

#set any extra language here (author will mantain only en_US and pt_BR)
en_US = gettext.translation('ggs', languages=['en_US'], fallback=True)
pt_BR = gettext.translation('ggs', languages=['pt_BR'], fallback=True)


class ggs(QMainWindow):
    def __init__(self):
        super(ggs, self).__init__()
        self.initUI()

    def initUI(self):

        #tooltip font
        QToolTip.setFont(QFont('SansSerif', 10))

        #initial status bar status
        self.statusBar().showMessage(_('Ready'))

        self.createMenuActions()
        self.createMenus()

        #button to open custom game list
        btn = QPushButton(_('Open File'), self)
        btn.setToolTip(_('Open your game list here'))
        btn.setStatusTip(_('Open your game list here'))
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

    def createMenuActions(self):
        
        #language menu options must not be translated. Future language
        #may be added with the option text in the target language
        
        self.enLanguage = QAction('English', self, checkable=True,
                                  statusTip=_('set program language to English'))
        self.enLanguage.triggered.connect(self.selectLang('en_US'))
        self.pt_brLanguage = QAction('Português (Brasil)', self, checkable=True,
                                     statusTip=_('set program language to Brazilian Portuguese'))
        self.pt_brLanguage.triggered.connect(self.selectLang('pt_BR'))
        
        self.languageGroup = QActionGroup(self)
        self.languageGroup.addAction(self.enLanguage)
        self.languageGroup.addAction(self.pt_brLanguage)
        #must improve the default option to remember last language used
        self.enLanguage.setChecked(True)

    def selectLang(self, lang):
	#this is not working for some reason...
        print(lang)
        if lang == 'pt_BR':
            pt_BR.install()
        if lang == 'en_US':
            en_US.install()

    def createMenus(self):
        #Options struc
        self.optionsMenu = self.menuBar().addMenu(_('Options'))
        self.languageMenu = self.optionsMenu.addMenu(_('Language'))
        self.languageMenu.addAction(self.enLanguage)
        self.languageMenu.addAction(self.pt_brLanguage)
        
        
        


#some code to make things happen        
app = QApplication(sys.argv) #startup from shell
ex = ggs()
sys.exit(app.exec_()) #mainloop and clean exit

import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from desinger import *
import pyshorteners     #shortlınk
import pyperclip as p   #copy

#FUNCTİON
def Click():
    longlink=ui.Url.text()
    shortener=pyshorteners.Shortener()
    link=shortener.tinyurl.short(longlink)
    ui.shotUrl.setText(link)
    
def Copy():
    longlink=ui.Url.text()
    shortener=pyshorteners.Shortener()
    link=shortener.tinyurl.short(longlink)
    p.copy(link)
    

Uygulama=QApplication(sys.argv)
penAna=QMainWindow()
ui=Ui_MainWindow()
ui.setupUi(penAna)
penAna.show()

#COMMAND
ui.shorted.clicked.connect(Click)
ui.copy.clicked.connect(Copy)


sys.exit(Uygulama.exec_())
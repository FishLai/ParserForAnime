'''
Created on 2018年8月27日

@author: quan_
'''
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication

from Frame.interface import Ui_Form

class MainForm(QMainWindow):
    '''
    classdocs
    '''
    def __init__(self, parent=None):
        '''
        Constructor
        '''
        super(MainForm, self).__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        
if __name__ == '__main__':
    import sys
    
    app = QApplication(sys.argv)
    form = MainForm()
    form.show()
    sys.exit(app.exec_())


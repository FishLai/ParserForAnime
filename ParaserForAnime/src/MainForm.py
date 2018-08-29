'''
Created on 2018年8月27日

@author: FishLai
m_t, model of table;
'''
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication

from Frame.interface import Ui_Form
from PyQt5.Qt import QStandardItem

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
        ui = self.ui
        
        ui.Btn_Re.clicked.connect(self.refreshEvent)
        self.tableView_set()
    def tableView_set(self):
        self.model_tb = QtGui.QStandardItemModel()
        m_t = self.model_tb
        tb_h = ["Anime", "episode", "isDownload"]
        m_t.setHorizontalHeaderLabels(tb_h)
        table = self.ui.tableView
        table.setModel(m_t)
        
        
    def refreshEvent(self, event):
        print("hi")
        
if __name__ == '__main__':
    import sys
    
    app = QApplication(sys.argv)
    form = MainForm()
    form.show()
    sys.exit(app.exec_())


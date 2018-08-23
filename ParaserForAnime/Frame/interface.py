# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'interface.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setWindowModality(QtCore.Qt.ApplicationModal)
        Form.resize(481, 640)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setMinimumSize(QtCore.QSize(480, 640))
        Form.setMaximumSize(QtCore.QSize(1280, 1080))
        Form.setWindowTitle("")
        Form.setWindowOpacity(1.0)
        Form.setLayoutDirection(QtCore.Qt.LeftToRight)
        Form.setStyleSheet("Qt::FramelessWindowHint")
        self.Btn_Re = QtWidgets.QPushButton(Form)
        self.Btn_Re.setGeometry(QtCore.QRect(30, 60, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        font.setItalic(True)
        self.Btn_Re.setFont(font)
        self.Btn_Re.setObjectName("Btn_Re")
        self.Btn_dl = QtWidgets.QPushButton(Form)
        self.Btn_dl.setGeometry(QtCore.QRect(210, 560, 101, 41))
        self.Btn_dl.setStyleSheet("font: italic 12pt \"Comic Sans MS\";")
        self.Btn_dl.setFlat(False)
        self.Btn_dl.setObjectName("Btn_dl")
        self.Btn_Vlist = QtWidgets.QPushButton(Form)
        self.Btn_Vlist.setGeometry(QtCore.QRect(330, 560, 121, 41))
        self.Btn_Vlist.setStyleSheet("font: italic 12pt \"Comic Sans MS\";")
        self.Btn_Vlist.setObjectName("Btn_Vlist")
        self.tableView = QtWidgets.QTableView(Form)
        self.tableView.setGeometry(QtCore.QRect(10, 100, 461, 451))
        self.tableView.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.tableView.setObjectName("tableView")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(80, 20, 301, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setStyleSheet("font: italic 20pt \"Comic Sans MS\";\n"
"color:rgb(0, 170, 0);")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        self.Btn_Re.setText(_translate("Form", "Refresh"))
        self.Btn_dl.setText(_translate("Form", "Download"))
        self.Btn_Vlist.setText(_translate("Form", "PutInVedioList"))
        self.label.setText(_translate("Form", "Newest Anime"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())


import sys
from region import Shares, Regions
# from login import login
# import database
# from database import Session
from database import User, create_debug_engine, create_session
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QTableWidgetItem, QTableWidget
from Main_Window_UI import Ui_MainWindow
import os
import codecs

if os.name == 'nt':
    sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())

class ApplicationWindow(QMainWindow):
    def __init__(self):
        super(ApplicationWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.Button.pressed.connect(self.button)
        self.ui.comboBox.activated.connect(self.parametr)

    """It is function for working with Table(add all coluns and rows with their values)"""
    def button(self):
        self.parametr()
        self.table = self.ui.Table.clear()
        self.row = len(self.command)
        self.cols = len (self.command[0])
        self.table = self.ui.Table
        self.table.setColumnCount(self.cols)
        self.table.setRowCount(self.row)

        for i in range(len(self.b)):
            for j in range(len(self.b[i])):
                self.table.setItem(i , j, QTableWidgetItem(str(self.b[i][j])))

    def parametr(self):
        self.text = self.ui.comboBox.currentText()
        if self.text == "Share":
            self.command = self.choose_s()
        else:
            self.command = self.choose_r()
        return self.command
            
    def choose_s(self):
        self.user_id = "1"
        self.b = []
        self.Share = Shares(self.user_id)
        self.b.append(self.Share.shares(self.user_id))
        self.b.append(self.Share.documents(self.user_id))
        return self.b
    def choose_r(self):
        self.region_id = "1"
        self.b = []
        self.Region = Regions(self.region_id)
        self.b.append(self.Region.areas(self.region_id))
        self.b.append(self.Region.numbers(self.region_id))
        return self.b


if __name__ == '__main__':
    de = create_debug_engine(True)
    session = create_session(de)
    app = QApplication(sys.argv)
    w = ApplicationWindow()
    w.show()
    sys.exit(app.exec_())
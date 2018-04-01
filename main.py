import sys
from login import login
from PyQt5.QtWidgets import QApplication, QMainWindow
from main_window import Ui_MainWindow
import os
import codecs

if os.name == 'nt':
    sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())

def register(obj):
    models.SESSION.add(obj)


def commit():
    models.SESSION.commit()


def rollback():
    models.SESSION.rollback()


class ApplicationWindow(QMainWindow):
    def __init__(self):
        super(ApplicationWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
    def Connection(self, find_user):
        register(find_user)
        return print(print_session())



if __name__ == '__main__':
    # import pudb
    # pu.db
    app = QApplication(sys.argv)
    w = ApplicationWindow()
    w.show()
    app.exec_()

    de = create_debug_engine(True)
    create_session(de)
    commit()
    quit()
    del w
    del app

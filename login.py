import sys
from login_ui import Ui_Login
from PyQt5.QtWidgets import QWidget, QCheckBox, QApplication
from PyQt5.QtCore import Qt
from database import User, create_debug_engine, create_session, print_session
from sqlalchemy import select
import os
# def query_select(name_table):
# 	models.SESSION.query(name_table) 
class login(QWidget):
    
	def __init__(self):
		super(login,self).__init__()
		self.ui = Ui_Login()
		self.ui.setupUi(self)      
		self.ui.sign_in.pressed.connect(self.button)
	def button(self):
		self.login = self.ui.login.text()
		self.password = self.ui.password.text()
		self.find_user(self.login, self.password)
	def find_user(self, login, password):
		self.login = login
		self.password = password
		self.de = create_debug_engine(True)
		self.transaction = select([User.login, User.password]).\
		where(login == self.login).\
    	where(password == self.password)
		self.result = self.de.execute(self.transaction).fetchall()
		if (len(self.result) != 0):
			os.system("~/dacha/myprogramm/main.py")# think under this scrips
			print(2)
		else:
			print("invalid login or password")
		return print(1)
if __name__ == '__main__':
	# import pudb
	# pu.db

	app = QApplication(sys.argv)
	ex = login()
	ex.show()
	sys.exit(app.exec_())
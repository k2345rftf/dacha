from database import User, create_debug_engine, create_session



class Users:
	def __init__(self, login, password):
		self.login = login
		self.password = password
	def Query(self, login, password, param):
		self.b = []
		for self.smth in session.query(self.param).filter(User.login == self.login).filter(User.password == self.password):
			self.b.append(self.smth[0])
		return self.b		

	def id_user(self, login, password):
		self.param = User.id
		self.b = self.Query(self.login, self.password, self.param)
		if (len(self.b)!=0):
			self.user_id = self.b[0]
		else:
			self.user_id = print("This user is not found!!!")
		return self.user_id

	def member(self, login, password):
		self.memb = User.membership
		self.user_id = self.id_user(self.login, self.password)
		if self.user_id != 0:
			self.member = self.Query(self.login, self.password, self.memb)
		return self.member
	def privelege(self, login, password):
		self.param = User.privelege_id
		self.user_id = self.id_user(self.login, self.password)
		if self.user_id !=0:
			self.privelege = self.Query(self.login, self.password, self.param)
		return self.privelege

de = create_debug_engine(True)
session = create_session(de)
login = "admin1"
password = "1234561"
b = Users(login, password)
print(b.id_user(login, password))
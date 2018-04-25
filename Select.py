
from database import User, create_debug_engine, create_session


class Login:
	def __init__(self, login, password):
		self.login = login
		self.password = password


	def find_user(self, login, password):
		self.b = []
		for self.user_id in session.query(User.id).filter(User.login == self.login).filter(User.password == self.password):
			self.b.append(self.user_id)
		if (len(self.b) != 0):
			self.array = []
			self.a = []
			self.a.append(self.b[0][0])
			self.who_is_it = What_is_the_user(self.a)
			self.array.append(self.who_is_it.isMember(self.a))
			self.array.append(self.who_is_it.privel(self.a))
		else:
			self.array = print("invalid login or password")
		return print(self.array)

class What_is_the_user:
	def __init__(self, user_id):

		self.user_id = user_id

	def isMember(self, user_id):
		self.array = []
		self.user_id = user_id
		self.ismemb = session.query(User.membership).filter(User.id == self.user_id)
		for self.member in self.ismemb:
			self.array.append(self.member[0])
		if len(self.member) >0:
			self.a = 1
		else:
			self.a = 0
		return self.a	
	def  privel(self, user_id):
		self.user_id = user_id
		self.privelege = session.query(User.privelege).filter(User.id == self.user_id)
		self.a = self.privelege[0]
		return self.a

class Select(What_is_the_user):
	def __init__(self, login, password):
		self.login = login
		self.password = password
		self.user_id =Login.find_user(self, self.login, self.password)

		self.member = What_is_the_user.isMember(self.user_id)
		return print(self.member)

de = create_debug_engine(True)
session = create_session(de)
login = "admin"
password = "123456"
b = Login(login, password)
print(b.find_user(login, password))

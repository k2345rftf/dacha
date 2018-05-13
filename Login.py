from database import User, create_debug_engine, create_session

class  Login:
	"""docstring for  Login"""
	def __init__(self, login, password):
		self.password = password
		self.login = login

	def check_user(self):
		from database import User
		self.user = session.query(User.id).filter(User.login == self.login).filter(User.password == self.password).all()
		if len(self.user) == 0:
			return None
		else:
			return self.user[0]

		
class UserData(Login):
	def __init__(self, login, password):
		
		self.login = login
		self.password = password
		super().__init__(self.login, self.password)
		self.user = Login(self.login, self.password).check_user()
	

	def isNone(self, param):
		self.param = param
		return self.param

	def privelege(self):
		if self.isNone(self.user):
			self.privelege = session.query(User.privelege).filter(User.id == self.user)
		else:
			self.privelege = [None]
		return self.privelege[0]

	def member(self):
		if self.isNone(self.user):
			self.member = session.query(User.membership).filter(User.id == self.user)
		else:
			self.member = [None]
		return self.member[0]


de = create_debug_engine(True)
session = create_session(de)
a = AccountentAPI()
print(a.showService(None))
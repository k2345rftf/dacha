from database import User, create_debug_engine, create_session
from Accountent import AccountentAPI
from Casher import CasherAPI
from Gardener import GardenerAPI
from Login import UserData


class WhoIsIt(UserData):
	def __init__(self, login, password):
		self.login = login
		self.password = password
		super().__init__(self.login, self.password)
	
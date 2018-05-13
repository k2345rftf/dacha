from database import create_debug_engine, create_session


class ShowUserRegion:
	def __init__(self, user_id):
		self.user_id = user_id


	def region_id(self):
		from database import Share
		self.b =[]
		for self.user in session.query(Share.region_id).filter(Share.user_id == self.user_id):
			self.b.append(str(self.user[0]))
		return self.b 

	def show(self):
		from database import Share, Region
		self.b = []
		self.reg = self.region_id()
		for self.i in range(len(self.reg)):

			self.data = session.query(Region.number_region, Share.share).filter(Region.region_id == Share.region_id).\
																		filter(Share.region_id == self.reg[self.i]).add()
			self.b.append(self.data)
		return self.b




class ShowHistoryPayment:

	def __init__(self, user_id):
		self.user_id = user_id

	def show_all(self):
		from database import Transactions
		self.b =[]
		self.j = 0
		for self.a in session.query(Transactions.date,
									Transactions.name_serv,
									Transactions.cost_unit,
									Transactions.cost,
									Transactions.payment,
									Transactions.overpayments,
									Transactions.total).filter_by(id_user = self.user_id):
			self.b.append([])

			for self.i in range(len(self.a)):
				self.b[self.j].append(self.a[self.i-1])
			self.j=self.j+1
		return self.b

	def show_area(self, date):
		from database import Transactions
		import datetime
		self.date = date
		self.b =[]
		self.j = 0
		for self.a in session.query(Transactions.date,
									Transactions.name_serv,
									Transactions.cost_unit,
									Transactions.cost,
									Transactions.payment,
									Transactions.overpayments,
									Transactions.total).filter_by(id_user = self.user_id).filter(Transactions.date >= self.date[0]).filter(Transactions.date <= self.date[1]):
			self.b.append([])

			for self.i in range(len(self.a)):
				self.b[self.j].append(self.a[self.i-1])
			self.j=self.j+1
		return self.b



class Gardener_work:
	def __init__(self, user_id):
		self.user_id = user_id

	def ChangePassword(self, password):
		from database import User
		self.password = password
		return session.query(User).filter(User.id == self.user_id).update({"password" : self.password})


	def insert_counter(self, value, name_serv):

		import datetime
		from database import CounterUnit, Counter, select_obj
		
		self.name_serv = name_serv
		self.c = select_obj(CounterUnit.classAccur,CounterUnit.user_id, self.user_id, None, None)
		if len(self.c) == 0:
			return "You have not qot a counter!!!!!"
		else:
			self.value = value
			self.id_counter = select_obj(Counter.id_counter,Counter.user_id, self.user_id, None, None)
			if len(self.id_counter) == 0:
				self.id_counter.append(0)

			self.b = Counter(	date = datetime.datetime.now(),
								id_counter = self.id_counter,
						        user_id = self.user_id,
						        name_counter = self.name_serv,
						        value = float(self.value.replace(",",".")))
			return self.b

	def addCounter(self, typeCounter, classAccur):
		from database import CounterUnit
		import datetime 
		self.typeCounter = typeCounter
		self.classAccur = classAccur
		self.r = session.query(CounterUnit.number).filter(CounterUnit.user_id == self.user_id).all()
		self.numb = self.r[len(self.r)-1][0]

		self.b = CounterUnit(
			number = self.numb+1,
        	user_id = self.user_id,
        	dateUnstCount = datetime.datetime.now(),
        	typeCounter = self.typeCounter,
        	classAccur = float(self.classAccur.replace(",",".")))
		return session.add(self.b)

class GardenerAPI(ShowUserRegion, ShowHistoryPayment, Gardener_work):
	def __init__(self, user_id):
		self.user_id = user_id
		super().__init__(self.user_id)

	def showHistory(self, date):
		from database import isNone
		self.date = date
		if isNone(self.date):
			return ShowHistoryPayment().show_area(self.date)
		else:
			return ShowHistoryPayment().show_all()

	def showShare(self):
		return ShowUserRegion(self.user_id).show()

	def insertCounter(self, value, name_serv):
		self.value = value
		self.name_serv = name_serv
		return Gardener_work(self.user_id).insert_counter(self.value, self.name_serv)

	def insCountUnit(self,typeCounter, classAccur):
		self.classAccur = classAccur
		self.typeCounter = typeCounter
		return Gardener_work(self.user_id).addCounter(self.typeCounter, self.classAccur)

	def changePass(self, password):
		self.password = password
		return Gardener_work(self.user_id).ChangePassword(self.password)		

de = create_debug_engine(True)
session = create_session(de)
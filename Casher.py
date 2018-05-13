from database import create_debug_engine, create_session




class GardenerPayment:





	def periods(self, name_service):
		from database import Service, select_obj
		self.name_service = name_service
		self.date = select_obj(Service.date, Service.name_service, self.name_service, None, None)
		if len(self.date) != 0:
			self.period = select_obj(Service.period, Service.name_service, self.name_service, Service.date, self.date[len(self.date)-1])
			self.value = self.period[0]
		else:
			self.value = 0
		
		return self.value



	def read_counter(self,user_id, name_serv, norm_value):
		from database import Counter, CounterUnit, select_obj
		self.user_id = user_id
		self.norm_value = norm_value
		self.name_serv = name_serv
		self.counter = select_obj(CounterUnit.classAccur, Counter.user_id, self.user_id, None, None)
		if len(self.counter) == 0:
			self.b = float(self.norm_value.replace(",","."))
		else:
			self.b = []
			for self.data in session.query(Counter.date, Counter.value).filter(Counter.user_id == self.user_id).\
																		filter(Counter.name_counter == self.name_serv):
				self.b.append([])
				for self.i in range(2):
					self.b[self.i].append(self.data[len(self.data)-1 - self.i][0])
					self.b[self.i].append(self.data[len(self.data)-1 - self.i][1])
					


		return self.b

	def recalc_cost(self,user_id, name_serv, norm_value):
		from database import Service, select_obj
		self.norm_value = norm_value
		self.user_id = user_id
		self.name_serv = name_serv
		self.count = self.read_counter(self.user_id, self.name_serv, self.norm_value)
		self.date = select_obj(Service.date, Service.name_service, self.name_serv, None, None)
		self.periodq = self.periods(self.name_serv)
		if len(self.date) ==0:
			self.cost = 0
		else:
			self.cost1 = select_obj(Service.cost_unit, Service.name_service, self.name_serv, Service.date, self.date[len(self.date)-1])
			self.cost = float(self.cost1[0])
		if (type(self.count) == float):
			self.value = self.count * self.cost
		else:
			if (self.periodq - (datetime.datetime.timestamp(self.count[0][0]) - datetime.datetime.timestamp(self.count[1][0]))) == 0:
				self.value = (self.count[0][1] - self.count[1][1]) * self.cost
			else:
				self.r = (datetime.datetime.timestamp(self.count[0][0]) - datetime.datetime.timestamp(self.count[1][0]))
				self.value = (self.periodq - self.r) * float(self.norm_value.replace(",",".")) + self.r * self.cost
		return self.value


	def overpayment(self,user_id, payment, name_serv, norm_value):
		from database import Transactions, select_obj
		self.user_id = user_id
		self.norm_value = norm_value
		self.name_serv = name_serv
		self.payment = payment
		self.cost = self.recalc_cost(self.user_id, self.name_serv, self.norm_value)
		self.trans = session.query(Transactions.total).filter(Transactions.id_user == self.user_id).filter(Transactions.name_serv == self.name_serv).all()
		if len(self.trans) != 0:
			self.total = self.trans[len(self.trans)-1][0]
		else:
			self.total = 0 
		self.value = self.total + self.payment
		return self.value



	def insert_trans(self,user_id, name_serv, payment, norm_value):
		from database import Service, Transactions, select_obj
		import datetime
		self.user_id = user_id
		self.norm_value = norm_value
		self.name_serv = name_serv
		self.payment = float(payment.replace(",","."))
		self.data = select_obj(Service.cost_unit, Service.name_service, self.name_serv, None, None)
		if len(self.data)== 0:
			self.unit = 1
		else:
			self.unit = self.data[len(self.data)-1]
		self.id_transaction = select_obj(Transactions.id_transaction,Transactions.id_user, self.user_id, None, None)
		if len(self.id_transaction) == 0:
			self.id_transaction.append(0)
		self.cost = self.recalc_cost(self.user_id, self.name_serv, self.norm_value)
		self.payment = self.payment
		self.overpayments = self.overpayment(self.user_id, self.payment, self.name_serv, self.norm_value)
		self.cost_unit = self.unit
		self.total = self.payment + self.overpayments


		self.b = Transactions(
							id_transaction = int(self.id_transaction[len(self.id_transaction)-1]) + 1,
					        id_user = self.user_id,
					        date = datetime.datetime.now(),
					        name_serv = self.name_serv,
					        cost_unit = self.cost_unit,
					        cost = self.cost,
					        payment = self.payment,
					        overpayments = self.overpayments,
					        total = self.total)
		return session.add(self.b)


class CompanyPayment:

	def __init__(self, id):
		self.ide = int(id)



	def insert_trans(self,user_id, name_serv, payment):
		from database import Company, User, isNone
		import datetime
		self.user_id = user_id
		self.a = session.query(Company.id_transaction).all()
		if len(self.a) == 0:
			self.id_tr = -1
		else:
			self.id_tr = self.a[len(self.a)-1]

		
		
		self.name_serv = name_serv
		self.payments = float(payment.replace(",","."))


		self.b = Company(
						id_transaction = int(self.id_tr+1),
					    date = datetime.datetime.now(),
					    id_creditor = int(self.user_id),
					    name_service = self.name_serv,
					    cost = self.payments,
					    id_deb = self.ide)
		return session.add(self.b)


class ShowHistoryPaymentC:

	def dates(self, param):
		import datetime
		self.param = param.split(".")
		return datetime.datetime(int(self.param[2]), int(self.param[1]), int(self.param[0]))

	def show_all(self):
		from database import Company, User
		self.b =[]
		self.j = 0
		for self.a in session.query(Company.date,
									User.NFC,
									Company.name_service,
									Company.cost).filter(User.id == Company.id_creditor):
			self.b.append([])

			for self.i in range(len(self.a)):
				self.b[self.j].append(self.a[self.i-1])
			self.j=self.j+1
		return self.b

	def show_area(self, date):
		from database import Company, User
		self.date = date
		self.b =[]
		self.j = 0
		for self.a in session.query(Company.date,
									User.NFC,
									Company.name_service,
									Company.cost).filter(User.id == Company.id_creditor).\
												filter(Company.date >= self.dates(self.date[0])).filter(Company.date <= self.dates(self.date[1])):
			self.b.append([])

			for self.i in range(len(self.a)):
				self.b[self.j].append(self.a[self.i-1])
			self.j=self.j+1
		return self.b



class CasherAPI(ShowHistoryPaymentC, CompanyPayment, GardenerPayment):
	
	def __init__(self, user_id):
		self.user_id = user_id
		super().__init__(self.user_id)

	def showHistory(self, date):
		from database import isNone
		self.date = date
		if isNone(self.date):
			return ShowHistoryPaymentC().show_area(self.date)
		else:
			return ShowHistoryPaymentC().show_all()

	def companyPay(self, id, name_serv, payment):
		self.uid = int(id)
		self.name_serv = name_serv
		self.payment = payment
		return CompanyPayment(self.user_id).insert_trans(self.uid, self.name_serv, self.payment)

	def gardenerPay(self,uid, name_serv, payment, norm_value):
		self.uid = uid
		self.name_serv = name_serv
		self.payment = payment
		self.norm_value = norm_value
		return GardenerPayment().insert_trans(self.uid, self.name_serv, self.payment, self.norm_value)


de = create_debug_engine(True)
session = create_session(de)

from database import User, Counter, CounterUnit, Service, Transactions, Company, create_debug_engine, create_session, select_obj
import datetime
from Interface import IShowHistory
import zope.interface



class GardenerPayment:

	def __init__(self, user_id, norm_value):
		self.user_id = user_id
		self.norm_value = norm_value




	def periods(self, name_service):
		self.name_service = name_service
		self.date = select_obj(Service.date, Service.name_service, self.name_service, None, None)
		if len(self.date) != 0:
			self.period = select_obj(Service.period, Service.name_service, self.name_service, Service.date, self.date[len(self.date)-1])
			self.value = self.period[0]
		else:
			self.value = 0
		
		return self.value



	def read_counter(self, name_serv, norm_value):
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

	def recalc_cost(self, name_serv):

		self.name_serv = name_serv
		self.count = self.read_counter(self.name_serv, self.norm_value)
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


	def overpayment(self, payment, name_serv):
		self.name_serv = name_serv
		self.payment = payment
		self.overp = []

		self.date = select_obj(Transactions.date,Transactions.id_user, self.user_id, Transactions.name_serv, self.name_serv)
		
		self.per = self.periods(self.name_serv)


		if len(self.date) == 0:
			self.t = datetime.datetime(1970, 1, 1)
			self.overp = 0
			self.p = [datetime.datetime(1970, 1, 1)]
		else:
			self.t = self.date[len(self.date)-1]
			self.o = session.query(Transactions.total).filter(Transactions.date == self.date[len(self.date)-1]).\
															filter(Transactions.id_user == self.user_id).\
															filter(Transactions.name_serv == self.name_serv).all()
			self.overp = self.o[0]
			self.date_get = session.query(Service.date_get).filter(Service.date == self.t).all()			
			self.p = select_obj(Service.date,Service.name_service, self.name_serv, Service.date_get, self.date_get[len(self.date_get)-1][0])	

		# print((datetime.datetime.today() - self.p[0]))
		if int(datetime.datetime.timestamp(datetime.datetime.today()) - datetime.datetime.timestamp(self.p[0])) <= self.per*86400: 
			self.value = self.payment + self.overp
		else:
			self.value = self.payment - self.recalc_cost(self.name_serv) + self.overp
		return self.value



	def insert_trans(self, name_serv, payment):
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
		self.cost = self.recalc_cost(self.name_serv)
		self.payment = self.payment
		self.overpayments = self.overpayment(self.payment, self.name_serv)
		self.cost_unit = self.unit
		self.total = self.cost - (self.payment + self.overpayments)


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


	def insert_trans(self,user_id, name_serv, payment):
		self.user_id = user_id
		for self.a in session.query(Company.id_transaction):
			self.e = self.a[len(self.a)-1]
		if self.e !=0:
			self.id_tr = self.e
		else:
			self.id_tr = 1
		self.name_serv = name_serv
		self.payments = float(payment.replace(",","."))
		self.id_debs = select_obj(User.id, User.privelege, 1, None, None)
		if len(self.id_debs) == 0:
			self.ide = 0
		else:
			self.ide = self.id_debs[0]

		self.b = Company(
						id_transaction = int(self.id_tr+1),
					    date = datetime.datetime.now(),
					    id_creditor = int(self.user_id),
					    name_service = self.name_serv,
					    cost = self.payments,
					    id_deb = self.ide)
		return session.add(self.b)


class ShowHistoryPaymentC:
	zope.interface.implementedBy(IShowHistory)

	def show_all(self):
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
		self.date = date
		self.b =[]
		self.j = 0
		for self.a in session.query(Company.date,
									User.NFC,
									Company.name_service,
									Company.cost).filter(User.id == Company.id_creditor).\
												filter(Company.date >= self.date[0]).filter(Company.date <= self.date[1]):
			self.b.append([])

			for self.i in range(len(self.a)):
				self.b[self.j].append(self.a[self.i-1])
			self.j=self.j+1
		return self.b



de = create_debug_engine(True)
session = create_session(de)

s = GardenerPayment("1", "14")
s.insert_trans("name", "100")
session.commit()
print(s.insert_trans("name", "100"))




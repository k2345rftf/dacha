from database import User, Counter, Service, Transactions, create_debug_engine, create_session, select_obj




class WorkWithGardener:

	def __init__(self, user_id):
		self.user_id = user_id





	def period(self, name_service):
		self.name_service = name_service
		self.date = select_obj(Service.date, Service.name_service, self.name_service)
		self.period = select_obj(Service.period, Service.name_service, self.name_service, Service.date, self.date[len(self.date)-1])
		return datetime.strptime(self.period, "%d")

	def payment(self, name_serv, payment):
		self.payment = payment
		self.name_serv = name_serv
		self.date = select_obj(Transactions.id_transaction, Transactions.name_serv, self.name_serv, None, None)
		self.trans = session.query(Transactions).filter(Transactions.id_user == self.user_id).filter(Transactions.name_serv == self.name_serv).\
																							filter(Transactions.date == self.date[len(self.date)-1]).one()
		self.trans.payment = float(self.payment.replace(",","."))
		return self.trans




	def read_counter(self, name_serv, norm_value):
		self.value = norm_value
		self.name_serv = name_serv
		self.counter = select_obj(CounterUnit.classAccur, Counter.user_id, self.user_id)
		if len(self.counter) == 0:
			self.b = self.value
		else:
			self.b = []
			for self.data in session.query(Counter.date, Counter.value).filter(Counter.user_id == self.user_id).\
																		filter(Counter.name_counter == self.name_serv):
				self.b.append([])
				for self.i in range(2):
					self.b[self.i].append(self.data[len(self.data)-1 - self.i][0])
					self.b[self.i].append(self.data[len(self.data)-1 - self.i][1])


		return self.b

	# def recalc_cost(self, name_serv):
	# 	self.name_serv = name_serv
	# 	self.count = self.read_counter(self.name_serv)
	# 	if self.period(self.name_serv) != (self.count[0][0]-self.count[1][0]) and (len(self.count)>= 2):
	# 		self.value = self.



	def overpayment(self):
		self.value = self.payment() - self.recalc_cost()
		return self.value

	def insert_trans(self):
		self.id_transaction = self.select_obj(Transactions.id_transaction,Transactions.id_user, self.user_id, None, None)
		if len(self.id_transaction) == 0:
			self.id_transaction.append(0)
		self.cost = self.recalc_cost()
		self.payment = self.payment()
		self.overpayments = self.overpayment()
		self.cost_unit = self.read_counter()/float(self.unit.replace(",", "."))
		self.total = self.payment - self.cost


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
		return self.b




de = create_debug_engine(True)
session = create_session(de)
a = WorkWithGardener("1")
# session.add(a.insert_trans())
# session.commit()
print(a.payment("name", "100"))






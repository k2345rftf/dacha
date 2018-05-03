from database import Share, Region, Counter, Transactions, Service, create_debug_engine, create_session, select_obj
from Interface import IRegion
import zope.interface
import datetime
from Interface import IShowHistory
import zope.interface




class ShowUserRegion:
	# zope.interface.implementedBy(IRegion)
	def __init__(self, user_id):
		self.user_id = user_id


	def __region_id(self):
		self.b =[]
		for self.user in session.query(Share.region_id).filter(Share.user_id == self.user_id):
			self.b.append(str(self.user[0]))
		return self.b 

	def area_shares(self):
		self.region_id = self.__region_id(self.user_id)
		if len(self.region_id) == 0:
			raise User_id_Error("please, sign in using valide login or password, and try again!!") 
		else:
			self.b =[]
			for self.j in range(len(self.region_id)):
				for self.num in session.query(Region.number_region, Share.share).filter(Share.region_id == self.region_id[self.j]).\
																				filter(Region.region_id == Share.region_id):
					
					self.a =[]
					for self.i in range(len(self.num)):
						self.a.append(self.num[self.i])
						
					self.b.append(self.a)
			return self.b

	def documentation(self):
		self.region_id = self.__region_id(self.user_id)
		if len(self.region_id) == 0:
			raise User_id_Error("please, sign in using valide login or password, and try again!!") 
		else:
			return 0

	def area(self):
		self.areas = self.area_shares(self.user_id)
		self.k = 1
		self.j = len(self.areas[0])
		self.k = 0
		for self.i in range(len(self.areas)):
			self.k = self.k + float(self.areas[self.i][self.j-1].replace(",", "."))

		return self.k



class ShowHistoryPayment:
	zope.interface.implementedBy(IShowHistory)

	def __init__(self, user_id):
		self.user_id = user_id

	def show_all(self):
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
	def __init__(self, user_id, name_serv):
		self.user_id = user_id
		self.name_serv = name_serv

	def ChangePassword(self):
		pass

	def insert_counter(self, value):
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
						        value = self.value)
			return self.b




de = create_debug_engine(True)
session = create_session(de)
a = ShowHistoryPayment("1")
date = [datetime.datetime(2018, 4, 20), datetime.datetime(2018, 4, 21)]
# session.add(a.insert_trans())
# session.commit()
print(a.show_all())
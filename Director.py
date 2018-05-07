from database import User, Share, Region, Company, Transactions, Service, Counter, create_debug_engine, create_session, select_obj, Inventory
import zope.interface
from Interface import IShowHistory
import datetime




class Companies:
	zope.interface.implementedBy(IShowHistory)
	def __init__(self, date):
		self.date = date

	def show_all(self):
		self.b = []
		for self.data in session.query(Company.date,
									  User.NFC,
									  Company.name_service,
									  Company.cost).filter(User.id == Company.id_creditor):
			self.b.append(self.data)
		return self.b

	def  show_area(self):
		self.c = []
		for self.data in session.query(Company.date,
                                       User.NFC,
                                       Company.name_service,
                                       Company.cost).filter(Company.date >= self.date[0]).filter(Company.date <= self.date[1]).filter(User.id == Company.id_creditor):
			self.c.append(self.data)
		return self.c
		
class Counters:
	def __init__(self, reading, name_counter):
		self.name_counter = name_counter
		self.reading = reading


	def input_count(self):
		self.h = []
		for self.data in session.query(Counter.id_counter):
			self.h.append(self.data)
			print("UUUUUUUUUUUUUUU")
		self.d = Counter(
			date = datetime.datetime.now(),
			id_counter = self.h[len(self.h) - 1][0] + 1,
			user_id = 1,
			name_counter = self.name_counter,
			value = int(self.reading))
		return session.add(self.d)








de = create_debug_engine(True)
session = create_session(de)
date =[datetime.datetime(2017,3,12),datetime.datetime(2019,4,26)]
a = Counters("1","name")
a.input_count()
session.commit()
print(1)




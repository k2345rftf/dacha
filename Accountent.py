from database import User, Counter, CounterUnit, Service, Transactions, Company, create_debug_engine, create_session, select_obj
import datetime


class InsertService:
	def __init__(self, name_service, doc_serv, date_get, period, cost_unit, unit, peny_data, peny):
		self.name_services = name_service
		self.doc_servs = doc_serv
		self.date_gets = date_get
		self.periods = period
		self.cost_units = cost_unit
		self.units = unit
		self.peny_dates = peny_data
		self.penys = peny



	def __date(self, param):
		self.param = param
		self.a = self.param.split(".")
		return datetime.datetime(int(self.a[2]), int(self.a[1]), int(self.a[0]), 0, 0, 0, 0)
	def insert_serv(self):

		self.ids = select_obj(Service.id, Service.name_service, self.name_services, None, None)
		if len(self.ids) != 0:
			self.ids1 = self.ids[len(self.ids)-1]
		else:
			self.ids1 = -1
		self.b = Service(id = self.ids1+1,
						 date = datetime.datetime.now(),
					     name_service = self.name_services,
					     doc_serv = self.doc_servs,
					     date_get = self.__date(self.date_gets),
					     period = int(self.periods),
					     cost_unit = float(self.cost_units.replace(",",".")),
					     unit = self.units,
					     peny_data = self.__date(self.peny_dates),
					     peny = int(self.penys))
		return session.add(self.b)







de = create_debug_engine(True)
session = create_session(de)
a = InsertService("name", "asd2", "20.12.2012", "30", "345,5","rg", "20.12.2017", "1")
a.insert_serv()
session.commit()
print(1)
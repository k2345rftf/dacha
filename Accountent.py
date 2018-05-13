from database import create_debug_engine, create_session

class InsertService:

	def __date(self, param):
		self.param = param
		self.a = self.param.split(".")
		return datetime.datetime(int(self.a[2]), int(self.a[1]), int(self.a[0]), 0, 0, 0, 0)
	def insert_serv(self, name_service, doc_serv, date_get, period, cost_unit, unit, peny_data, peny):
		from database import User, Service, select_obj
		import datetime
		self.name_services = name_service
		self.doc_servs = doc_serv
		self.date_gets = date_get
		self.periods = period
		self.cost_units = cost_unit
		self.units = unit
		self.peny_dates = peny_data
		self.penys = peny
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

class ShowService:
	
	def show_all(self):
		from database import Service
		import datetime
		self.b = session.query( Servise.date,
							    Servise.name_service,
							    Service.doc_serv,
							    Service.period,
							    Service.date_get,
							    Service.cost_unit,
							    Service.unit,
							    Service.peny_date,
							    Service.peny).all()		
		return self.b

	def show_area(self, date):
		from database import Service
		import datetime		
		self.date = date
		self.b = session.query( Servise.date,
							    Servise.name_service,
							    Service.doc_serv,
							    Service.period,
							    Service.date_get,
							    Service.cost_unit,
							    Service.unit,
							    Service.peny_date,
							    Service.peny).filter(Service.date >= self.date[0]).filter(Service.date <=self.date[1]).all()					
		return self.b


class ShowCompany:
	
	def dates(self, param):
		import datetime
		self.param = param.split(".")
		return datetime.datetime(int(self.param[2]), int(self.param[1]), int(self.param[0]))

	
	def show_all(self):
		from database import User, Company
		self.b = session.query( Company.date,
							    User.NFC,
							    Company.name_service,
							    Company.cost).filter(User.id == Company.id_creditor).all()		
		return self.b

	def show_area(self, date):
		from database import User, Company
		self.date = date
		self.b = session.query( Company.date,
							    User.NFC,
							    Company.name_service,
							    Company.cost).filter(User.id == Company.id_creditor).filter(Company.date >= self.dates(self.date[0])).filter(Company.date <=self.dates(self.date[1])).all()					
		return self.b


class AccountentAPI(ShowCompany, ShowService, InsertService):
	
	def __init__(self):
		
		super().__init__()
		



	def showCompany(self, date):
		from database import isNone
		self.date = date
		if isNone(self.date):
			return ShowCompany().show_area(self.date)
		else:
			return ShowCompany().show_all()

	def showService(self, date):
		from database import isNone
		self.date = date
		if isNone(self.date): 
			return ShowCompany().show_area(self.date)
		else:
			return ShowCompany().show_all()


	def insert_service(self, name_service, doc_serv, date_get, period, cost_unit, unit, peny_date, peny):	
		self.name_services = name_service
		self.doc_servs = doc_serv
		self.date_gets = date_get
		self.periods = period
		self.cost_units = cost_unit
		self.units = unit
		self.peny_dates = peny_date
		self.penies = peny
		return InsertService().insert_serv(self.name_services, self.doc_servs, self.date_gets, self.periods, self.cost_units, 
									self.peny_dates, self.penies)

de = create_debug_engine(True)
session = create_session(de)


from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, Float, Numeric, Date, Enum
from sqlalchemy import ForeignKey
from sqlalchemy.orm import sessionmaker

# SESSION = None
# ENGINE = None
Base = declarative_base()

BASE = Base






# 0 - gardener
# 1 - casher
# 2 - accountent
# 3 - director
# 4 - hired worker


class User(Base):
    """table of authorization"""
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)

    login = Column(String(20))
    password = Column(String(20))
    NFC = Column(String)
    membership = Column(Integer)
    privelege = Column(Integer)
    counter = Column(Integer)


    def __init__(self, id, login, password, membership, privelege):
        self.id = id

        self.login = login
        self.password = password
        self.NFC = NFC
        self.membership = membership
        self.privelege = privelege
        self.counter = counter
    

    def __repr__(self):
        return "<{}(id = {}, login = {}, password = {}, NFC={}, membership = {}, privelege = {}, counter = {}".format(self.__class__,
                                                                                                                        self.id, 
                                                                                                                        self.login, 
                                                                                                                        self.password, 
                                                                                                                        self.NFC, 
                                                                                                                        self.membership, 
                                                                                                                        self.privelege,
                                                                                                                        self.counter)


class CounterUnit(Base):
    __tablename__ = "Counters"
    number = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("user.id"))
    dateUnstCount = Column(Date)
    typeCounter = Column(String)
    classAccur = Column(Float)


    def __init(self, number, user_id, dateUnstCount, typeCounter, classAccur):
        self.number = number
        self.user_id = user_id
        self.dateUnstCount = dateUnstCount
        self.typeCounter = typeCounter
        self.classAccur = classAccur

    def __repr__(self):
        return "<{}(number = {}, user_id = {}, dateUnstCount = {}, typeCounter = {}, classAccur = {}". format(  self.number,
                                                                                                                self.user_id,
                                                                                                                self.dateUnstCount,
                                                                                                                self.typeCounter,
                                                                                                                self.classAccur)



class Share(Base):
    """table of authorization"""
    __tablename__ = 'share'
    user_id = Column(Integer, ForeignKey("user.id"))
    region_id = Column(Integer, primary_key = True)
    share = Column(Float)
    doc = Column(String(255))


    def __init__(self, user_id, region_id, share, doc):
        self.user_id = user_id
        self.region_id = region_id
        self.share = share
        self.doc = doc
    def __repr__(self):
        return "<{}(user_id = {}, region_id = {}, share = {}, doc = {}".format(self.__class__,self.user_id, self.region_id, self.share, self.doc)



class Region(Base):
    """table of authorization"""
    __tablename__ = 'region'
    region_id = Column(Integer, ForeignKey("share.region_id"))
    area = Column(Float)
    number_region = Column(Integer, primary_key = True)



    def __init__(self, region_id, area, number_region):
        self.region_id = region_id
        self.area = area
        self.number_region = number_region

    def __repr__(self):
        return "<{}(region_id = {}, area = {}, number_region = {}".format(self.__class__,self.region_id, self.area, self.number_region)



class Transactions(Base):
    __tablename__ = 'transactions'
    id_transaction = Column(Integer, primary_key = True, autoincrement=True)
    id_user = Column(Integer, ForeignKey("user.id"))
    date = Column(Date)
    name_serv = Column(String, ForeignKey("service.name_service"))
    cost_unit = Column(Float, ForeignKey("service.cost_unit"))
    cost = Column(Float)
    payment = Column(Float)
    overpayments = Column(Float)
    total = Column(Float)


    def __init__(self, id_transaction, id_user, date, name_serv,cost_unit, cost,payment, overpayments, total ):
        self.id_transaction = id_transaction
        self.id_user = id_user
        self.date = date
        self.name_serv = name_serv
        self.cost_unit = cost_unit 
        self.cost = cost  
        self.payment = payment
        self.overpayments = overpayments
        self.total = total
    def __repr__(self):
        return "<{}(id_transaction={}, id_user={}, date={}, name_serv={},cost_unit={}, cost={}, payment={}, overpayments={}, total={}".format(
                                                                                                    self.__class__,
                                                                                                    self.id_transaction,
                                                                                                    self.id_user,
                                                                                                    self.date,
                                                                                                    self.name_serv,
                                                                                                    self.cost_unit,
                                                                                                    self.cost,
                                                                                                    self.payment,
                                                                                                    self.overpayments,
                                                                                                    self.total)



class Service(Base):
    __tablename__ = "service"
    date = Column(Date)
    name_service = Column(String, primary_key = True)
    doc_serv = Column(String)
    period = Column(Integer)
    cost_unit = Column(Float)
    peny_data = Column(Date)
    peny = Column(Float)
    unit = Column(String)
    def __init__(self, date, name_serv, doc_serv, period, cost_unit, unit, peny_data, peny):
        self.date = date
        self.name_serv = name_serv
        self.doc_serv = doc_serv
        self.period = period
        self.cost_unit = cost_unit
        self.unit = unit
        self.peny_data = peny_data
        self.peny = peny
        self.unit = unit
    def __repr__(self):
        return "<{}(date={}, name_serv={}, doc_serv={}, period ={}, cost_unit={}, unit={}, peny_data={}, peny={}, unit = {}".format(self.__class__, self.date,
                                                                                                                                                self.name_serv,
                                                                                                                                                self.doc_serv,
                                                                                                                                                self.period,
                                                                                                                                                self.cost_unit,
                                                                                                                                                self.unit,
                                                                                                                                                self.peny_data,
                                                                                                                                                self.peny,
                                                                                                                                                self.unit)



class Counter(Base):
    __tablename__ = "counter"
    date = Column(Date)
    id_counter = Column(Integer, primary_key = True)
    user_id = Column(Integer)
    name_counter = Column(String, ForeignKey("service.name_service"))
    value = Column(Integer)

    service = relationship("Service", backref="name_serv")

    def __init__(self, date, id_counter, user_id, name_counter, value):
        self.date = date
        self.id_counter = id_counter
        self.user_id = user_id
        self.name_counter = name_counter
        self.value = value

    def __repr__(self):
        return "<{}(date={}, id_counter={}, user_id={}, name_counter={}, value={}".format(self.__class__, self.date,
                                                                                                        self.id_counter,
                                                                                                        self.user_id,
                                                                                                        self.name_counter,
                                                                                                        self.value)



class Inventory(Base):
    __tablename__ = "Inventory"
    date = Column(Date)
    user_id = Column(Integer)
    number_unit = Column(Integer, primary_key = True)
    name_unit = Column(String)
    available = Column(Integer)

    def __init__(self, date, user_id, number_unit, name_unit, available):
        self.date = date
        self.user_id = 
        self.number_unit = number_unit
        self.name_unit = name_unit
        self.available = available

    def __repr__(self):
        return "<{}(date = {}, user_id = {}, number_unit = {}, name_unit = {}, available = {}".format(self.__class__,
                                                                                                        self.date,
                                                                                                        self.user_id,
                                                                                                        self.number_unit,
                                                                                                        self.name_unit,
                                                                                                        self.available)



class Company(Base):
    __tablename__ = "trans_copm"
    id_transaction = Column(Integer, primary_key = True)
    date = Column(Date)
    id_creditor = Column(Integer)
    name_service = Column(String)
    cost = Column(Float)
    id_deb = Column(Integer)

    def __init__(self, id_transaction, date, name_creditor, name_service, cost, name_deb):
        self.id_transaction = id_transaction
        self.date = date
        self.id_creditor = id_creditor
        self.name_service = name_service
        self.cost = cost
        self.id_deb = id_deb

    def __repr__(self):
        return "<{}(id_transaction={}, date={}, id_creditor={}, name_service={}, cost={}, id_deb = {}".format(self.__class__, 
                                                                                                            self.id_transaction,
                                                                                                            self.date,
                                                                                                            self.id_creditor,
                                                                                                            self.name_service,
                                                                                                            self.cost,
                                                                                                            self.id_deb)




def create_session(engine):
    from sqlalchemy.orm import sessionmaker
    global SESSION
    Session = sessionmaker(bind=engine)
    Session.configure(bind=engine)
    SESSION = Session()
    return SESSION


def create_debug_engine(echo=False):
    from sqlalchemy import create_engine

    global ENGINE, BASE
    ENGINE = create_engine('sqlite:///:user.db', echo=echo)
    BASE.metadata.create_all(ENGINE)
    return ENGINE


def create_release_engine(echo=False):
    raise RuntimeError("Not implemented!")
    return ENGINE


def print_session():
    global SESSION
    print(SESSION)

def select_obj(value, param1, param2, param3, param4):
    b = []

    if param4 == None:
        for value_c in session.query(value).filter(param1 == param2):
            b.append(value_c[0])
    else:
        for value_c in session.query(value).filter(param1 == param2).filter(param3 == param4):
            b.append(value_c[0])
    return b


de = create_debug_engine(True)
session = create_session(de)
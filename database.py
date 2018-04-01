from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, Float, Numeric, Date, Enum
from sqlalchemy import ForeignKey

SESSION = None
ENGINE = None
Base = declarative_base()

BASE = Base
class User(Base):
	"""table of authorization"""
	__tablename__ = 'user'
	id = Column(Integer, primary_key=True)
	login = Column(String(20))
	password = Column(String(20))

	def __init__(self, id, login, password):
		self.id = id
		self.login = login
		self.password = password

	def __repr__(self):
		return "<{}(id = {}, login = {}, password = {}".format(self.__class__,self.id, self.login, self.password)



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
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, Float, Numeric, Date, Enum
from sqlalchemy import ForeignKey
from sqlalchemy.orm import sessionmaker

# SESSION = None
# ENGINE = None
Base = declarative_base()

BASE = Base
class User(Base):
    """table of authorization"""
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    login = Column(String(20))
    password = Column(String(20))
    membership = Column(Integer)
    privelege_id = Column(Integer)

    def __init__(self, id, login, password):
        self.id = id
        self.login = login
        self.password = password
        self.membership = membership
        self.privelege_id = privelege_id
    

    # def __repr__(self):
    #     return "<{}(id = {}, login = {}, password = {}, membership = {}, privelege_id = {}".format(self.__class__,self.id, self.login, self.password, self.membership, self.privelege_id)

class Share(Base):
    """table of authorization"""
    __tablename__ = 'Share'
    user_id = Column(Integer, ForeignKey("user.id"))
    region_id = Column(Integer, primary_key = True)
    share = Column(Integer)
    doc = Column(String(255))
    user = relationship("User", backref = "users")

    def __init__(self, user_id, region_id, share, doc):
        self.user_id = user_id
        self.region_id = region_id
        self.share = share
        self.doc = doc
    def __repr__(self):
        return "<{}(user_id = {}, region_id = {}, share = {}".format(self.__class__,self.user_id, self.region_id, self.share)


class Region(Base):
    """table of authorization"""
    __tablename__ = 'region'
    region_id = Column(Integer, ForeignKey("Share.region_id"))
    area = Column(Integer)
    number_region = Column(Integer, primary_key = True)

    def __init__(self, id, region_id, area):
        self.region_id = region_id
        self.area = area
        self.number_region = number_region

    def __repr__(self):
        return "<{}(region_id = {}, area = {}, number_region = {}".format(self.__class__,self.region_id, self.area, self.number_region)




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


# def print_session():
#     global SESSION
#     print(SESSION)
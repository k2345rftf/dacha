from database import User, Share, Region, create_debug_engine, create_session
# from zope.interface import Interface
# from interface_region import IRegion
# from interface_region import IShare


class Shares:
	# zope.interface.implemetedBy(IShare)
	def __init__(self, user_id):
		self.user_id = user_id

	def id_regions(self, user_id):
		self.b = []
		for self.region_id in session.query(Share.region_id).filter(Share.user_id == self.user_id):
			self.b.append(self.region_id[0])
		return self.b
	def shares(self, user_id):
		self.b =[]
		for self.share in session.query(Share.share).filter(Share.user_id == self.user_id):
			self.b.append(self.share[0])
		return self.b
	def documents(self, user_id):
		self.b =[]
		for self.share in session.query(Share.share).filter(Share.user_id == self.user_id):
			self.b.append(self.share[0])
		return self.b

class Regions():
	# zope.interface.implemetedBy(IRegion)
	def __init__(self, region_id):
		self.region_id = region_id

	def areas(self, region_id):
		self.b = []
		for self.region_id in session.query(Region.area).filter(Region.region_id == self.region_id):
			self.b.append(self.region_id[0])
		return self.b
	def numbers(self, region_id):
		self.b =[]
		for self.number in session.query(Region.number_region).filter(Region.region_id == self.region_id):
			self.b.append(self.number[0])
		return self.b

de = create_debug_engine(True)
session = create_session(de)

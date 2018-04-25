from zope.interface import Interface

class IShare(Interface):
	def id_regions(user_id):
	#"""number region"""
		return
	def shares(user_id):
	#"""area region"""
		return
	def documents(user_id):
	#"""documentation about region"""
		return	 


class IRegion(Interface):
	def areas(id_region):
		#"""Area region"""
		return
	def numbers(id_region):
		#"""number region"""
		return
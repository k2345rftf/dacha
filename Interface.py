from zope.interface import Interface



class IRegion(Interface):

	def area_shares():
		# it showed massive [[num_region, share], ....]
		return

	def documentation():
		# it showed user documentation to the region (I don`t know, how will be showed the document)
		return

	def area():
		# it will be showed addition all value area
		return


		
class IShowHistory(Interface):

	def show_all():
		pass


	def show_area():
		pass





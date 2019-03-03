class switcher:
	"""
	allows you to switch between containers by specifying a path.
	"""
	def __init__(self, ownerComp):
		# The component to which this extension is attached
		self.ownerComp = ownerComp
		self.listOOfContainers = op('containers');
	def SwitchTo(self,path):
		#update this to call a container's "off" function
		for row in self.listOOfContainers.rows():
			o = op(row[0])
			if row[0] == path:
				o.par.display = True
			else:
				o.par.display = False


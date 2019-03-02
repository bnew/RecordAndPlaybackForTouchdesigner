import loader

class chopLoaderPlayer:
	"""
	chopLoaderPlayer description
	"""
	def __init__(self, ownerComp):
		# The component to which this extension is attached
		self.ownerComp = ownerComp
		self.switch = op('switch1')
		self.table = op('data')
	def AddDataset(self, path):
		newDat = {
		"OPType" : tableDAT,
		"path": path,
		"startX": 0,
		"startY": 0,
		"switch": self.switch,
		"table": self.table
		}
		loader.createOPFromFile(newDat);


	def AddFolder(self):
		folder = ui.chooseFolder()
		print("selected " + folder)
		files = loader.loadFilesFromFolder(folder,".csv")
		for file in files:
			self.AddDataset(folder+"/"+file)


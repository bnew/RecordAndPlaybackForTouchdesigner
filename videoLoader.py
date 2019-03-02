import loader

class videoloader:
	"""
	videoloader description
	"""
	def __init__(self, ownerComp):
		# The component to which this extension is attached
		self.ownerComp = ownerComp
		self.videoTable = op('table1')
		self.videoSwitch = op('switch1')
		self.movieLocationX = op('switch1').nodeX-25;
		self.movieLocationY = op('switch1').nodeY

	def AddVideo(self, path):
		newVid = {
		"OPType" : moviefileinTOP,
		"path": path,
		"startX": self.movieLocationX,
		"startY": self.movieLocationY,
		"switch": self.videoSwitch,
		"table": self.videoTable
		}
		loader.createOPFromFile(newVid);
		

	def DeleteAllVideos(self):
		self.videoTable.clear(keepFirstRow=True)
		#probably should delete any movie player ops..
		vids = self.videoSwitch.inputs;
		for vid in vids:
			vid.destroy()
	def LoadVideosFromFolder(self):
		folder = ui.chooseFolder()
		print("selected " + folder)
		files = loader.loadFilesFromFolder(folder,".mov")
		for file in files:
			self.AddVideo(folder+"/"+file)
	def LoadVideo(self):
		path = ui.chooseFile(load=True, fileTypes=[".mov"])
		if path:
			self.AddVideo(path)

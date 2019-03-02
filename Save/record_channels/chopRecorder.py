
class chopRecorder:
	"""
	records channel data into a trail, and saves it out as a csv
	"""
	def __init__(self, ownerComp):
		self.ownerComp = ownerComp
		self.trail = op('trail1')
		self.type = '.csv' #file type to save as
		self.data = op('chopto1')
		self.data.bypass = True
		self.filenameDisplay = op('text2')

	def ChooseLocation(self):
		saver = self.ownerComp;

		saver.Type = self.type
		saver.SaveDialogue();
		self.filenameDisplay.par.text = saver.Filename


	def Start(self):
		self.trail.par.reset.pulse()
		self.trail.par.active = 1

	def Stop(self):
		self.trail.par.active = 0
		self.data.bypass = False
		self.SaveChop();

	def SaveChop(self):
		saver = self.ownerComp;
		if saver.Path:
			self.data.save(saver.Path+ "/"+ saver.Filename)
			saver.IncrementFile();
			print("file saved")
			self.filenameDisplay.par.text = saver.Filename

		else:
			a = ui.messageBox('Error','Cant save without path, choose a location:', buttons=['cancel', 'choose location'])
			if a:
				self.ChooseLocation()
				self.SaveChop()







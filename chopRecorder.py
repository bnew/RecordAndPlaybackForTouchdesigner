"""
Help: search "Extensions" in wiki
"""

class chopRecorder:
	"""
	chopRecorder description
	"""
	def __init__(self, ownerComp):
		self.ownerComp = ownerComp
		self.trail = op('trail1')
		self.type = '.csv' #file type to save as
		#self.ownerComp.Type = self.type
		self.data = op('chopto1')
		self.data.bypass = True
		#self.filenameDisplay = op('filename')

	def ChooseLocation(self):
		self.ownerComp.Type = self.type
		self.ownerComp.SaveDialogue();


	def Start(self):
		self.trail.par.reset.pulse()
		self.trail.par.active = 1

	def Stop(self):
		self.trail.par.active = 0
		self.data.bypass = False

	def SaveChop(self):
		saver = self.ownerComp;
		if saver.Path:
			self.data.save(saver.Path+ "/"+ saver.Filename)
			saver.IncrementFile();
			print("file saved")
		else:
			a = ui.messageBox('Error','Cant save without path, choose a location:', buttons=['cancel', 'choose location'])
			if a:
				self.ChooseLocation()
				self.SaveChop()







#	import saver_utils as s

class videoRecorder:
	"""
	videoRecorder description
	"""
	def __init__(self, ownerComp):
		# The component to which this extension is attached
		self.ownerComp = ownerComp
		self.type = ".mov"
		self.recorder = op('moviefileout1')
		self.displayText = op('text2')

	def ChooseLocation(self):
		oc = self.ownerComp
		oc.Type = self.type;
		oc.SaveDialogue();
		self.setVideoPath();

	def Start(self):
		self.recorder.par.record = True;

	def Stop(self):
		self.recorder.par.record = False;

		oc = self.ownerComp
		self.ownerComp.IncrementFile();
		self.displayText.par.text = self.ownerComp.Filename
		self.setVideoPath();

	def setVideoPath(self):
		oc = self.ownerComp
		self.recorder.par.file = oc.Path+'/'+oc.Filename
		self.displayText.par.text = oc.Filename




	# def SetFileNameAndLocation(self, incrementing):
	# 	#set the file name
	# 	print("boo")
	# 	#open ui
	# 	file = s.getFile()
	# 	print(file)
	# 	if file:
	# 		self.latestPath = file[0] + '.mov'
	# 		op('moviefileout1').par.file = self.latestPath
	# 		self.filename = file[1] + '.mov'

	# def updateFileNameFromPath(self):
	# 	fn = self.latestPath.split('/')
	# 	fn = fn[len(fn)-1]
	# 	self.filename = fn

	# def incrementFile(self):
	# 	self.filename = self.filename + currentCount;


	# def StartRecording(self):
	# 	print("recording")

	# def Pause(self):
	# 	print("pause")

	# def Continue(self):
	# 	print("continue")

	# def StopRecording(self):
	# 	print("stop")

	# def SaveFile(self):
	# 	print("self")
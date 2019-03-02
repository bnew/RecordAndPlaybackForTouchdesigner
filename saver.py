from sys import platform

class saver:
	"""
	saver description
	"""


	def __init__(self, ownerComp):
		# The component to which this extension is attached
		self.ownerComp = ownerComp
		self.count = 0; #something to increment the filename
		self.Path = ""; #the folder
		self.Filename = ""; #the name + type
		self.Name = ""; #the base name, ignoring any incrementing
		self.Type ="" #the file type

	def SaveDialogue(self):
		path = ui.chooseFile(load=False,title="set the name and location of your file")

		if path:
			print("got " + path)
			if platform == "win32":
				path = ''.join(path.split('.')[:-1])
				#print(path)
			fn = path.split('/') #split the path
			self.Path = '/'.join(fn[:-1])
			print("path is set to " + self.Path)
			fn = fn[-1] #filename is the last element in the split
			self.Name = fn
			print("Name " + self.Name)
			self.Filename = fn + self.Type;
			print("Filename " + self.Filename)
			self.count = 0;

	def IncrementFile(self):
		self.count += 1;
		self.Filename = self.Name + str(self.count) + self.Type; 

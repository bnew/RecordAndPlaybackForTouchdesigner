'''
place inside of a component that you would like to save without externalities 
and run this script
in order to compile for release
'''
def saveTOX(op, folder):
	path = folder + "/" + op.name + ".tox"
	op.save(path)
	return


ogOP = parent();
targetOP = parent(2).copy(ogOP);

path = ui.chooseFolder(title="save the toxes without dependencies")
if path:
	listOfExternalCOMPs= targetOP.findChildren(parName='externaltox',onlyNonDefaults=True)
	print(path+".tox")
	#externals= {} #dict to remember our external paths
	for c in listOfExternalCOMPs:
		#externals[c.id] = c.par.externaltox
		c.par.externaltox = ''
	targetOP.par.externaltox =''

	listOfExternalTextFiles= targetOP.findChildren(parName='file', type=DAT)
	for txtop in listOfExternalTextFiles:
		print(txtop)
		txtop.par.file = ''
		#txtop.par.loadonstart = 0
	saveTOX(targetOP,path)
	
	#save the other toxes that are children of the target:
	for c in listOfExternalCOMPs:
		saveTOX(c,path)


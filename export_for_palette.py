targetOP = op('record_and_playback')
parent().copy(targetOP);
path = ui.chooseFile(load=False,title="save the tox")
if path:
	listOfExternalOperators= targetOP.findChildren(parName='externaltox',onlyNonDefaults=True)
	print(path+".tox")
	#externals= {} #dict to remember our external paths
	for c in listOfExternalOperators:
		#externals[c.id] = c.par.externaltox
		c.par.externaltox = ''
	targetOP.par.externaltox =''

	listOfExternalTextFiles= targetOP.findChildren(parName='file', type=DAT)
	for txtop in listOfExternalTextFiles:
		print(txtop)
		txtop.par.file = ''
		#txtop.par.loadonstart = 0

	f = targetOP.save(path+".tox")
	
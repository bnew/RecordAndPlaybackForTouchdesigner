import os


def loadFilesFromFolder(folder,filetype):
	files = []
	for filename in os.listdir(folder):
		if filename.endswith(filetype):
			files.append(filename)
			print(filename)
	return files


def createOPFromFile(properties):
	#OPType, path, startX, startY, switch
	newPlayer = parent().create(properties['OPType']);
	#load the file
	newPlayer.par.file = properties['path']
	#move the player so it looks nice
	newPlayer.nodeY = properties['startX'];
	newPlayer.nodeY = properties['startY']-newPlayer.digits*100;
	#connect it to a switch
	newPlayer.outputConnectors[0].connect(properties['switch'])
	
	newRow =[properties['path'].split("/")[-1], len(properties['switch'].inputs)-1, newPlayer.name]
	properties['table'].appendRow(newRow);
	#pulse reload player to be safe
	newPlayer.par.reload.pulse()

def removeFiles(table, switch):
	#confirm = ui.messageBox('WARNING', 'Do you want to remove all videos in the playlist? The files will not be deleted', buttons=['no', 'yes'])
	#if confirm:
	table.clear(keepFirstRow=True)
	files =switch.inputs;
	for file in files:
			file.destroy()

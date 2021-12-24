import glob

def search(directory, searchElem:list, extension = ".txt"):
	files = glob.glob(directory+"*"+extension)
	files_detected = []
	for file in files:
		sf = open(file)
		stored = sf.read()
		for elem in searchElem:
			if elem in stored:
				files_detected.append(file)
				return files_detected
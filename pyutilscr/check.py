import glob

def search(directory, searchElem:list, extension = ".txt"):
	"""Searches files in a specified directory and checks if they contain the specified elements.
    
    	directory format: /home/runner/project
    	directory type: folder
    	element type: list
    	extensions requirments: MUST have a period before, such as ".txt"

    :param directory: 
    :param searchElem:list: 
    :param extension:  (Default value = ".txt")

	"""
	files = glob.glob(directory+"*"+extension)
	files_detected = []
	for file in files:
		sf = open(file)
		stored = sf.read()
		for elem in searchElem:
			if elem in stored:
				files_detected.append(file)
				return files_detected
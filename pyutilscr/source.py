import inspect



def method_source(method):
	"""
	Gets source code of a method/function/class
	:param method:

	"""
	raw_code=inspect.getsourcelines(method)
	return "".join(raw_code[0])

def file_source(file):
	"""
	Gets source code of a file
	:param file:
	
	"""
	return inspect.getsourcefile(file)
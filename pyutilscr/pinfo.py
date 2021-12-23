import platform

class overview:
	def __init__(self):
		self.osi = platform.platform()
		self.system = platform.system()
		self.releaseinfo = platform.release()
		self.proc = platform.processor()
		self.machine = platform.machine()
		self.uname = platform.uname()
		self.version = platform.version()
	def osi(self):
		return self.osi
	def system(self):
		return self.system
	def rinfo(self):
		return self.releaseinfo
	def proc(self):
		return self.proc
	def minfo(self):
		return self.machine
	def unix(self):
		return self.uname
	def version(self):
		return self.version
	def complete(self):
		comp = [self.osi, self.system, self.releaseinfo, self.proc, self.machine, self.uname,self.version]
		return comp
ov=overview()
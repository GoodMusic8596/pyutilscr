import platform

class overview:
	""" 
	Overview contains all the info necessary for system informatin.
	"""
	def __init__(self):
		self.osi = platform.platform()
		self.system = platform.system()
		self.releaseinfo = platform.release()
		self.proc = platform.processor()
		self.machine = platform.machine()
		self.uname = platform.uname()
		self.version = platform.version()
	def osi(self):
		"""Returns Operating system info, such as Darwin, Windows, or Linux."""
		return self.osi
	def system(self):
		"""Returns Darwin, Windows, Linux, etc."""
		return self.system
	def rinfo(self):
		"""Returns release info on your os distribution."""
		return self.releaseinfo
	def proc(self):
		"""Returns your processor info."""
		return self.proc
	def minfo(self):
		"""Returns your machine info such as assembly and bit(32 or 64) info."""
		return self.machine
	def unix(self):
		"""Returns uname information."""
		return self.uname
	def version(self):
		"""Returns os version."""
		return self.version
	def complete(self):
		"""Returns os info, system info, release info, processor info, machine info, uname info, and version info."""
		comp = [self.osi, self.system, self.releaseinfo, self.proc, self.machine, self.uname,self.version]
		return comp
ov=overview()
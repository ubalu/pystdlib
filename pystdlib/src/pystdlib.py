def hcf(msg='', die:bool=False):
	"""
Just ye' olde Halt and Catch Fire.\n
### Example:
	>>> hcf(msg='Something went wrong', die=True)
	Something went wrong
	
	[Process exited with exit code 1]
	>>> hcf(die=False)
	Traceback (most recent call last):
	File <yourfile>
	File <modulefile>
		assert False, msg
	AssertionError
"""
	if die:
		print(msg)
		exit(1)
	else:
		assert False, msg


class Iota:
	def __init__(self) -> None:
		self.iota_counter = 0

	def iota(self) -> int:
		r = self.iota_counter
		self.iota_counter += 1
		return r
	
	def reset(self) -> None:
		self.iota_counter = 0
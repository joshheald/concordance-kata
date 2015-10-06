class Splitter():
	@classmethod
	def lineSplit(cls, line):
		"""Split a line of words into words"""
		line = line.translate(None, '.:,')
		return line.split()

	@classmethod
	def linesForString(cls, string):
		"""Split a string into an array of lines"""
		alllines = string.split('\n')
		return [line for line in alllines if line is not ""]
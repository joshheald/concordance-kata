class ConcordanceGenerator():
	"""Produces a concordance, a list of all the words present in a text, and the line numbers on which they occur."""
	splitter = None
	def __init__(self, splitter):
		self.splitter = splitter

	def concordanceForString(self, string=None):
		lines = self.splitter.linesForString(string)
		for line in lines:
			self.splitter.lineSplit(line)
		return string

		
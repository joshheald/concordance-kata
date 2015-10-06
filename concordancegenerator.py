import concordance

class ConcordanceGenerator():
	"""Produces a concordance, a list of all the words present in a text, and the line numbers on which they occur."""
	splitter = None
	def __init__(self, splitter):
		self.splitter = splitter

	def concordanceForString(self, string=None):
		if string is not None:
			lines = self.splitter.linesForString(string)
			c = concordance.Concordance()
			for line_number, line in enumerate(lines, start=1):
				words = self.splitter.lineSplit(line)
				if words is not None:
					for word in words:
						c.addInstanceOfWordAtLine(word, line_number)

			return c

		
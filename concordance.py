class Concordance():
	"""An alphabetical list of words with an associated list of line numbers"""
	_wordlist = {}
	def __init__(self):
		self._wordlist = dict()

	def addInstanceOfWordAtLine(self, word="", lineNumber=-1):
		if word is not "" and lineNumber > -1:
			word = word.lower()
			self._wordlist.setdefault(word, set())
			self._wordlist[word].add(lineNumber)

	def entryForWord(self, word):
		word = word.lower()
		if word in self._wordlist.keys():
			lineNumbers = "{0}".format(", ".join(str(lineNumber) for lineNumber in sorted(self._wordlist[word])))
			return "{word}: {lineNumbers}".format(word=word, lineNumbers=lineNumbers)

	def allEntries(self):
		entries = []
		for word in self._wordlist:
			entries.append(self.entryForWord(word))
		return entries

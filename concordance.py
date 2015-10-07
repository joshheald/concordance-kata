# -*- coding: utf-8 -*-
class Concordance():
	"""An alphabetical list of words with an associated list of line numbers"""
	def __init__(self):
		self._wordlist = dict()

	def addInstanceOfWordAtLine(self, word="", lineNumber=-1):
		if word is not "" and lineNumber > -1:
			word = word.lower()
			self._wordlist.setdefault(word, set())
			self._wordlist[word].add(lineNumber)

	def entryForWord(self, word):
		word = word.lower()
		line_numbers = self._wordlist.get(word, None)
		if line_numbers:
			line_numbers_string = "{0}".format(", ".join(str(line_number) for line_number in sorted(line_numbers)))
			return "{word}: {line_numbers}".format(word=word, line_numbers=line_numbers_string)

	def allEntries(self):
		entries = []
		for word in self._wordlist:
			entries.append(self.entryForWord(word))
		return sorted(entries)

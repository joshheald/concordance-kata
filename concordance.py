# -*- coding: utf-8 -*-
class Concordance():
	"""An alphabetical list of words with an associated list of line numbers"""
	def __init__(self):
		self._word_list = dict()

	def add_instance_of_word_at_line(self, word="", line_number=-1):
		if word is not "" and line_number > -1:
			word = word.lower()
			self._word_list.setdefault(word, set())
			self._word_list[word].add(line_number)

	def entry_for_word(self, word):
		word = word.lower()
		line_numbers = self._word_list.get(word, None)
		if line_numbers:
			line_numbers_string = "{0}".format(", ".join(str(line_number) for line_number in sorted(line_numbers)))
			return "{word}: {line_numbers}".format(word=word, line_numbers=line_numbers_string)

	def all_entries(self):
		entries = []
		for word in self._word_list:
			entries.append(self.entry_for_word(word))
		return sorted(entries)
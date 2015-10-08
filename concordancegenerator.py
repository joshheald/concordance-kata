# -*- coding: utf-8 -*-

import concordance
import splitter
import sys

class ConcordanceGenerator():
	"""Produces a concordance, a list of all the words present in a text, and the line numbers on which they occur."""
	splitter = None
	def __init__(self, splitter):
		self.splitter = splitter

	def concordance_for_string(self, string=None):
		if string is None:
			return None
		
		working_concordance = concordance.Concordance()
		lines = self.splitter.lines_for_string(string)
		for line_number, line in enumerate(lines, start=1):
			words = self.splitter.line_split(line)
			working_concordance = self._add_words_in_line_to_concordance(words, line_number, working_concordance)

		return working_concordance

	def _add_words_in_line_to_concordance(self, words, line_number, cdance):
		for word in words:
			cdance.add_instance_of_word_at_line(word, line_number)
		return cdance

def main(filename):
	if filename is not None:
		pass
	with open(filename, "rU") as text_file:
		text_string = text_file.read()
		generator = ConcordanceGenerator(splitter=splitter.Splitter())
		output = generator.concordance_for_string(text_string)
		for entry in output.all_entries():
			print entry

if __name__ == "__main__":
	main(filename=sys.argv[1])
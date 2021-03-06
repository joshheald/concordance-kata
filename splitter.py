# -*- coding: utf-8 -*-
import re


def quote_replace(match):
	return match.group(1)

class Splitter():
	def line_split(self, line):
		"""Split a line of words into words"""
		line = re.sub(r"`(.*?)'", quote_replace, line)
		line = line.translate(None, '.:,()+*')
		return line.split()

	def lines_for_string(self, string):
		"""Split a string into an array of lines"""
		all_lines = string.split('\n')
		return [line for line in all_lines if line is not ""]
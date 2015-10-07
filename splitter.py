# -*- coding: utf-8 -*-
class Splitter():
	def lineSplit(self, line):
		"""Split a line of words into words"""
		line = line.translate(None, '.:,()+*')
		return line.split()

	def linesForString(self, string):
		"""Split a string into an array of lines"""
		alllines = string.split('\n')
		return [line for line in alllines if line is not ""]
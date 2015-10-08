import unittest
import splitter

class SplitterTests(unittest.TestCase):
	def test_canSplitTwoWords(self):
		"""Test that we can split two words into an array with two elements"""
		test_string = "hello world"
		words = splitter.Splitter().line_split(test_string)
		self.assertEqual(len(words), 2)

	def test_line_splitWhenGivenAnEmptyStringReturnsAnEmptyArray(self):
		"""Test that we return empty array from our split on an empty string"""
		test_string = ""
		words = splitter.Splitter().line_split(test_string)
		self.assertFalse(words)

	def test_allWordsInSplitArePresentInInput(self):
		"""Test that all of the split-out words are returned"""
		test_string = "hello world"
		words = splitter.Splitter().line_split(test_string)
		for word in words:
			self.assertTrue(word in test_string)

	def test_splitterRemovesUnpermittedPunctuation(self):
		"""Test that unpermitted punctuation is removed in split"""
		test_string = "(t'was: the +best, and worst.*)"
		words = splitter.Splitter().line_split(test_string)
		self.assertEqual(words, ["t'was", "the", "best", "and", "worst"])

	def test_splitterCanProduceAnArrayOfAllTheLinesInAMultilineString(self):
		"""Test that we can get an array with the correct number of lines from a multiline string"""
		test_string = "hello world\n how's it going today"
		lines = splitter.Splitter().lines_for_string(test_string)
		self.assertEqual(len(lines), 2)

	def test_splitIntoLinesIgnoresEmptyLines(self):
		"""There can be no words on empty lines, so it doesn't make sense to return them."""
		test_string = "hello \n\n world\n how are you?"
		lines = splitter.Splitter().lines_for_string(test_string)
		self.assertEqual(len(lines), 3)

	def test_splitterRemovesBacktickApostrophesWhenUsedAsQuotationMarks(self):
		"""Test that words quoted in `this' style appear without any quotation marks"""
		test_string = "hello `world'"
		words = splitter.Splitter().line_split(test_string)
		self.assertEqual(words, ["hello", "world"])

	def test_splitterRemovesBacktickApostropheQuotationsThatSpanMultipleWords(self):
		"""Test that words quoted in `this style', across multiple words appear individually without any quotation marks"""
		test_string = "hello `world, goodbye' cruel world."
		words = splitter.Splitter().line_split(test_string)
		self.assertEqual(words, ["hello", "world", "goodbye", "cruel", "world"])

	def test_splitterRemovesMultipbleBacktickApostropheQuotationsOnTheSameLine(self):
		"""Test that words quoted in `this' style appear without any quotation marks even when there's more than one on a line"""
		test_string = "`hello' `world'"
		words = splitter.Splitter().line_split(test_string)
		self.assertEqual(words, ["hello", "world"])
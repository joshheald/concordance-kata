import unittest
import splitter

class SplitterTests(unittest.TestCase):
	def test_canSplitTwoWords(self):
		"""Test that we can split two words into an array with two elements"""
		testString = "hello world"
		words = splitter.Splitter().lineSplit(testString)
		self.assertEqual(len(words), 2)

	def test_lineSplitWhenGivenAnEmptyStringReturnsAnEmptyArray(self):
		"""Test that we return empty array from our split on an empty string"""
		testString = ""
		words = splitter.Splitter().lineSplit(testString)
		self.assertFalse(words)

	def test_allWordsInSplitArePresentInInput(self):
		"""Test that all of the split-out words are returned"""
		testString = "hello world"
		words = splitter.Splitter().lineSplit(testString)
		for word in words:
			self.assertTrue(word in testString)

	def test_splitterRemovesUnpermittedPunctuation(self):
		"""Test that unpermitted punctuation is removed in split"""
		testString = "(t'was: the +best, and worst.*)"
		words = splitter.Splitter().lineSplit(testString)
		self.assertEqual(words, ["t'was", "the", "best", "and", "worst"])

	def test_splitterCanProduceAnArrayOfAllTheLinesInAMultilineString(self):
		"""Test that we can get an array with the correct number of lines from a multiline string"""
		testString = "hello world\n how's it going today"
		lines = splitter.Splitter().linesForString(testString)
		self.assertEqual(len(lines), 2)

	def test_splitIntoLinesIgnoresEmptyLines(self):
		"""There can be no words on empty lines, so it doesn't make sense to return them."""
		testString = "hello \n\n world\n how are you?"
		lines = splitter.Splitter().linesForString(testString)
		self.assertEqual(len(lines), 3)
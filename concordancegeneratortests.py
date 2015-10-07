import unittest
import concordancegenerator
import concordance

class ConcordanceGeneratorTests(unittest.TestCase):
	def test_init_takesASplitter(self):
		"""A splitter is passed in to do the work of splitting up input strings"""
		sut = concordancegenerator.ConcordanceGenerator(splitter=SpySplitter())

	def test_concordance_for_string_whenCalledWithNoneReturnsNone(self):
		"""An empty string wouldn't make sense if there was no text to begin with"""
		sut = concordancegenerator.ConcordanceGenerator(splitter=SpySplitter())
		self.assertIsNone(sut.concordance_for_string(None))

	def test_concordance_for_string_whenCalledWithAnEmptyStringReturnsAnEmptyConcordance(self):
		"""An empty string has no words, so the concordance should be empty too"""
		sut = concordancegenerator.ConcordanceGenerator(splitter=SpySplitter())
		self.assertIsNone(sut.concordance_for_string())

	def test_concordance_for_string_usesTheSplitterItWasCreatedWithToSplitTheStringIntoLines(self):
		"""We have to parse the string one line at a time in order to retain the line numbers"""
		spy_splitter = SpySplitter()
		sut = concordancegenerator.ConcordanceGenerator(splitter=spy_splitter)
		expected_string = "Hello world!\nGoodbye cruel world..."
		sut.concordance_for_string(expected_string)
		self.assertTrue(spy_splitter.lines_for_string_was_called)
		self.assertEqual(expected_string, spy_splitter.lines_for_string_most_recent_string)

	def test_concordance_for_string_usesTheSplitterItWasCreatedWithToSplintEachLineIntoWords(self):
		mock_splitter = MockSplitter()
		sut = concordancegenerator.ConcordanceGenerator(splitter=mock_splitter)
		expected_string = "Hello world!\nGoodbye cruel world..."
		sut.concordance_for_string(expected_string)
		self.assertEqual(["Hello world!", "Goodbye cruel world..."], mock_splitter.line_split_lines)

	def test_concordance_for_string_returnsAConcordanceWithAllTheWordsReturnedFromLineSplit(self):
		expected_concordance = concordance.Concordance()
		expected_concordance._word_list = {
			"hello": set([1]),
			"world": set([1, 2]),
			"goodbye": set([2]),
			"cruel": set([2])
		}
		mock_splitter = MockSplitter()
		sut = concordancegenerator.ConcordanceGenerator(splitter=mock_splitter)
		actual_concordance = sut.concordance_for_string("Hello world!\nGoodbye cruel world...")
		self.assertEqual(expected_concordance.all_entries(), actual_concordance.all_entries())




# Mock Classes

class SpySplitter():
	def __init__(self):
		self.lines_for_string_was_called = False
		self.lines_for_string_most_recent_string = None

	def line_split(self, line):
		return []

	def lines_for_string(self, string):
		self.lines_for_string_was_called = True
		self.lines_for_string_most_recent_string = string
		return ["Hello world!", "Goodbye cruel world..."]

class MockSplitter():
	def __init__(self):
		self.line_split_lines = []
		self.line_count = 0

	def line_split(self, line):
		self.line_split_lines.append(line)
		if self.line_count == 0:
			self.line_count += 1
			return ["Hello", "world"]
		elif self.line_count == 1:
			self.line_count += 1
			return ["Goodbye", "cruel", "world"]
		else:
			return None

	def lines_for_string(self, string):
		return ["Hello world!", "Goodbye cruel world..."]
		
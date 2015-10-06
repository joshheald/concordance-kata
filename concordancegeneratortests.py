import unittest
import concordancegenerator
import concordance

class ConcordanceGeneratorTests(unittest.TestCase):
	def test_init_takesASplitter(self):
		"""A splitter is passed in to do the work of splitting up input strings"""
		sut = concordancegenerator.ConcordanceGenerator(splitter=SpySplitter())

	def test_concordanceForString_whenCalledWithNoneReturnsNone(self):
		"""An empty string wouldn't make sense if there was no text to begin with"""
		sut = concordancegenerator.ConcordanceGenerator(splitter=SpySplitter())
		self.assertIsNone(sut.concordanceForString(None))

	def test_concordanceForString_whenCalledWithAnEmptyStringReturnsAnEmptyConcordance(self):
		"""An empty string has no words, so the concordance should be empty too"""
		sut = concordancegenerator.ConcordanceGenerator(splitter=SpySplitter())
		self.assertIsNone(sut.concordanceForString())

	def test_concordanceForString_usesTheSplitterItWasCreatedWithToSplitTheStringIntoLines(self):
		"""We have to parse the string one line at a time in order to retain the line numbers"""
		spySplitter = SpySplitter()
		sut = concordancegenerator.ConcordanceGenerator(splitter=spySplitter)
		expected_string = "Hello world!\nGoodbye cruel world..."
		sut.concordanceForString(expected_string)
		self.assertTrue(spySplitter.linesForString_was_called)
		self.assertEqual(expected_string, spySplitter.linesForString_most_recent_string)

	def test_concordanceForString_usesTheSplitterItWasCreatedWithToSplintEachLineIntoWords(self):
		mock_splitter = MockSplitter()
		sut = concordancegenerator.ConcordanceGenerator(splitter=mock_splitter)
		expected_string = "Hello world!\nGoodbye cruel world..."
		sut.concordanceForString(expected_string)
		self.assertEqual(["Hello world!", "Goodbye cruel world..."], mock_splitter.lineSplit_lines)

	def test_concordanceForString_returnsAConcordanceWithAllTheWordsReturnedFromLineSplit(self):
		expected_concordance = concordance.Concordance()
		expected_concordance._wordlist = {
			"hello": set([1]),
			"world": set([1, 2]),
			"goodbye": set([2]),
			"cruel": set([2])
		}
		mock_splitter = MockSplitter()
		sut = concordancegenerator.ConcordanceGenerator(splitter=mock_splitter)
		actual_concordance = sut.concordanceForString("Hello world!\nGoodbye cruel world...")
		self.assertEqual(expected_concordance.allEntries(), actual_concordance.allEntries())




# Mock Classes

class SpySplitter():
	def __init__(self):
		self.lineSplit_call_count = 0
		self.linesForString_was_called = False
		self.linesForString_most_recent_string = None

	def lineSplit(self, line):
		self.lineSplit_call_count += 1

	def linesForString(self, string):
		self.linesForString_was_called = True
		self.linesForString_most_recent_string = string
		return ["Hello world!", "Goodbye cruel world..."]

class MockSplitter():
	def __init__(self):
		self.lineSplit_lines = []
		self.lineCount = 0

	def lineSplit(self, line):
		self.lineSplit_lines.append(line)
		if self.lineCount == 0:
			self.lineCount += 1
			return ["Hello", "world"]
		elif self.lineCount == 1:
			self.lineCount += 1
			return ["Goodbye", "cruel", "world"]
		else:
			return None

	def linesForString(self, string):
		return ["Hello world!", "Goodbye cruel world..."]
		
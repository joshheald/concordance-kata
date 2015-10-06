import unittest
import concordancegenerator

class ConcordanceGeneratorTests(unittest.TestCase):
	def test_init_takesASplitter(self):
		"""A splitter is passed in to do the work of splitting up input strings"""
		sut = concordancegenerator.ConcordanceGenerator(splitter=MockSplitter())

	def test_concordanceForString_whenCalledWithNoneReturnsNone(self):
		"""An empty string wouldn't make sense if there was no text to begin with"""
		sut = concordancegenerator.ConcordanceGenerator(splitter=MockSplitter())
		self.assertIsNone(sut.concordanceForString(None))

	def test_concordanceForString_whenCalledWithAnEmptyStringReturnsAnEmptyString(self):
		"""An empty string has no words, so the concordance should be empty too"""
		sut = concordancegenerator.ConcordanceGenerator(splitter=MockSplitter())
		self.assertEqual("", sut.concordanceForString(""))

	def test_concordanceForString_usesTheSplitterItWasCreatedWithToSplitTheStringIntoLines(self):
		"""We have to parse the string one line at a time in order to retain the line numbers"""
		mockSplitter = MockSplitter()
		sut = concordancegenerator.ConcordanceGenerator(splitter=mockSplitter)
		expected_string = "Hello world!\nGoodbye cruel world..."
		sut.concordanceForString(expected_string)
		self.assertTrue(mockSplitter.linesForString_was_called)
		self.assertEqual(expected_string, mockSplitter.linesForString_most_recent_string)

	def test_concordanceForString_usesTheSplitterItWasCreatedWithToSplintEachLineIntoWords(self):
		mockSplitter = MockSplitter()
		sut = concordancegenerator.ConcordanceGenerator(splitter=mockSplitter)
		expected_string = "Hello world!\nGoodbye cruel world..."
		sut.concordanceForString(expected_string)
		self.assertEqual(2, mockSplitter.lineSplit_call_count)
		self.assertEqual(["Hello world!", "Goodbye cruel world..."], mockSplitter.lineSplit_lines)


# Mock Classes

class MockSplitter():
	lineSplit_call_count = 0
	lineSplit_lines = []
	linesForString_was_called = False
	linesForString_most_recent_string = None

	def lineSplit(self, line):
		self.lineSplit_call_count += 1
		self.lineSplit_lines.append(line)

	def linesForString(self, string):
		self.linesForString_was_called = True
		self.linesForString_most_recent_string = string
		return ["Hello world!", "Goodbye cruel world..."]
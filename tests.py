import unittest

class Splitter():
	@classmethod
	def lineSplit(cls, line):
		"""Split a line of words into words"""
		line = line.translate(None, '.:,')
		return line.split()

	@classmethod
	def linesForString(cls, string):
		"""Split a string into an array of lines"""
		alllines = string.split('\n')
		return [line for line in alllines if line is not ""]


class SplitterTests(unittest.TestCase):
	def test_canSplitTwoWords(self):
		"""Test that we can split two words into an array with two elements"""
		testString = "hello world"
		words = Splitter.lineSplit(testString)
		self.assertEqual(len(words), 2)

	def test_lineSplitWhenGivenAnEmptyStringReturnsAnEmptyArray(self):
		"""Test that we return empty array from our split on an empty string"""
		testString = ""
		words = Splitter.lineSplit(testString)
		self.assertFalse(words)

	def test_allWordsInSplitArePresentInInput(self):
		"""Test that all of the split-out words are returned"""
		testString = "hello world"
		words = Splitter.lineSplit(testString)
		for word in words:
			self.assertTrue(word in testString)

	def test_splitterRemovesUnpermittedPunctuation(self):
		"""Test that unpermitted punctuation is removed in split"""
		testString = "t'was: the best, and worst."
		words = Splitter.lineSplit(testString)
		self.assertEqual(words, ["t'was", "the", "best", "and", "worst"])

	def test_splitterCanProduceAnArrayOfAllTheLinesInAMultilineString(self):
		"""Test that we can get an array with the correct number of lines from a multiline string"""
		testString = "hello world\n how's it going today"
		lines = Splitter.linesForString(testString)
		self.assertEqual(len(lines), 2)

	def test_splitIntoLinesIgnoresEmptyLines(self):
		testString = "hello \n\n world\n how are you?"
		lines = Splitter.linesForString(testString)
		self.assertEqual(len(lines), 3)

class Concordance():
	"""An alphabetical list of words with an associated list of line numbers"""
	_wordlist = {}
	def __init__(self):
		self._wordlist = dict()

	def addInstanceOfWordAtLine(self, word="", lineNumber=-1):
		if word is not "" and lineNumber > -1:
			self._wordlist.setdefault(word, set())
			self._wordlist[word].add(lineNumber)

	def entryForWord(self, word):
		if word not in self._wordlist.keys():
			return None
		lineNumbers = "{0}".format(", ".join(str(lineNumber) for lineNumber in sorted(self._wordlist[word])))
		return "{word}: {lineNumbers}".format(word=word, lineNumbers=lineNumbers)

	def allEntries(self):
		entries = []
		for word in self._wordlist:
			entries.append(self.entryForWord(word))
		print entries
		return entries


class ConcordanceTests(unittest.TestCase):
	def test_addInstanceOfWordAtLine_canAddAWordToTheConcordance(self):
		"""Test that we can add a new word to the concordance"""
		expectedWord = "WordFromText"
		sut = Concordance()
		sut.addInstanceOfWordAtLine(word=expectedWord)

	def test_addInstanceOfWordAtLine_canAddAWordToTheConcordanceWithALineNumber(self):
		"""Test that we can add a new word with associated line number to the concordance"""
		expectedLineNumber = 15
		sut = Concordance()
		sut.addInstanceOfWordAtLine(lineNumber=expectedLineNumber)

	def test_addInstanceOfWordAtLine_doesNotAddToTheConcordanceIfNoWordIsProvided(self):
		sut = Concordance()
		sut.addInstanceOfWordAtLine(lineNumber=1)
		self.assertEqual([], sut.allEntries())

	def test_addInstanceOfWordAtLine_doesNotAddToTheConcordanceIfNoLineNumberIsProvided(self):
		sut = Concordance()
		sut.addInstanceOfWordAtLine(word="Bruce")
		self.assertEqual([], sut.allEntries())

	def test_addInstanceOfWordAtLine_doesNotAddDuplicateLineNumbersWhenProvided(self):
		sut = Concordance()
		sut.addInstanceOfWordAtLine(word="Samwell", lineNumber=2)
		sut.addInstanceOfWordAtLine(word="Samwell", lineNumber=2)
		self.assertEqual("Samwell: 2", sut.entryForWord("Samwell"))

	def test_entryForWord_returnsNoneWhenTheWordHasNotBeenStored(self):
		expectedWord = "What's"
		sut = Concordance()
		self.assertIsNone(sut.entryForWord(expectedWord))

	def test_entryForWord_canRetrieveTheLineNumberStoredForAWord(self):
		expectedLineNumber = 42
		expectedWord = "Meaning"
		sut = Concordance()
		sut.addInstanceOfWordAtLine(word=expectedWord, lineNumber=expectedLineNumber)
		expectedConcordanceEntry = "Meaning: 42"
		self.assertEqual(expectedConcordanceEntry, sut.entryForWord(expectedWord))

	def test_entryForWord_canRetrieveMultipleLineNumbersStoredForAWord(self):
		expectedLineNumbers = [1, 4, 8, 42]
		expectedWord = "Life"
		sut = Concordance()
		for lineNumber in expectedLineNumbers:
			sut.addInstanceOfWordAtLine(word=expectedWord, lineNumber=lineNumber)
		expectedConcordanceEntry = "Life: 1, 4, 8, 42"
		self.assertEqual(expectedConcordanceEntry, sut.entryForWord(expectedWord))

	def test_entryForWord_canRetrieveTheLineNumberStoredForAWordInNumericalOrder(self):
		inputLineNumbers = [42, 4, 9, 2, 17]
		expectedWord = "and"
		sut = Concordance()
		for lineNumber in inputLineNumbers:
			sut.addInstanceOfWordAtLine(word=expectedWord, lineNumber=lineNumber)
		expectedConcordanceEntry = "and: 2, 4, 9, 17, 42"
		self.assertEqual(expectedConcordanceEntry, sut.entryForWord(expectedWord))

	def test_allEntries_canRetrieveTheConcordanceEntriesForAllWordsAtOnce(self):
		sut = Concordance()
		sut.allEntries()

	def test_allEntries_returnsEachWordWhichHasBeenAddedToTheConcordance(self):
		sut = Concordance()
		sut.addInstanceOfWordAtLine("Carta", 1)
		sut.addInstanceOfWordAtLine("Magna", 12)
		expectedConcordanceEntryList = ["Carta: 1", "Magna: 12"]
		self.assertEqual(expectedConcordanceEntryList, sut.allEntries())

	def test_allEntries_returnsEachWordWhichHasBeenAddedToTheConcordanceInAlphabeticalOrderOfWord(self):
		sut = Concordance()
		sut.addInstanceOfWordAtLine("Magna", 12)
		sut.addInstanceOfWordAtLine("Carta", 12)
		sut.addInstanceOfWordAtLine("John", 1)
		expectedConcordanceEntryList = ["Carta: 12", "John: 1", "Magna: 12"]
		self.assertEqual(expectedConcordanceEntryList, sut.allEntries())


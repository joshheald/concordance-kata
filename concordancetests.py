import unittest
import concordance

class ConcordanceTests(unittest.TestCase):
	def test_addInstanceOfWordAtLine_canAddAWordToTheConcordance(self):
		"""Test that we can add a new word to the concordance"""
		expectedWord = "WordFromText"
		sut = concordance.Concordance()
		sut.addInstanceOfWordAtLine(word=expectedWord)

	def test_addInstanceOfWordAtLine_canAddAWordToTheConcordanceWithALineNumber(self):
		"""Test that we can add a new word with associated line number to the concordance"""
		expectedLineNumber = 15
		sut = concordance.Concordance()
		sut.addInstanceOfWordAtLine(lineNumber=expectedLineNumber)

	def test_addInstanceOfWordAtLine_doesNotAddToTheConcordanceIfNoWordIsProvided(self):
		"""The method has defaults to make it easier to test, but really this should be refactored out"""
		sut = concordance.Concordance()
		sut.addInstanceOfWordAtLine(lineNumber=1)
		self.assertEqual([], sut.allEntries())

	def test_addInstanceOfWordAtLine_doesNotAddToTheConcordanceIfNoLineNumberIsProvided(self):
		"""The method has defaults to make it easier to test, but really this should be refactored out"""
		sut = concordance.Concordance()
		sut.addInstanceOfWordAtLine(word="Bruce")
		self.assertEqual([], sut.allEntries())

	def test_addInstanceOfWordAtLine_doesNotAddDuplicateLineNumbersWhenProvided(self):
		"""Words may be present more than once on a line, but we don't want to note that line number more than once"""
		sut = concordance.Concordance()
		sut.addInstanceOfWordAtLine(word="Samwell", lineNumber=2)
		sut.addInstanceOfWordAtLine(word="Samwell", lineNumber=2)
		self.assertEqual("samwell: 2", sut.entryForWord("samwell"))

	def test_addInstanceOfWordAtLine_isCaseInsensitive(self):
		"""This, this, and THIS are all the same word, so we should group all instances together"""
		sut = concordance.Concordance()
		sut.addInstanceOfWordAtLine(word="this", lineNumber=3)
		sut.addInstanceOfWordAtLine(word="This", lineNumber=4)
		sut.addInstanceOfWordAtLine(word="THIS", lineNumber=7)
		self.assertEqual(["this: 3, 4, 7"], sut.allEntries())

	def test_entryForWord_returnsNoneWhenTheWordHasNotBeenStored(self):
		"""If we don't store a given word, we can't produce an entry for it, and None is better than an empty string to represent that"""
		expectedWord = "what's"
		sut = concordance.Concordance()
		self.assertIsNone(sut.entryForWord(expectedWord))

	def test_entryForWord_canRetrieveTheLineNumberStoredForAWord(self):
		"""We should be able to look up our concordance entry for a single word"""
		expectedLineNumber = 42
		expectedWord = "meaning"
		sut = concordance.Concordance()
		sut.addInstanceOfWordAtLine(word=expectedWord, lineNumber=expectedLineNumber)
		expectedConcordanceEntry = "meaning: 42"
		self.assertEqual(expectedConcordanceEntry, sut.entryForWord(expectedWord))

	def test_entryForWord_canRetrieveMultipleLineNumbersStoredForAWord(self):
		"""The concordance entry we produce should have all the line numbers we store for a word"""
		expectedLineNumbers = [1, 4, 8, 42]
		expectedWord = "life"
		sut = concordance.Concordance()
		for lineNumber in expectedLineNumbers:
			sut.addInstanceOfWordAtLine(word=expectedWord, lineNumber=lineNumber)
		expectedConcordanceEntry = "life: 1, 4, 8, 42"
		self.assertEqual(expectedConcordanceEntry, sut.entryForWord(expectedWord))

	def test_entryForWord_canRetrieveTheLineNumberStoredForAWordInNumericalOrder(self):
		"""Potentially, a string could be read in reverse or arbitrary order - we should always return in ascending order"""
		inputLineNumbers = [42, 4, 9, 2, 17]
		expectedWord = "and"
		sut = concordance.Concordance()
		for lineNumber in inputLineNumbers:
			sut.addInstanceOfWordAtLine(word=expectedWord, lineNumber=lineNumber)
		expectedConcordanceEntry = "and: 2, 4, 9, 17, 42"
		self.assertEqual(expectedConcordanceEntry, sut.entryForWord(expectedWord))

	def test_entryForWord_isCaseInsensitive(self):
		"""That, that, and THAT are all the same word, so we should be able to get the combined entry for them whichever we use as a lookup key"""
		sut = concordance.Concordance()
		sut.addInstanceOfWordAtLine(word="something", lineNumber=8)
		self.assertEqual("something: 8", sut.entryForWord("SOMEthing"))

	def test_allEntries_returnsEachWordWhichHasBeenAddedToTheConcordance(self):
		"""When we get all the entries, every word we've added should have an entry returned in a list"""
		sut = concordance.Concordance()
		sut.addInstanceOfWordAtLine("Carta", 1)
		sut.addInstanceOfWordAtLine("Magna", 12)
		expectedConcordanceEntryList = ["carta: 1", "magna: 12"]
		self.assertEqual(expectedConcordanceEntryList, sut.allEntries())

	def test_allEntries_returnsEachWordWhichHasBeenAddedToTheConcordanceInAlphabeticalOrderOfWord(self):
		"""When we get all the entries, they should be returned in alphabetical order even if they weren't added that way"""
		sut = concordance.Concordance()
		sut.addInstanceOfWordAtLine("Magna", 12)
		sut.addInstanceOfWordAtLine("Carta", 12)
		sut.addInstanceOfWordAtLine("John", 1)
		expectedConcordanceEntryList = ["carta: 12", "john: 1", "magna: 12"]
		self.assertEqual(expectedConcordanceEntryList, sut.allEntries())


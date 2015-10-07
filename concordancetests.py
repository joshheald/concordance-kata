import unittest
import concordance

class ConcordanceTests(unittest.TestCase):
	def test_add_instance_of_word_at_line_canAddAWordToTheConcordance(self):
		"""Test that we can add a new word to the concordance"""
		expected_word = "WordFromText"
		sut = concordance.Concordance()
		sut.add_instance_of_word_at_line(word=expected_word)

	def test_add_instance_of_word_at_line_canAddAWordToTheConcordanceWithALine_number(self):
		"""Test that we can add a new word with associated line number to the concordance"""
		expected_line_number = 15
		sut = concordance.Concordance()
		sut.add_instance_of_word_at_line(line_number=expected_line_number)

	def test_add_instance_of_word_at_line_doesNotAddToTheConcordanceIfNoWordIsProvided(self):
		"""The method has defaults to make it easier to test, but really this should be refactored out"""
		sut = concordance.Concordance()
		sut.add_instance_of_word_at_line(line_number=1)
		self.assertEqual([], sut.all_entries())

	def test_add_instance_of_word_at_line_doesNotAddToTheConcordanceIfNoLine_numberIsProvided(self):
		"""The method has defaults to make it easier to test, but really this should be refactored out"""
		sut = concordance.Concordance()
		sut.add_instance_of_word_at_line(word="Bruce")
		self.assertEqual([], sut.all_entries())

	def test_add_instance_of_word_at_line_doesNotAddDuplicateLine_numbersWhenProvided(self):
		"""Words may be present more than once on a line, but we don't want to note that line number more than once"""
		sut = concordance.Concordance()
		sut.add_instance_of_word_at_line(word="Samwell", line_number=2)
		sut.add_instance_of_word_at_line(word="Samwell", line_number=2)
		self.assertEqual("samwell: 2", sut.entry_for_word("samwell"))

	def test_add_instance_of_word_at_line_isCaseInsensitive(self):
		"""This, this, and THIS are all the same word, so we should group all instances together"""
		sut = concordance.Concordance()
		sut.add_instance_of_word_at_line(word="this", line_number=3)
		sut.add_instance_of_word_at_line(word="This", line_number=4)
		sut.add_instance_of_word_at_line(word="THIS", line_number=7)
		self.assertEqual(["this: 3, 4, 7"], sut.all_entries())

	def test_entry_for_word_returnsNoneWhenTheWordHasNotBeenStored(self):
		"""If we don't store a given word, we can't produce an entry for it, and None is better than an empty string to represent that"""
		expected_word = "what's"
		sut = concordance.Concordance()
		self.assertIsNone(sut.entry_for_word(expected_word))

	def test_entry_for_word_canRetrieveTheLine_numberStoredForAWord(self):
		"""We should be able to look up our concordance entry for a single word"""
		expected_line_number = 42
		expected_word = "meaning"
		sut = concordance.Concordance()
		sut.add_instance_of_word_at_line(word=expected_word, line_number=expected_line_number)
		expected_concordance_entry = "meaning: 42"
		self.assertEqual(expected_concordance_entry, sut.entry_for_word(expected_word))

	def test_entry_for_word_canRetrieveMultipleLine_numbersStoredForAWord(self):
		"""The concordance entry we produce should have all the line numbers we store for a word"""
		expected_line_numbers = [1, 4, 8, 42]
		expected_word = "life"
		sut = concordance.Concordance()
		for line_number in expected_line_numbers:
			sut.add_instance_of_word_at_line(word=expected_word, line_number=line_number)
		expected_concordance_entry = "life: 1, 4, 8, 42"
		self.assertEqual(expected_concordance_entry, sut.entry_for_word(expected_word))

	def test_entry_for_word_canRetrieveTheLine_numberStoredForAWordInNumericalOrder(self):
		"""Potentially, a string could be read in reverse or arbitrary order - we should always return in ascending order"""
		inputLine_numbers = [42, 4, 9, 2, 17]
		expected_word = "and"
		sut = concordance.Concordance()
		for line_number in inputLine_numbers:
			sut.add_instance_of_word_at_line(word=expected_word, line_number=line_number)
		expected_concordance_entry = "and: 2, 4, 9, 17, 42"
		self.assertEqual(expected_concordance_entry, sut.entry_for_word(expected_word))

	def test_entry_for_word_isCaseInsensitive(self):
		"""That, that, and THAT are all the same word, so we should be able to get the combined entry for them whichever we use as a lookup key"""
		sut = concordance.Concordance()
		sut.add_instance_of_word_at_line(word="something", line_number=8)
		self.assertEqual("something: 8", sut.entry_for_word("SOMEthing"))

	def test_all_entries_returnsEachWordWhichHasBeenAddedToTheConcordance(self):
		"""When we get all the entries, every word we've added should have an entry returned in a list"""
		sut = concordance.Concordance()
		sut.add_instance_of_word_at_line("Carta", 1)
		sut.add_instance_of_word_at_line("Magna", 12)
		expected_concordance_entryList = ["carta: 1", "magna: 12"]
		self.assertEqual(expected_concordance_entryList, sut.all_entries())

	def test_all_entries_returnsEachWordWhichHasBeenAddedToTheConcordanceInAlphabeticalOrderOfWord(self):
		"""When we get all the entries, they should be returned in alphabetical order even if they weren't added that way"""
		sut = concordance.Concordance()
		sut.add_instance_of_word_at_line("Magna", 12)
		sut.add_instance_of_word_at_line("simple", 2)
		sut.add_instance_of_word_at_line("Carta", 12)
		sut.add_instance_of_word_at_line("John", 1)
		sut.add_instance_of_word_at_line("Andrew", 17)
		sut.add_instance_of_word_at_line("bowl", 9)
		expected_concordance_entryList = ["andrew: 17", "bowl: 9", "carta: 12", "john: 1", "magna: 12", "simple: 2"]
		self.assertEqual(expected_concordance_entryList, sut.all_entries())


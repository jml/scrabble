import unittest

from scrabble import (
    is_anagram, is_subanagram, factorial, find_anagrams_by_dictionary,
    find_anagrams_by_permutations, generate_permutations)


class TestSubanagram(unittest.TestCase):
    """A 'subanagram' is a word formed from a subsequence of letters of
    another word.
    """

    def assertIsSubanagram(self, word1, word2):
        self.assertTrue(
            is_subanagram(word1, word2),
            "%r is not a sub-anagram of %r" % (word1, word2))

    def assertIsNotSubanagram(self, word1, word2):
        self.assertFalse(
            is_subanagram(word1, word2),
            "%r is a sub-anagram of %r" % (word1, word2))

    def test_equalWords(self):
        self.assertIsSubanagram('foo', 'foo')
        self.assertIsNotSubanagram('bar', 'foo')
        self.assertIsSubanagram('of', 'foo')
        self.assertIsNotSubanagram('foo', 'of')
        self.assertIsSubanagram('of', 'fog')
        self.assertIsNotSubanagram('go', 'foo')
        self.assertIsSubanagram('ofo', 'foo')
        self.assertIsNotSubanagram('fooo', 'foo')


class TestAnagram(unittest.TestCase):

    def assertIsAnagram(self, word1, word2):
        self.assertTrue(
            is_anagram(word1, word2),
            "%r is not an anagram of %r" % (word1, word2))
        self.assertTrue(
            is_anagram(word2, word1),
            "%r is not an anagram of %r" % (word1, word2))

    def assertIsNotAnagram(self, word1, word2):
        self.assertFalse(
            is_anagram(word1, word2),
            "%r is an anagram of %r" % (word1, word2))
        self.assertFalse(
            is_anagram(word2, word1),
            "%r is an anagram of %r" % (word1, word2))

    def test_differentLength(self):
        self.assertIsNotAnagram('foo', 'f')

    def test_sameWord(self):
        self.assertIsAnagram('foo', 'foo')

    def test_sameLengthNotAnagram(self):
        self.assertIsNotAnagram('foo', 'bar')
        self.assertIsNotAnagram('fog', 'foo')

    def test_anagrams(self):
        self.assertIsAnagram('foo', 'oof')


class TestFactorial(unittest.TestCase):

    def test_one(self):
        self.assertEqual(1, factorial(1))

    def test_zero(self):
        self.assertEqual(1, factorial(0))

    def test_n(self):
        self.assertEqual(120, factorial(5))


class TestPermutations(unittest.TestCase):

    def test_singleton(self):
        self.assertEqual([[1]], list(generate_permutations([1])))

    def test_doubleton(self):
        self.assertEqual([[1, 2], [2, 1]], list(generate_permutations([1, 2])))

    def test_triple(self):
        self.assertEqual(
            [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]],
            list(generate_permutations([1, 2, 3])))


class TestFindAnagrams(unittest.TestCase):
    # Dictionary: act, cat, dog
    # Anagrams of 'act'

    def setUp(self):
        self.dictionary = set(['act', 'cat', 'dog'])
        self.anagram_finders = []

    def assertAnagramsAre(self, word, anagrams):
        for finder in self.anagram_finders:
            self.assertEqual(set(anagrams), finder(self.dictionary, word))

    def test_nonWord(self):
        self.assertAnagramsAre('foo', [])

    def test_oneAnagram(self):
        self.assertAnagramsAre('dog', ['dog'])

    def test_anagrams(self):
        self.assertAnagramsAre('tac', ['act', 'cat'])

import unittest

from hw4 import *


# test file for homework 4

# these are the student tests. the autograder tests will be considerably more rigorous

class tester(unittest.TestCase):
    def test_is_unique(self):
        self.assertTrue(is_unique('g'))
        self.assertFalse(is_unique('hello world'))

    def test_count_anagrams(self):
        self.assertEquals(count_anagrams(['19cs6', 'apple', '1s9c6', 'dog', 'cs1962', 'sc961'], 'cs196'), 3)
        self.assertEquals(count_anagrams(['aabbcc', 'abcabc', 'abcdef', 'defghi'], 'golf'), 0)

    def test_anagram_of_palindrome(self):
        self.assertTrue(anagram_of_palindrome('arortot'))
        self.assertFalse(anagram_of_palindrome('asdf'))
        self.assertFalse(anagram_of_palindrome('thanks for the memories shotaro'))

    def test_reverse_dictionary(self):
        self.assertEquals(reverse_dictionary({'a': 1}), {1: 'a'})
        self.assertEquals(reverse_dictionary({'a': 1, 'b': 2}), {1: 'a', 2: 'b'})

    def test_alphabet_finder(self):
        test = 'abcdefghijklmnopqrstuvwxyz'
        result = 'abcdefghijklmnopqrstuvwxyz'
        self.assertEquals(alphabet_finder(test), result)

        test = 'hi!abcdefghijklmnopqrstuvwxy you wont see a z till there!'
        result = 'hi!abcdefghijklmnopqrstuvwxy you wont see a z'
        self.assertEquals(alphabet_finder(test), result)

    def test_happy_numbers(self):
        self.assertEquals(happy_numbers(8), 2468 // 1234)
        self.assertEquals(happy_numbers(15), 4)
        self.assertEquals(happy_numbers(10 ** 5), 14377)


if __name__ == "__main__":
    unittest.main(module=__name__, buffer=True, exit=False)

import sys
from contextlib import contextmanager
import math
import unittest
from test_common import *
import task6


class TestTask6(TestCase):
    def test_addfile(self):
        with self.vis():
            freq = task6.Freq()
            freq.add_file('words_simple.txt')
            for word in ['this', 'dictionary', 'words']:
                self.assertEqual(freq.word_frequency[word], 1,
                                 "Incorrect frequency.")

        with self.vis():
            freq = task6.Freq()
            freq.add_file('words_dup.txt')
            for (word, count) in [('words', 3), ('and', 2)]:
                self.assertEqual(freq.word_frequency[word], count,
                                 "Incorrect frequency.")

        # ------------------------MY TESTS------------------------------
        # Invalid input: file is not in the same file/ file does not exist
        with self.vis():
            freq = task6.Freq()
            with self.assertRaises(FileNotFoundError, msg="add_file should raise exception if file not found"):
                freq.add_file('file_that_cannot_be_found.txt')

        # Valid input
        # Takes out all whitespace (empty lines and spaces)
        with self.vis():
            freq = task6.Freq()
            freq.add_file('words_empty.txt')
            for word in ['this', 'file', 'contains', 'an', 'empty', 'line', 'and', 'some', 'space']:
                self.assertEqual(freq.word_frequency[word], 1, "Incorrect frequency.")

        # Adding two files to the hash table
        with self.vis():
            freq = task6.Freq()
            freq.add_file('words_simple.txt')
            freq.add_file('words_dup.txt')
            for (word, count) in [('this', 2), ('is', 1), ('words', 4), ('and', 2)]:
                self.assertEqual(freq.word_frequency[word], count, "Incorrect frequency.")

        self.assertTrue(self.check_okay("addfile"))

    def test_rarity(self):
        with self.vis():
            freq = task6.Freq()
            freq.add_file('words_freq.txt')

            self.assertEqual(freq.rarity('a'), 0,
                             "Incorrect rarity.")

        with self.vis():
            self.assertEqual(freq.rarity('fish'), 2,
                             "Incorrect rarity.")

        # -------------------------MY TESTS-------------------------------
        # Valid input
        # Checking for a misspelled word
        with self.vis():
            self.assertEqual(freq.rarity('fissh'), 3, "Incorrect rarity.")

        # Invalid input
        # Word must be of type string otherwise it should raise TypeError
        with self.vis():
            with self.assertRaises(TypeError, msg="word should only be of type string"):
                freq.rarity(32)

        self.assertTrue(self.check_okay("rarity"))


if __name__ == '__main__':
    unittest.main()

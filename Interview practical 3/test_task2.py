import sys
from contextlib import contextmanager
import math
import unittest
from test_common import *
import task1
import task2
import builtins


class TimedOutExn_(Exception):
    pass


class TestTask2(TestCase):
    def test_load(self):
        with self.vis():
            table = task1.HashTable()
            task2.load_dictionary(table, "words_simple.txt", 10)
            self.assertEqual(count_nonempty_buckets(table), 6)

        with self.vis():
            table = task1.HashTable()
            task2.load_dictionary(table, "words_empty.txt", 10)
            self.assertEqual(count_nonempty_buckets(table), 11, "Failed to handle empty line or whitespace.")

        self.assertTrue(self.check_okay("load_dictionary"))

        # ---------------MY TESTS----------------------
        x = task1.HashTable(3, 107)
        # Valid inputs
        # Checking that time returned is less than the max_time given
        self.assertTrue(task2.load_dictionary(x, 'Testfile.txt', 130) <= 130, "time returned should be less than max_time")

        # Invalid inputs
        # TimeOutError should be raised when the timer exceeds max_time given
        with self.assertRaises(builtins.TimeoutError, msg="TimeOutError should be raised"):
            task2.load_dictionary(x, 'english_small.txt', 1)

    def test_load_timeout(self):
        with self.vis("load without max_time"):
            table = task1.HashTable()
            task2.load_dictionary(table, "words_simple.txt")

        with self.vis("failed to apply timeout"):
            table = task1.HashTable(100000, 1)
            with self.assertRaises(Exception, msg = "reading too many words should time out."):
                try:
                    self.with_deadline(10, task2.load_dictionary, (table, "english_small.txt", 1))
                except TimedOutExn_:
                    pass

        self.assertTrue(self.check_okay("load_dictionary timeout"))

    def test_load_time(self):
        with self.vis("reporting words"):
            (words, time) = self.with_deadline(5, task2.load_dictionary_time, (31, 100, "words_simple.txt", 10))
            self.assertEqual(words, 6)

        self.assertTrue(self.check_okay("load_dictionary time"))


if __name__ == '__main__':
    unittest.main()

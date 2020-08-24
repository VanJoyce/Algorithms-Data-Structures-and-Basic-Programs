import sys
from contextlib import contextmanager
import math
import unittest
from test_common import *
import task3
import task2


class TestTask3(TestCase):
    def test_statistics(self):
        table = task3.HashTable(1024, 1)

        with self.vis("testing statistics"):
            for key in ["abcdef", "defabc"]:
                table[key] = 1
            stats = table.statistics()
            self.assertEqual(stats, (1, 1, 1, 0), "incorrect statistics")

        with self.vis():
            for key in ["acbedf"]:
                table[key] = 1
            stats = table.statistics()
            self.assertEqual(stats, (2, 3, 2, 0), "incorrect statistics")

        # -------------- MY TESTS -----------------------
        x = task3.HashTable(2, 107)
        with open('Testfile.txt') as file:
            for word in file:
                if word[-1] == "\n":
                    word = word[:-1]
                x[word] = 1

        self.assertEqual(x.rehash_count, 1, msg="rehash_count should be 1")
        self.assertEqual(x.collision, 3, msg="collision should be 3")
        self.assertEqual(x.probe_max, 2, msg="probe_max should be 2")
        self.assertEqual(x.probe_total, 4, msg="probe_total should be 4")

        self.assertTrue(self.check_okay("statistics"))

    def test_load_statistics(self):
        with self.vis("reporting words"):
            (w, _, _, _, _, _) = self.with_deadline(1, task3.load_dictionary_statistics, (1, 1024, "words_perm.txt", 10))
            self.assertEqual(w, 5, "incorrect word count")

        self.assertTrue(self.check_okay("load_statistics"))


if __name__ == '__main__':
    unittest.main()

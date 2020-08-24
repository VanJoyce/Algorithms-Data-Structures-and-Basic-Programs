import sys
from contextlib import contextmanager
import math
import unittest
from test_common import *
import task1
import itertools


class TestTask1(TestCase):
    def test_init(self):
        with self.vis("empty init"):
            x = task1.HashTable()
        with self.vis("init with size and base"):
            z = task1.HashTable(800, 2398)

        assert self.check_okay("init")

    def test_hash(self):

        x = task1.HashTable(1024, 17)
        for (key, expect) in [("", 0),
                              ("abcdef", 389),
                              ("defabc", 309)]:
            with self.vis():
                self.assertEqual(x.hash(key), expect, msg=f"Unexpected hash with base 17 and key {key}.")

        assert self.check_okay("hash")

    # The tests for __contains__ and __getitem__ use __setitem__, so we don't make any assumptions
    # about the underlying array representation. Remember to define your own tests for __setitem__
    # (and rehash)
    def test_contains(self):
        x = task1.HashTable(1024, 1)

        with self.vis():
            self.assertFalse("abcdef" in x, "False positive in __contains__ for empty table.")

        with self.vis("unexpected failure in setitem"):
            x["abcdef"] = 18
            x["definitely a string"] = None
            x["abdcef"] = "abcdef"

        for key in ["abcdef", "definitely a string", "abdcef"]:
            with self.vis():
                self.assertTrue(key in x, "False negative in __contains__ for key {}".format(key))

        assert self.check_okay("contains")

    def test_getitem(self):
        x = task1.HashTable(1024, 1)

        with self.vis():
            with self.assertRaises(KeyError, msg="x[key] should raise KeyError for missing key."):
                elt = x["abcdef"]

        with self.vis("unexpected failure in setitem"):
            x["abcdef"] = 18
            x["definitely a string"] = None

        with self.vis():
            self.assertEqual(x["abcdef"], 18, msg = "Read after store failed.")

        x["abdcef"] = 22

        assert self.check_okay("getitem")

    def test_setitem(self):
        # -------------------------MY TESTS---------------------------
        x = task1.HashTable(3, 107)

        # Check for invalid input: key is an integer
        with self.assertRaises(TypeError, msg="x[key] should raise TypeError for integer key"):
            x[11] = 3

        # Check for valid input
        # Can insert key and value
        x["dba"] = 351
        self.assertTrue(x["dba"] == 351, msg="Value 351 should be inserted into hash table with the given key")
        # Can change value at the same key
        x["dba"] = 401
        self.assertTrue(x["dba"] == 401, msg="Value should be changed")
        # when collision occurs, (key, value) should be inserted at next empty space
        x["cda"] = 395  # hash value of 'cda' is supposed to be 0 (same with 'dba')
        self.assertFalse(x["dba"] == 395, msg="Value should not be same as x['cda']")
        self.assertTrue(x.table[1] == ("cda", 395), msg="Collision not resolved")
        # when hash table is full, its capacity should be updated using the rehash method
        x["defg"] = 321
        x["ghij"] = 256
        x["lmno"] = 965
        self.assertEqual(len(x.table), 7, msg="Table capacity is not updated")
        self.assertTrue(x["lmno"] == 965, msg="Data not inserted after table is full")

        assert self.check_okay("setitem")

    def test_rehash(self):
        # ---------------------------MY TESTS---------------------------------
        x = task1.HashTable(3)

        x["abcd"] = 1
        x["acbd"] = 2
        x["dabc"] = 3
        x["acdb"] = 4

        # Valid inputs
        # Checking if the hash table capacity is updated correctly
        self.assertTrue(len(x.table) == 7, "hash table capacity updated wrongly")

        # Invalid input
        # Checking if cannot rehash because no number in Primes is bigger than hash table capacity
        # WARNING: This test takes a long time to run
        string = "abcdefghijklmnopqrs"
        permutations = [''.join(perm) for perm in itertools.permutations(string, 10)]
        with self.assertRaises(ValueError, msg="There shouldn't be a number in Primes that is bigger"):
            for perm in permutations:
                x[perm] = 1

        assert self.check_okay("rehash")


if __name__ == '__main__':
    unittest.main()

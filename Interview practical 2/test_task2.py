import math
import unittest
from test_common import *
import task2

class TestTask2(unittest.TestCase):
    def test_init_mine(self):
        # Check parameter sizes less than 40 have sizes initialised at 40
        test1 = task2.ListADT(30)
        self.assertEqual(len(test1.the_array), 40, msg="Input for size less than 40 should have become 40.")

        # Test if parameter is negative integer
        with self.assertRaises(ValueError, msg="Size should be more than 0"):
            task2.ListADT(-4)

    def test_insert_mine(self):
        # Check that cannot insert at the index immediately after range
        test1 = task2.ListADT(50)
        with self.assertRaises(IndexError, msg="Should be able to insert at -1."):
            test1.insert(2, "hello")

        # Check cannot insert Nonetype
        with self.assertRaises(TypeError, msg="index cannot be nonetype"):
            test1.insert(None, 4)

        # Check correct growth
        for i in range(51):
            test1.append(1)
        self.assertEqual(len(test1.the_array), math.ceil(1.9*50), msg="Size didn't increase correctly.")

    def test_delete_mine(self):
        test1 = task2.ListADT(60)
        append(test1, [3, 2, 1, 5])

        # Check that it shrank correctly (size cannot be less than 40)
        test1.delete(3)
        self.assertEqual(len(test1.the_array), 40, msg="Size didn't shrink correctly.")

        # Check that index can only be integer
        with self.assertRaises(TypeError, msg="Array as parameter should fail."):
            test1.delete([0, 1])

    def test_append_mine(self):
        test1 = task2.ListADT(10)
        # Check it doesn't grow when it is not yet full
        for i in range(40):
            test1.append(1)
        self.assertEqual(len(test1.the_array), 40, msg="It grew when it's not supposed to.")

        # Check it grows as soon as it's full
        test1.append(1)
        self.assertEqual(len(test1.the_array), math.ceil(1.9*40), msg="It grew when it's not supposed to.")

    def test_insert(self):
        x = task2.ListADT(10)

        ## This should not fail.
        append(x, [1 for i in range(1000)])

        ## If the ListADT has renamed the underlying array, or used some other
        ## representation, we can't realy test whether resizing is handled correctly.
        if not hasattr(x, "the_array"):
            raise AttributeError("could not identify underlying array for the ListADT.")

        y = task2.ListADT(10)

        # If we gave a smaller constant, should have become 40.
        self.assertEqual(len(y.the_array), 40, "Allocated array below threshold.")

        # ... and with rounding
        y = task2.ListADT(44)
        for i in range(45):
            y.insert(i, i)
        self.assertEqual(len(y.the_array), 84, "Incorrect grow.") # math.ceil(44 * 1.9)

        # Check shrinking
        for i in range(25):
            y.delete(len(y)-1)
        self.assertTrue(len(y.the_array) == 42, "Incorrect shrink.")


if __name__ == '__main__':
    unittest.main()

import math
import unittest
from test_common import *
import task1

class TestTask1(unittest.TestCase):
    # Check that initialisation doesn't fail
    def test_init(self):
        y = task1.ListADT(10)

    def test_init_mine(self):
        test1 = task1.ListADT()
        # Check that size of array is as default when not specified
        self.assertEqual(len(test1.the_array),  100)

        # Test if parameter is not integer
        with self.assertRaises(TypeError, msg = "Size should only be of type integer"):
            task1.ListADT("one")

    def test_str(self):
        # Check str for non-empty lists
        x = task1.ListADT(10)
        append(x, [1, 2, 3])
        self.assertEqual(str(x).strip('\n'), '1\n2\n3')

    def test_str_mine(self):
        test1 = task1.ListADT()

        # Check if empty list returns emtpy string
        self.assertEqual(str(test1), "")

        # Check for non-empty lists
        append(test1, ["cat","dog","goat"])
        self.assertEqual(str(test1).strip('\n'), 'cat\ndog\ngoat')

    def test_len(self):
        # Test length of an empty list
        x = task1.ListADT(20)
        self.assertEqual(len(x), 0, msg="Length of empty list should be 0")
        # And for a non-empty one
        x.insert(0, 2)
        self.assertEqual(len(x), 1, msg="Length should be 1")

    def test_len_mine(self):
        test1 = task1.ListADT()

        # Test with empty list
        self.assertEqual(len(test1), 0, msg="Length should be 0 for empty lists.")

        # Test with non-empty list with a few elements
        append(test1, [1,0,71,2])
        self.assertEqual(len(test1), 4, msg="Incorrect length.")

    def test_get(self):
        x = task1.ListADT(10)
        append(x, [0, 1, 2, 3, 4])

        # Check both positive and negative indices
        for index, value in [ (1, 1), (-2, 3)]:
            self.assertEqual(x[index], value, msg="Incorrect _getitem_.")

    def test_get_mine(self):
        test1 = task1.ListADT()
        append(test1, [1, 5, 7, 3])

        # Check if index is not integer
        with self.assertRaises(TypeError, msg="Index should only be of integer type."):
            test1["try"]

        # Check index out of range
        with self.assertRaises(IndexError, msg="Index out of range"):
            test1[4]    #len(self)
            test1[-5]   #-len(self)-1

        # Test positive index at the beginning of list
        self.assertEqual(test1[0], 1, msg="Doesn't get correct element with positive index.")
        # Test positive index at the end of list
        self.assertEqual(test1[3], 3, msg="Doesn't get correct element with positive index.")
        # Test negative index at the end of list
        self.assertEqual(test1[-1], 3, msg="Doesn't get correct element with negative index.")
        # Test negative index at the beginning of list
        self.assertEqual(test1[-4], 1, msg="Doesn't get correct element with negative index.")

    def test_set(self):
        x1 = task1.ListADT(10)
        append(x1, [1, 2, 3])
        # Testing assignment (and implicitly _getitem_)
        x1[0] = 8
        self.assertTrue(equal(x1, [8, 2, 3]), msg = "Incorrect assignment at index 0")

    def test_set_mine(self):
        test1 = task1.ListADT()
        # Test with index that is out of range
        with self.assertRaises(IndexError, msg="Index out of range"):
            test1[1] = 3    # len(self)
            test1[-1] = 2   # -len(self)-1

        append(test1, [6,9,5])
        # Test with positive index at end of list
        test1[2] = 10
        self.assertTrue(equal(test1, [6,9,10]), msg="Positive index at the end cannot be set.")
        # Test with positive index in the middle of the list
        test1[1] = 4
        self.assertTrue(equal(test1, [6,4,10]), msg="Incorrect assignment at index 1.")
        # Test negative index at beginning of the list
        test1[-1] = 2
        self.assertTrue(equal(test1, [6, 4, 2]), msg="Incorrect assignment at index -1.")
        # Test negative index at end of the list
        test1[-3] = 8
        self.assertTrue(equal(test1, [8, 4, 2]), msg="Incorrect assignment at index -3.")

    def test_eq(self):
        x1 = task1.ListADT(10)
        x2 = task1.ListADT(20)
        # Check equality for lists of different size
        self.assertTrue(x1 == x2, msg =  "Lists with different capacity should still be equal.")
        # Check that equality tests for List type.
        append(x1, [1, 2, 3])
        self.assertFalse(x1 == [1, 2, 3], "Equality test doesn't check type.")

    def test_eq_mine(self):
        # Check lists with exact same elements and same capacities
        test1 = task1.ListADT(10)
        test2 = task1.ListADT(10)
        append(test1, [5, 6, 7, 8])
        append(test2, [5, 6, 7, 8])
        self.assertTrue(test1 == test2, msg="Two lists should be equal.")

        # Check lists that have different elements but same length and capacity
        test3 = task1.ListADT(10)
        append(test3, [5, 4, 3, 9])
        self.assertFalse(test1 == test3, msg="The two lists should not be equal.")

    def test_insert(self):
        x = task1.ListADT(10)
        # Check insertion at beginning
        x.insert(0, 1)
        self.assertTrue(equal(x, [1]), msg =  "Insertion in empty list failed")
        # And at end.
        x.insert(1, 2)
        self.assertTrue(equal(x, [1, 2]), msg =  "Insertion at end failed")

        # Check insertion out-of-bounds
        with self.assertRaises(IndexError, msg = "Inserting out of bounds should fail"):
            x.insert(6, 8)

        with self.assertRaises(Exception, msg = "Inserting above capacity should raise an exception."):
            append(x, [1 for i in range(20) ])

    def test_insert_mine(self):
        test1 = task1.ListADT()
        append(test1, [4, 2, 6])

        # Insertion with negative indices
        # Check if can insert at the back with negative indices
        test1.insert(-1, 3)
        self.assertTrue(equal(test1, [4, 2, 6, 3]), msg="Inserting with index -1 should append to the back.")
        # Check if can insert at the beginning of the list (-len(self)-1)
        test1.insert(-5, 1)
        self.assertTrue(equal(test1, [1, 4, 2, 6, 3]), msg="Inserting at index -5 should be alright")

        # Check index is an integer
        with self.assertRaises(TypeError, msg="Index cannot be a string."):
            test1.insert("two", 3)

    def test_delete(self):
        x = task1.ListADT(10)
        append(x, [0,1,2,3,4,5])
        # Test deletion from the middle.
        x.delete(2)
        self.assertTrue(equal(x, [0,1,3,4,5]), msg =  "Delete from middle failed")
        # And from a negative index.
        x.delete(-4)
        self.assertTrue(equal(x, [0,3,4,5]), msg =  "Negative deletion failed")

    def test_delete_mine(self):
        test1 = task1.ListADT()

        # Test empty list
        with self.assertRaises(Exception, msg="Should not be able to delete from an empty list."):
            test1.delete(0)

        append(test1, [3, 1, 4])
        # Test deletion with index just over range
        with self.assertRaises(IndexError, msg="Should not be able to delete over range."):
            test1.delete(-4)
            test1.delete(3)

        # Test deletion with negative index at ends of list
        test1.delete(-1)
        self.assertTrue(equal(test1, [3, 1]), msg="Should be able to delete from index -1")
        test1.delete(-2)
        self.assertTrue(equal(test1, [1]), msg="Should be able to delete from index -2")

if __name__ == '__main__':
    unittest.main()

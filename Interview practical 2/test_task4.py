import math
import unittest
from test_common import *
import task2
import task4

class TestTask4(unittest.TestCase):
    def test_read(self):
        ed = task4.Editor()
        ed.read_filename('TestFile.txt')
        self.assertTrue(equal_lines(ed, test_content), msg =  "File not correctly read.")

    def test_read_mine(self):
        ed = task4.Editor()
        # Test if reading file correctly
        ed.read_filename('test1.txt')
        file = open('test1.txt','r')
        lst = []
        for line in file:
            lst.append(line)
        file.close()
        self.assertTrue(equal_lines(ed, [l.strip('\n') for l in lst]), msg="File not correctly read.")

        # Test with other random string
        with self.assertRaises(FileNotFoundError, msg="No such file exists in the folder."):
            ed.read_filename('random')

    def test_print(self):
        pass

    def test_print_mine(self):
        ed = task4.Editor()
        # Raises error when given line number is 0
        with self.assertRaises(ValueError, msg="No such thing as line 0."):
            ed.print_num("0")

    def test_delete(self):
        ed = task4.Editor()
        ed.read_filename('TestFile.txt')
        ed.delete_num("1")
        self.assertTrue(equal_lines(ed, test_content[1:]), msg =  "Failed to delete first line.")

        for index in ["-5"]:
            with self.assertRaises(IndexError, msg = "Deleting out-of-bounds lines should fail."):
                ed.read_filename('TestFile.txt')
                ed.delete_num(index)

    def test_delete_mine(self):
        ed = task4.Editor()
        ed.read_filename('TestFile.txt')
        # Check index just outside of range raises error
        with self.assertRaises(IndexError, msg="Can't delete outside of the range."):
            ed.delete_num("5")

        # Check that all lines are deleted when no line number is given
        ed.delete_num("")
        self.assertTrue(equal(ed.text_lines, []), msg="All lines should be deleted.")

    def test_insert(self):
        ed = task4.Editor()
        ed.insert_num_strings("1", ToListADT(task2.ListADT, [test_content[0]]))
        self.assertTrue(equal_lines(ed, [test_content[0]]), msg =  "Failed to insert single line.")

        ed = task4.Editor()
        ed.insert_num_strings("-1", ToListADT(task2.ListADT, [test_content[2], test_content[3]]))
        self.assertTrue(equal_lines(ed, [test_content[2], test_content[3]]), msg =  "Incorrect handling of negative insertion")

    def test_insert_mine(self):
        ed = task4.Editor()
        # Invalid case: numline given is 0
        with self.assertRaises(ValueError, msg="No such thing as line 0."):
            ed.insert_num_strings("0", ["hello", "there"])

        ed.insert_num_strings("1", ["hello", "there"])
        # Insert with negative index at the edge
        ed.insert_num_strings("-3", ["Why,"])
        self.assertTrue(equal_lines(ed, ["Why,", "hello", "there"]), msg="Negative index does not work.")

if __name__ == '__main__':
    unittest.main()
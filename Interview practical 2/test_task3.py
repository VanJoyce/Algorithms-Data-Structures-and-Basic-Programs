import math
import unittest
from test_common import *
import task3

class TestTask3(unittest.TestCase):
    def test_read_file(self):
        test_lines = task3.read_text_file('TestFile.txt')
        self.assertEqual([ l.strip('\n') for l in ToList(test_lines) ], test_content, msg = "File not correctly read.")


    def test_read_file_mine(self):
        # Check if it can read a bigger text file
        test1 = task3.read_text_file('test2.txt')

        file = open('test2.txt', 'r')
        lst = []
        for line in file:
            lst.append(line)
        file.close()
        self.assertEqual([ l.strip('\n') for l in ToList(test1) ], [ l.strip('\n') for l in lst ], msg = "File not correctly read.")

        # Test with a non-existent file
        with self.assertRaises(FileNotFoundError, msg="The file cannot be found in the same folder."):
            task3.read_text_file('fake.txt')


if __name__ == '__main__':
    unittest.main()

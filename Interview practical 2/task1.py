#!/usr/bin/python3
class ListADT:

    def __init__(self, size=100):
        """
        Creates an instance of the class ListADT and initialises its instance variables.

        :param size: size of the list (the maximum number of items in the list)
        :pre-condition: size must be a positive integer
        :post-condition: An empty list of specified size is created
        :complexity: best and worst case are both O(1)
        """
        if not isinstance(size, int):
            raise TypeError("Size specified is not an integer")
        elif size < 0:
            raise ValueError("No such thing as negative size")
        self.length = 0
        self.the_array = [None] * size

    def __str__(self):
        """
        Prints out the list with one item per line.

        :return: a string representation of the list
        :post-condition: The string has only one item of the list per line
        :complexity: best case is O(1) when the list is empty and worst case is O(n) where n is the length of the list
        """
        out_string = ""
        for index in range(self.length):
            out_string += str(self.the_array[index]) + "\n"
        return out_string

    def __len__(self):
        """
        Returns the length of the list.

        :return: the length of the list
        :complexity: best case and worst case are both O(1)
        """
        return self.length

    def __getitem__(self, index):
        """
        Returns the item at the given index in the list.

        :param index: index of the list to get the item from
        :return: item at given index in the list
        :pre-condition: index given is within the range -len(self) to len(self)-1 and index is of integer type
        :post-condition: list isn't changed
        :complexity: best and worst case are both O(1)
        """
        if not isinstance(index, int):
            raise TypeError("Index is not an integer")
        if 0 <= index < self.length:
            item = self.the_array[index]
        elif -self.length <= index < 0:
            item = self.the_array[self.length + index]
        else:
            raise IndexError('Index is out of range')
        return item

    def __setitem__(self, index, item):
        """
        Sets the value at index in the list to be item.

        :param index: index of the list where the value is to be set
        :param item: the value of the element in the list
        :return: None
        :pre-condition: index given is within the range -len(self) to len(self)-1 and index is of integer type
        :post-condition: the value at index of the list is item
        :complexity: best and worst case are both O(1)
        """
        if not isinstance(index, int):
            raise TypeError("Index is not an integer")
        if 0 <= index < self.length:
            self.the_array[index] = item
        elif -self.length <= index < 0:
            self.the_array[self.length + index] = item
        else:
            raise IndexError('Index is out of range')

    def __eq__(self, other):
        """
        Checks if the two lists are instances of ListADT and they have exactly the
        same elements in the same order. Both may have different capacities.

        :param other: a list
        :return: True if both self and other are instances of ListADT and have the
                 same elements in the same order and False otherwise
        :pre-condition: other is an instance of ListADT
        :post-condition: both lists remain unchanged
        :complexity: best case is O(1) when other is not an instance of ListADT or length is not equal and
                     worst case is O(n) where n is the length of both lists
        """
        if isinstance(other, ListADT) and self.length == other.length:
            for index in range(self.length):
                if self.the_array[index] != other[index]:
                    return False
            return True
        else:
            return False

    def insert(self, index, item):
        """
        Inserts an item into a given index of the list.

        :param index: index of the list in which you want to insert item into
        :param item: value to be inserted into the list
        :return: None
        :pre-condition: the list is not full, and index is within the range -len(self)-1 to len(self) and is an integer
        :post-condition: every item from index to the end of the list is shifted one space
                         to the right nad the item is inserted at index. Length of the list
                         has increased by 1.
        :complexity: best case is O(1) when item is inserted at the back of the list and worst case is O(n) where n
                     is the length of the list
        """
        if not isinstance(index, int):
            raise TypeError("index should be of type integer")
        if not self.is_full():
            if -self.length-1 <= index < 0:
                index += self.length + 1
            if index > self.length or index < -self.length-1:
                raise IndexError('Not a valid index')
            for i in range(self.length-1, index-1, -1):
                self.the_array[i + 1] = self.the_array[i]
            self.the_array[index] = item
            self.length += 1
        else:
            raise Exception('List is full')

    def delete(self, index):
        """
        Deletes item at given index of the list.

        :param index: index of item to be deleted
        :return: None
        :pre-condition: the list is not empty, and index is within the range -len(self) to len(self)-1 and is an integer
        :post-condition: Every item to the right of given index is shifted one space to the left.
                         The length of the list is decreased by 1.
        :complexity: best case is O(1) when item at the back of the list is deleted and worst case is O(n) where n
                     is the length of the list
        """
        if not isinstance(index, int):
            raise TypeError("index should be of type integer")
        if not self.is_empty():
            if -self.length <= index < 0:
                index += self.length
            if index >= self.length or index < -self.length:
                raise IndexError('Not a valid index')
            for i in range(index, self.length):
                self.the_array[i] = self.the_array[i+1]
            self.length -= 1
        else:
            raise Exception('List is empty')

    def is_empty(self):
        """
        Determines if the list is empty.

        :return: True if list is empty, False otherwise.
        :complexity: best and worst cases are both O(1)
        """
        return self.length == 0

    def is_full(self):
        """
        Determines if the list is full.

        :return: True if the list is full, False otherwise
        :complexity: best and worst cases are both O(1)
        """
        return self.length == len(self.the_array)

    def __contains__(self, item):
        """
        Checks if item is in the list.

        :param item: Value to be compared with
        :return: True if item is in the list, False otherwise.
        :complexity: best case is O(1) when the item is the first element in the list and worst case is O(n) where
                     n is the length of the list
        """
        for i in range(self.length):
            if item == self.the_array[i]:
                return True
        return False

    def append(self, item):
        """
        Appends the item at the end of the list.

        :param item: Value to be appended
        :return: None
        :pre-condition: the list is not full
        :post-condition: item is appended to the back of the list and
                         the length of the list has increased by 1
        :complexity: best and worst cases are both O(1)
        """
        if not self.is_full():
            self.the_array[self.length] = item
            self.length += 1
        else:
            raise Exception('List is full')

    def unsafe_set_array(self,array,length):
        """
        UNSAFE: only to be used during testing to facilitate it!! DO NOT USE FOR ANYTHING ELSE
        """
        try:
            assert self.in_test_mode
        except:
            raise Exception('Cannot run unsafe_set_array outside testing mode')
			
        self.the_array = array
        self.length = length

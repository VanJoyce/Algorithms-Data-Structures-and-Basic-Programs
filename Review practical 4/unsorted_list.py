#!/usr/bin/python3

"""
This file implements the unsorted list ADT using Python lists as fake objects and arrays.

@author         Javier Candeira, from lecture code by Maria Garcia de la Banda. Modified by Graeme Gange
@since          11 Aug 2013
@input          none
@output         none
@errorHandling  none
@knownBugs      none

Invariants:
- length is never greater than len(the_array)
- length points to the first empty position (if any)
- all slots in positions 0 to length-1 of the_array contain items.
"""


class List:
    def __init__(self, size):
        """
        Creates an empty object of the class, i.e., an empty array list.

        @param          size number of items in containing array, or maxitems of list
        @return         a list data structure
        @post           an empty list object is created
        @complexity     best and worst case: the complexity of [None]*size, which it is 
                        probably O(size)
        """
        self.list_length = 0
        self.the_array = [None] * size

    def length(self):
        """
        Returns the length of the list.

        @param          none
        @return         the length of the list
        @complexity     best and worst case: O(1)
        """
        return self.list_length

    def is_empty(self):
        """
        Determines if the list has any elements.

        @param          none
        @return         false if list has elements, true if empty
        @complexity     best and worst case: O(1)
        """
        return self.list_length == 0;

    def is_full(self):
        """
        Determines whether the list is full.
        Since it is implemented with arrays, it can get full.

        @param      none
        @return     true if the list is full, false otherwise
        @complexity best and worst case: O(1)
        """
        return self.list_length >= len(self.the_array)

    def reset(self):
        """
        Resets the list to an empty state.

        @param          none
        @post           the list is empty
        @complexity     best and worst case: O(1)
        """
        self.list_length = 0

    def get_item(self, index):
        """
        Returns an item at a given position in the list.

        @param          index of element to return
        @pre            index is integer between zero and len(list)-1
        @post           list isn't changed
        @complexity     best and worst case: O(1)
        """
        try:
            assert int(index) == index
            assert 0 <= index <= self.list_length-1
        except (AssertionError, ValueError):
            raise IndexError('index not an integer within range')
        return self.the_array[index]

    def add_last(self, new_item):
        """
        Adds the input item at the end of the unsorted list.

        @param          new_item to add to this list
        @post           returns True if list has space, False it is has not
        @post           if True, the list has one more element after the method is called and
                        list[last] equals new_item after the method is called
        @post           If False, list is untouched
        @complexity     best and worst case: O(1)
        """
        has_space_left = not self.is_full()
        if has_space_left:
            self.the_array[self.list_length] = new_item
            self.list_length += 1
        return has_space_left


    def index(self, item):
        """
        Position of the first item equaling input item in this unsorted list
        Since this is an unsorted list, this is a linear search.

        @param      item to find
        @return     the item's index if the item appears in the list,
                    None otherwise.
        @complexity best case: O(M) (first item), worst case: O(length*M) (not there), where 
                    M is the size of the elements
        """
        for i in range(self.list_length):
            if self.the_array[i] == item:      #found
                return i
        return None

    def delete_item(self, delitem):
        """
        Deletes the first appearance (if any) of the input item.

        @param      delitem, first instance of which to be deleted
        @return     True if item was in list and has been deleted
        @post       if item was in list, list has one fewer elements
        @post       if item was in list one or more times, only first one
                    will have been removed
        @post       if item wasn't in list, list is unchanged
        @complexity best and worst case: O(length*M) 
        """
        pos = self.index(delitem)
        found = (pos != None)
        if found:   
            for i in range(pos, self.list_length - 1):
                self.the_array[i] = self.the_array[i+1]
            self.list_length = self.list_length - 1
        return found  


def test_is_empty():
    li = List(3)
    assert li.is_empty()
    li.add_last(5)
    assert li.the_array==[5,None,None]
    assert not li.is_empty()

def test_is_full():
    li = List(3)
    assert not li.is_full()
    li.add_last(5)
    li.add_last(5)
    li.add_last(5)
    assert li.the_array==[5,5,5]
    assert li.is_full()

def test_add_last():
    li = List(5)
    assert li.add_last(5)
    assert li.the_array==[5,None,None,None,None]
    assert li.add_last(3)
    assert li.the_array==[5,3,None,None,None]
    assert li.add_last(10)
    assert li.the_array==[5,3,10,None,None]
    assert li.add_last(0)
    assert li.the_array==[5,3,10,0,None]
    assert li.add_last(9)
    assert li.the_array==[5,3,10,0,9]
    assert not li.add_last(10)

def test_length():
    li = List(0)
    assert li.length()==0
    li = List(10)
    assert li.length()==0
    li.add_last(5)
    assert li.length()==1    

def test_get_item():
    li=List(10)
    li.list_length = 5
    li.the_array=[5,3,10,0,9,None,None,None,None,None]
    assert li.get_item(0) == 5
    assert li.get_item(1) == 3
    assert li.get_item(2) == 10
    assert li.get_item(3) == 0
    assert li.get_item(4) == 9

def test_delete_item():
    li=List(0)
    li.list_length=10
    li.the_array=[5,3,10,0,9,1,4,6,7,8]
    assert li.delete_item(0)
    assert li.delete_item(10)
    assert li.delete_item(9)
    assert li.delete_item(4)
    assert li.delete_item(7)
    assert li.list_length==5
    assert li.the_array==[5,3,1,6,8,8,8,8,8,8]

if __name__ == '__main__':
    """minimal sanity tests"""
    li = List(10)
    test_is_empty()
    test_is_full()
    test_add_last()
    test_length()
    test_get_item()
    test_delete_item()
    li.reset()
    assert li.length() == 0
    assert li.is_empty()

    print("All tests passed")

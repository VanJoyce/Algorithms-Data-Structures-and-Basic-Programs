import task2
import task3

class Node:
  def __init__(self, item, next):
    self.item =item
    self.next=next

class StackLinkedList:
    def __init__(self):
        self.top = None

    def is_empty(self):
        return self.top is None

    def is_full(self):
        return False

    def push(self, item):
        self.top = Node(item, self.top)

    def pop(self):
        if self.is_empty():
            raise Exception("stack is empty")
        tobereturned = self.top.item
        self.top = self.top.next
        return tobereturned

class Editor:
    def __init__(self):
        """
        Creates an instance of the class Editor and initialises its instance variables.

        :post-condition: the Editor object has instance variable text_lines which is a ListADT object
                         and an instance variable memory which is a StackLinkedList() object
        :complexity: best case and worst case are both O(1)
        """
        self.text_lines = task2.ListADT()
        self.memory = StackLinkedList()

    def read_filename(self, filename):
        """
        Converts a text file into a ListADT object and assigns it to instance variable text_lines.

        :param filename: name of the text file
        :return: None
        :pre-condition: file must be a text file and it must be in the same folder as this module. Filename includes
                        file extension
        :post-condition: text_lines is a ListADT object with each element being one line in the text file.
        :complexity: best and worst case should be dependent on read_text_file so they're both O(n) where n is the
                     number of lines in the text file.
        """
        self.text_lines = task3.read_text_file(filename)

    def print_num(self, num):
        """
        Prints the line at a given line number.

        :param num: line number
        :return: None
        :pre-condition: num is not 0
        :post-condition: line at specified line number is printed, or if no num is given, all lines are printed
        :complexity: best case is O(1) and worst case is O(n) where n is the number of lines in text_lines
        """
        if num == "":
            print(str(self.text_lines))
        else:
            num = int(num)
            if num == 0:
                raise ValueError("Zero is not a valid line number")
            elif num > 0:
                num -= 1
            print(self.text_lines[num])

    def delete_num(self, num):
        """
        Deletes line at a given line number.

        :param num: line number
        :return: None
        :pre-condition: num is not 0
        :post-condition: line at specified line number is deleted, or if no num is given, all lines are deleted.
                         line number and string deleted is stored in memory.
        :complexity: complexity depends on delete function in ListADT class. Best case is O(1) and worst case is O(n)
                     where n is the length of the list text_line
        """
        saved = task2.ListADT()
        saved.append("d")
        if num == "":
            saved.append(0)
            for line_num in range(len(self.text_lines)):
                saved.append(self.text_lines[0])
                self.text_lines.delete(0)
        else:
            num = int(num)
            if num == 0:
                raise ValueError("Zero is not a valid line number")
            elif num > 0:
                num -= 1
            saved.append(num)
            saved.append(self.text_lines[num])
            self.text_lines.delete(num)
        self.memory.push(saved)

    def insert_num_strings(self, num, list_of_strings):
        """
        Inserts a list of strings into specified position in text_lines.

        :param num: line number
        :param list_of_strings: a ListADT object with the lines to be inserted
        :return: None
        :pre-condition: num is not 0 and elements in list_of_strings is of type string
        :post-condition: the lines in list_of_strings are inserted into text_lines at the specified position
        :complexity: complexity depends on insert function in ListADT class. Best case is O(1) when there is only one
                     line to be inserted. Worst case is O(n*m) where n is the length of list_of_strings and m is
                     the length of text_lines.
        """
        saved = task2.ListADT()
        saved.append("i")
        num = int(num)
        if num == 0:
            raise ValueError("Zero is not a valid line number")
        elif num < 0:
            num += 1
            num += len(self.text_lines)
        else:
            num -= 1
        saved.append(num)
        for string in list_of_strings:
            self.text_lines.insert(num, string)
            num += 1
        saved.append(len(list_of_strings))
        self.memory.push(saved)

    def search_string(self, string):
        """
        Checks elements in text_lines for string given and returns their line numbers.

        :param string: string that is to be searched for in text_lines
        :return: a list of all the line numbers in which string appears
        :pre-condition: string must be of type string
        :post-condition: text_lines is unchanged
        :complexity: best case and worst case are both O(n*m) where n is the length of text_lines and m is the length
                     of the string elements of text_lines
        """
        if type(string) != str:
            raise TypeError("Item given is not of type string")
        line_num = task2.ListADT()
        for index in range(len(self.text_lines)):
            i = 0
            for char in self.text_lines[index]:
                if char == string[i]:
                    i += 1
                    if i == len(string):
                        line_num.append(index + 1)
                        break
                else:
                    i = 0
                    if char == string[i]:
                        i += 1
        return line_num

    def undo(self):
        """
        Reverses the last successful delete or insert function.

        :return: None
        :pre-condiiton: the item popped from the stack is a ListADT object and the first element at index 0 should
                        only either be "d" or "i" (representing delete and insert respectively")
        :post-condition: the last previous successful delete or insert function is undone
        :complexity: best case is O(1) when only one line has to be inserted at the back or when one line has to be
                     deleted from behind. Worst case happens when there are many lines to insert back into the list,
                     and it happens in O(n*m) time where n is the number of lines to be inserted and m is the length of
                     text_lines.

        """
        previous = self.memory.pop()
        if not isinstance(previous, task2.ListADT):
            raise TypeError("Did not expect any other object in memory")
        if previous[0] == "d":
            index = previous[1]
            for i in range(len(previous)-1, 1, -1):
                self.text_lines.insert(index, previous[i])
        elif previous[0] == "i":
            start = previous[1]
            for j in range(previous[2]):
                self.text_lines.delete(start)
        else:
            raise ValueError("Did not expect any other action other than delete or insert")

if __name__=='__main__':
    ed = Editor()
    while True:
        print("---MENU---")
        print("read filename\nprint num\ndelete num\ninsert num\nsearch string\nundo\nquit")
        try:
            command = input("What would you like to do? ")
            if command.startswith("read"):
                user_input = command.split(' ')         # put each word as an element in a list
                ed.read_filename(user_input[1])         # user_input[1] to get the filename
            elif command.startswith("print"):
                user_input = command.split(' ')
                if len(user_input) == 1 and user_input[0] == "print": # no line number given
                    ed.print_num("")
                elif len(user_input) == 2:
                    ed.print_num(user_input[1])
                else:
                    print("?")
            elif command.startswith("delete"):
                user_input = command.split(' ')
                if len(user_input) == 1 and user_input[0] == "delete":
                    ed.delete_num("")
                elif len(user_input) == 2:
                    ed.delete_num(user_input[1])
                else:
                    print("?")
            elif command.startswith("insert"):
                user_input = command.split(' ')
                strings = task2.ListADT()
                line = input()
                while line != ".":
                    strings.append(line)
                    line = input()
                ed.insert_num_strings(user_input[1], strings)
            elif command.startswith("search"):
                user_input = command.replace('search ', '')
                if user_input == '':
                    print("?")
                line_numbers = ed.search_string(user_input)
                print("Line numbers containing " + user_input)
                for line in line_numbers:
                    print(line)
            elif command == "undo":
                ed.undo()
            elif command == "quit":
                break
            else:
                print("?")
        except (FileNotFoundError, ValueError, IndexError, Exception, TypeError):
            print("?")
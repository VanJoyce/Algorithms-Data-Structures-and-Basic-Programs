import task2
import csv


class BinaryTreeNode:

    def __init__(self, key=None, value=None, left=None, right=None):
        self.key = key
        self.item = value
        self.left = left
        self.right = right

    def __str__(self):
        return " (" + str(self.key) +  ", " + str(self.item) + " ) "


class BinarySearchTree:

    def __init__(self):
        self.root = None
        self.probe = 0

    def is_empty(self):
        return self.root is None

    def __len__(self):
        return self._len_aux(self.root)

    def _len_aux(self, current):
        if current is None:
            return 0
        else:
            return 1+self._len_aux(current.left)+self._len_aux(current.right)

    def inorder(self, f):
        return self._inorder_aux(self.root, f)

    def _inorder_aux(self, current, f):
        if current is not None:
            self._inorder_aux(current.left, f)
            f(current)
            self._inorder_aux(current.right, f)

    def __contains__(self, key):
        # return self._contains_aux(key, self.root)
        return self._contains_iter(key)

    def _contains_aux(self, key, current_node):
        if current_node is None:  # base case
            return False
        elif key == current_node.key:
            return True
        elif key < current_node.key:
            return self._contains_aux(key, current_node.left)
        elif key > current_node.key:
            return self._contains_aux(key, current_node.right)

    def _contains_iter(self, key):
        current_node = self.root
        while current_node is not None:
            if key < current_node.key:
                current_node = current_node.left
            elif key > current_node.key:
                current_node = current_node.right
            else:
                return True
        return False

    def __getitem__(self, key):
        return self._get_item_iter(key, self.root)

    def _get_item_aux(self, key, current_node):
        if current_node is None:  # base case
            raise KeyError("Key not found")
        elif key == current_node.key:
            return current_node.item
        elif key < current_node.key:
            return self._get_item_aux(key, current_node.left)
        elif key > current_node.key:
            return self._get_item_aux(key, current_node.right)

    def _get_item_iter(self, key, current_node):
        while current_node is not None:
            if key < current_node.key:
                current_node = current_node.left
            elif key > current_node.key:
                current_node = current_node.right
            else:
                assert current_node.key == key
                return current_node.item
        raise KeyError("Key not found")

    def __setitem__(self, key, value):
        self._insert_iter(key, value)

    def _insert_aux(self, key, value, current_node):
        if current_node is None:
            current_node = BinaryTreeNode(key, value)
        elif key < current_node.key:
            self.probe += 1
            current_node.left =  self._insert_aux(key, value, current_node.left)
        elif key > current_node.key:
            self.probe += 1
            current_node.right = self._insert_aux(key, value, current_node.right)
        elif key == current_node.key:
            current_node.item = value
        return current_node

    def _insert_iter(self, key, value):
        if self.root is None:
            self.root = BinaryTreeNode(key, value)
            return

        current_node = self.root
        while True:
            if key < current_node.key:
                self.probe += 1
                if current_node.left is None:
                    current_node.left = BinaryTreeNode(key, value)
                    break
                else:
                    current_node = current_node.left
            elif key > current_node.key:
                self.probe += 1
                if current_node.right is None:
                    current_node.right = BinaryTreeNode(key, value)
                    break
                else:
                    current_node = current_node.right
            else:
                assert current_node.key == key
                current_node.item = value
                break


class HashTable:
    def __init__(self, table_capacity=53, hash_base=31):
        """
        Creates an instance of HashTable class.

        :param table_capacity: the size of the hash table
        :param hash_base: the hash base of the hash function
        :pre-condition: if table_capacity and hash_base are not specified, they should be initialised
                        with 53 and 31 respectively (the default)
        :post-condition: HashTable object is created with seven variables - table, base, count, collision, probe_total,
                         probe_max and rehash_count
        :complexity: best and worst cases are both O(1)
        """
        self.table = [None] * table_capacity
        self.base = hash_base
        self.count = 0
        self.collision = 0
        self.probe_total = 0
        self.probe_max = 0
        self.rehash_count = 0

    def __getitem__(self, key):
        """
        Returns value corresponding to key in the hash table.

        :param key: the key to look for in the hash table
        :return: value in the hash table that corresponds to the key
        :pre-condition: key must be of type string, key can be found in the hash table
        :post-condition: nothing is changed in the hash table
        :complexity: best case is O(1) when there was no collision so first element checked has matching key
                     worst case is O(n) where n is the number of nodes in the binary search tree being checked, happens
                     when the binary search tree is unbalanced
        """
        if not isinstance(key, str):
            raise TypeError("Key values must be of type string")

        hash_value = self.hash(key)
        my_tree = self.table[hash_value]
        if my_tree is not None:
            return my_tree[key]
        else:
            raise KeyError("Key not found")

    def __setitem__(self, key, value):
        """
        Sets the value corresponding to key in the hash table to be value.

        :param key: unique key for the value
        :param value: the value for the corresponding key
        :return: None
        :pre-condition: key must be of type string
        :post-condition: if no matching key exists, a new key and its value is inserted into the hash table, else if
                         a matching key does exist, its value is changed.
        :complexity: best case is O(1) when the first element checked in the hash table has the matching key and
                     its value is changed.
                     worst case depends on the binary search tree
                     it is O(n) where n is the depth of the binary search tree, happens when the binary tree is unbalanced
        """
        if not isinstance(key, str):
            raise TypeError("Key values must be of type string")

        hash_value = self.hash(key)
        if self.table[hash_value] is None:
            my_tree = BinarySearchTree()
            self.table[hash_value] = my_tree
        else:
            my_tree = self.table[hash_value]
            self.collision += 1
        my_tree[key] = value
        self.count += 1
        self.probe_total += my_tree.probe
        if my_tree.probe > self.probe_max:
            self.probe_max = my_tree.probe
        my_tree.probe = 0

    def __contains__(self, key):
        """
        Checks whether the key given is in the hash table.

        :param key: the key to look for in the hash table
        :return: True if key is found in the hash table, False otherwise
        :pre-condition: key must be of type string
        :post-condition: nothing is changed in the hash table
        :complexity: best case is O(1) when the first element checked in the hash table has the matching key
                     worst case is O(n) where n is the number of nodes in the binary tree checked and binary search tree is unbalanced
        """
        if not isinstance(key, str):
            raise TypeError("Key values must be of type string")
        hash_value = self.hash(key)
        if self.table[hash_value] is None:
            return False
        else:
            return key in self.table[hash_value]

    def hash(self, key):
        """
        Computes the hash value for a given key using uniform hash function.

        :param key: given key
        :return: hash value
        :pre-condition: key must be of type string
        :post-condition: None
        :complexity: best case is O(1) when the key is only one character long
                     worst case is O(n) where n is the number of characters in key
        """
        if not isinstance(key, str):
            raise TypeError("Key values must be of type string")
        value = 0
        for i in range(len(key)):
            value = ((value * self.base) + ord(key[i])) % len(self.table)
        return value

    def statistics(self):
        """
        Returns statistics about the hash table regarding collision, probing and rehashing.

        :return: number of collisions, total length of probe chains, length of longest
                 probe chain, number of times rehash() has been called
        :pre-condition: None
        :post-condition: Nothing about hash table is changed
        :complexity: both best and worst cases are O(1)
        """
        collision_count = self.collision
        probe_total = self.probe_total
        probe_max = self.probe_max
        rehash_count = self.rehash_count
        return collision_count, probe_total, probe_max, rehash_count


def load_dictionary_statistics(hash_base, table_size, filename, max_time):
    """
    Creates a hash table for the words in filename and returns number of words process, time taken and
    some statistics.

    :param hash_base: the base number used in the hash function
    :param table_size: the capacity of the hash table
    :param filename: the name of the file to be read
    :param max_time: the maximum amount of time that the function is allowed to take before TimeOutError is raised.
    :return: number of words, time taken, number of collisions, total length of probe chains, length of longest
             probe chain, number of times rehash() has been called
    :pre-condition: filename must be a text file and have only one word per line, max_time must be in seconds
    :post-condition: each distinct word is inserted into the hash table
    :complexity: best case is O(1) when the file has only one word in it
                 worst case is O(n) where n is the number of lines in filename
    """
    hash_table = HashTable(table_size, hash_base)
    try:
        time = task2.load_dictionary(hash_table, filename, max_time)
    except TimeoutError:
        time = None
    words = hash_table.count
    collision_count, probe_total, probe_max, rehash_count = hash_table.statistics()
    return words, time, collision_count, probe_total, probe_max, rehash_count


def table_load_dictionary_statistics(max_time):
    """
    Creates a csv file 'output_task5.csv' and writes into it the statistics of each combination of hash base and
    table size given per dictionary file.

    :param max_time: the maximum amount of time in seconds the function is allowed to take
    :return: a csv file
    :pre-condition: max_time must be in seconds
    :post-condition: a csv file is created with all the information
    :complexity: best case is O(1) if the file contains only one word
                 worst case is O(n) where n is the number of words processed before time runs out
    """
    b_combo = [1, 27183, 250726]
    tablesize_combo = [250727, 402221, 1000081]
    dictionaries = ['english_small.txt', 'english_large.txt', 'french.txt']

    with open('output_task5.csv', 'w', newline='') as file:
        output_writer = csv.writer(file, delimiter=',')
        for b in b_combo:
            for TABLESIZE in tablesize_combo:
                for dictionary in dictionaries:
                    words, time, collision_count, probe_total, probe_max, rehash_count = load_dictionary_statistics(b, TABLESIZE, dictionary, max_time)
                    if time is None:
                        time = "TIMEOUT"
                    output_writer.writerow([dictionary, TABLESIZE, b, words, time, collision_count, probe_total, probe_max, rehash_count])


if __name__=='__main__':
    table_load_dictionary_statistics(120)

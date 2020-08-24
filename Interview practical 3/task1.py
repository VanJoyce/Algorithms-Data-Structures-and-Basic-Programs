import copy


class HashTable:
    def __init__(self, table_capacity=53, hash_base=31):
        """
        Creates an instance of HashTable class.

        :param table_capacity: the size of the hash table
        :param hash_base: the hash base of the hash function
        :pre-condition: if table_capacity and hash_base are not specified, they should be initialised
                        with 53 and 31 respectively (the default)
        :post-condition: HashTable object is created with three variables - table, base and count
        :complexity: best and worst cases are both O(1)
        """
        self.table = [None] * table_capacity
        self.base = hash_base
        self.count = 0

    def __getitem__(self, key):
        """
        Returns value corresponding to key in the hash table.

        :param key: the key to look for in the hash table
        :return: value in the hash table that corresponds to the key
        :pre-condition: key must be of type string, key can be found in the hash table
        :post-condition: nothing is changed in the hash table
        :complexity: best case is O(1) when there was no collision so first element checked has matching key
                     worst case is O(n) where n is the capacity of the hash table
        """
        if not isinstance(key, str):
            raise TypeError("Key values must be of type string")

        hash_value = self.hash(key)
        if self.table[hash_value] is not None and self.table[hash_value][0] != key:  # collision, check probe chain
            i = (hash_value + 1) % len(self.table)
            while i != hash_value:
                if self.table[i] is None:  # no matching key because not in probe chain
                    raise KeyError("No such thing was found!")
                    break
                elif self.table[i][0] == key:
                    hash_value = i
                    break
                else:
                    i = (i + 1) % len(self.table)
        elif self.table[hash_value] is None:
            raise KeyError("No such thing was found!")
        return self.table[hash_value][1]

    def __setitem__(self, key, value):
        """
        Sets the value corresponding to key in the hash table to be value.

        :param key: unique key for the value
        :param value: the value for the corresponding key
        :return: None
        :pre-condition: key must be of type string
        :post-condition: if no matching key exists, a new key and its value is inserted into the hash table, else if
                         a matching key does exist, its value is changed. The rehash method is called before insertion
                         if table is full and the key does not exist in the table yet
        :complexity: best case is O(1) when the first element checked in the hash table has the matching key and
                     its value is changed.
                     worst case is O(n) where n is the length of the hash table
        """
        if not isinstance(key, str):
            raise TypeError("Key values must be of type string")

        # Check for matching key
        hash_value = self.hash(key)
        changed = False
        if self.table[hash_value] is not None and self.table[hash_value][0] != key:  # collision, check probe chain
            i = (hash_value + 1) % len(self.table)
            while i != hash_value:
                if self.table[i] is None:  # no matching key because not in probe chain
                    hash_value = i
                    break
                elif self.table[i][0] == key:
                    self.table[i] = (key, value)
                    changed = True
                    break
                else:  # self.table[i] is not None and the key doesn't match
                    i = (i + 1) % len(self.table)
        elif self.table[hash_value] is not None and self.table[hash_value][0] == key:
            self.table[hash_value] = (key, value)
            changed = True

        # No matching key and hash table is full
        if self.count == len(self.table):
            self.rehash()

        if not changed:
            self.table[hash_value] = (key, value)
            self.count += 1

    def __contains__(self, key):
        """
        Checks whether the key given is in the hash table.

        :param key: the key to look for in the hash table
        :return: True if key is found in the hash table, False otherwise
        :pre-condition: key must be of type string
        :post-condition: nothing is changed in the hash table
        :complexity: best case is O(1) when the first element in the hash table has the matching key
                     worst case is O(n) where n is the capacity of the hash table
        """
        if not isinstance(key, str):
            raise TypeError("Key values must be of type string")
        for i in range(len(self.table)):
            if self.table[i] is None:
                continue
            elif self.table[i][0] == key:
                return True
        return False

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

    def rehash(self):
        """
        Updates the size of the hash table and reinserts the data from the previous hash table.

        :return: None
        :pre-condition: there must be a prime number in the table Primes that is larger than twice the current length
                        of the hash table
        :post-condition: the new capacity of the hash table is the first number in Primes that is larger than twice the
                         current length of the hash table
        :complexity: best case is O(1) when the previous hash table had only a length of 1
                     worst case is O(n) where n is the length of the hash table
        """
        Primes = [3, 7, 11, 17, 23, 29, 37, 47, 59, 71, 89, 107, 131, 163, 197, 239, 293, 353, 431, 521, 631, 761,
                  919, 1103, 1327, 1597, 1931, 2333, 2801, 3371, 4049, 4861, 5839, 7013, 8419, 10103, 12143, 14591,
                  17519, 21023, 25229, 30313, 36353, 43627, 52361, 62851, 75521, 90523, 108631, 130363, 156437,
                  187751, 225307, 270371, 324449, 389357, 467237, 560689, 672827, 807403, 968897, 1162687, 1395263,
                  1674319, 2009191, 2411033, 2893249, 3471899, 4166287, 4999559, 5999471, 7199369]
        twice = 2*len(self.table)
        num = -1
        for num in Primes:
            if num > twice:
                previous = copy.deepcopy(self.table)
                self.table = [None] * num
                break
        if num == -1:
            raise ValueError("No such prime in the list")

        # re-insert
        for i in range(len(previous)):
            if previous[i] is None:
                continue
            else:
                hash_value = self.hash(previous[i][0])
                if self.table[hash_value] is not None:
                    hash_value = (hash_value + 1) % len(self.table)
                self.table[hash_value] = previous[i]

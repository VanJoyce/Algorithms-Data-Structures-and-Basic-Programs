import task1
import re


class HashTable(task1.HashTable):
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

        # No matching key and hash table is more than half full
        if self.count > 0.5 * len(self.table):
            self.rehash()

        if not changed:
            self.table[hash_value] = (key, value)
            self.count += 1


class Freq:
    def __init__(self):
        """
        Creates an instance of the class Freq and initialises its instance variables.

        :pre-condition: None
        :post-condition: an instance is created with two variables:
                         word_frequency - an empty hash table
                         max - to keep track of the maximum number of occurrence of the most common word
        :complexity: best case and worst case are both O(1)
        """
        self.word_frequency = HashTable(1000081, 250726)
        self.max = 0

    def add_file(self, filename):
        """
        Reads each word from a file into a hash table. The data associated with the word is its occurrence count.

        :param filename: the name of the file to be read
        :return: None
        :pre-condition: the file must be a text file
        :post-condition: the hash table word_frequency is filled with the words found in the file with the number of
                         time each word occurs
        :complexity: best case is O(1) when the file only has one word
                     worst case is O(n*m*l) where n is the number of lines in file and m is the number of words in each
                     line and l is the length of the hash table word_frequency
        """
        punctuation = [':', ';', '"', '(', ')', '.', ',']
        with open(filename, 'r', encoding="utf-8") as file:
            for line in file:
                for p in punctuation:
                    line = line.replace(p, ' ')
                line = line.split()
                for word in line:
                    try:
                        occurrence = self.word_frequency[word]
                    except KeyError:  # self.word_frequency[word] is None
                        self.word_frequency[word] = 0
                        occurrence = self.word_frequency[word]

                    occurrence += 1
                    if occurrence > self.max:
                        self.max = occurrence
                    self.word_frequency[word] = occurrence

    def rarity(self, word):
        """
        Returns the rarity score of a word in the hash table word_frequency.

        :param word: the word to look for in the hash table
        :return: rarity score of the word (0 for common, 1 for uncommon, 2 for rare, and 3 for misspelled words or
                 words that are not in the hash table
        :pre-condition: word must be a string
        :post-condition: nothing is changed in the hash table
        :complexity: depends on __getitem__ in HashTable class so best case is O(1) and worst case is O(n) where n is
                     the length of the hash table
        """
        if not isinstance(word, str):
            raise TypeError("Word given must be a string")

        try:
            occurrence = self.word_frequency[word]
        except KeyError:  # misspelling or missing word
            return 3

        if self.max/100 <= occurrence:  # common
            return 0
        elif self.max/1000 <= occurrence < self.max/100:  # uncommon
            return 1
        elif 0 < occurrence < self.max/1000:  # rare
            return 2


if __name__ == '__main__':
    table = Freq()
    table.add_file('1342-0.txt')
    table.add_file('2600-0.txt')
    table.add_file('98-0.txt')

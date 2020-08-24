import task6
import re


class HashTable(task6.HashTable):
    pass


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

        if self.max / 100 <= occurrence:  # common
            return 0
        elif self.max / 1000 <= occurrence < self.max / 100:  # uncommon
            return 1
        elif 0 < occurrence < self.max / 1000:  # rare
            return 2

    def evaluate_frequency(self, other_filename):
        """
        Calculates the percentages of common, uncommon, rare, or misspelled/ unusual words that appears in the file.

        :param other_filename: the name of the file to be looked at
        :return: a tuple with four elements containing the percentages of words in file that are common, uncommon, rare,
                 or is an error respectively
        :pre-condition: the file must be a text file
        :post-condition: nothing is changed in hash table or file
        :complexity: best case is O(1) when there is only one word in the file without any punctuations.
                     worst case is O(n*m) where n is the number of unique words in the file and m is the length
                     of the hash table
        """
        punctuation = [':', ';', '"', '(', ')', '.', ',']
        with open(other_filename, 'r', encoding="utf-8") as file:
            words = []
            for line in file:
                for p in punctuation:
                    line = line.replace(p, ' ')
                line = line.split()
                for word in line:
                    if word not in words:
                        words.append(word)
            common, uncommon, rare, errors = 0, 0, 0, 0
            for word in words:
                score = self.rarity(word)
                if score == 0:
                    common += 1
                elif score == 1:
                    uncommon += 1
                elif score == 2:
                    rare += 1
                elif score == 3:
                    errors += 1
                else:
                    raise Exception("Scores should only be 0, 1 ,2, or 3")

        common = (common/len(words))*100
        uncommon = (uncommon/len(words))*100
        rare = (rare/len(words))*100
        errors = (errors/len(words))*100

        return common, uncommon, rare, errors


if __name__ == '__main__':
    table = Freq()
    table.add_file('1342-0.txt')
    table.add_file('2600-0.txt')
    table.add_file('98-0.txt')
    print(table.evaluate_frequency('84-0.txt'))

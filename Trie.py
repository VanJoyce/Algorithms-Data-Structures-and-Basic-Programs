"""
Vanessa Joyce Tan
30556864
Assignment 3
"""


class Node:
    """
    Node class for the Trie.
    """
    def __init__(self):
        """
        Creates a node with a list of links for every lowercase English alphabet character and a terminal character,
        and frequency.

        :time complexity:   best case and worst case are both O(1) because no matter what, it takes the same amount of
                            time to create a node.
        :space complexity:  O(1) because space is fixed for every node
        :aux space complexity: O(1)
        """
        self.link = [None] * 27
        self.freq = 0


class Trie:
    """
    Trie class to store strings.
    """
    def __init__(self, text):
        """
        Creates a Trie object containing the strings in text.

        :param text: a list of strings
        :pre-condition: the strings in text must only consist of lowercase English alphabet characters and there are no
                        empty strings
        :post-condition: Trie object is created with the strings in text

        Assuming T is the total number of characters over all the strings in text,
        :time complexity:   best case and worst case are both O(T) because each word is inserted into the Trie and the
                            time complexity of __setitem__ depends on the number of characters in the word
        :space complexity: O(T) because a node exists for each character over all strings
        :aux space complexity: O(T)
        """
        self.root = Node()
        for word in text:
            self.__setitem__(word)

    def __setitem__(self, key):
        """
        Inserts a string into the Trie.

        :param key: the string to be inserted into the Trie.
        :return: -
        :pre-condition: key has to be in lowercase English alphabet characters
        :post-condition: key is stored in Trie

        Assuming N is the number of characters in key,
        :time complexity: best case and worst case are both O(N) because time complexity of setitem_aux() is O(N)
        :space complexity: O(N) because setitem_aux() has O(N) space complexity
        :aux space complexity: O(N)
        """
        current = self.root
        current.freq += 1
        self.setitem_aux(current, key)

    def setitem_aux(self, current, key, pos=0):
        """
        Recursive function to insert a string into the Trie. Creates a node it if doesn't exist yet for each character
        in the string and one for the terminal character. If a node already exists, increase its frequency.

        :param current: the current Node
        :param key: the string to be inserted into the Trie
        :param pos: iterator for key to know which character is being inserted
        :return: -
        :pre-condition: key has to be in lowercase English alphabet characters
        :post-condition: if node exists for character in key, the frequency is updated. If it doesn't exist, a node is
                         created

        Assuming N is the number of characters in key,
        :time complexity: best case and worst case are both O(N) because each recursive call is O(1) and this method is
                          called for every character in key
        :space complexity: O(N) because each node takes O(1) space and this method is called for each character in key
        :aux space complexity: O(N)
        """
        if pos >= len(key):  # end of string
            index = 0
        else:
            index = ord(key[pos]) - 96

        if current.link[index] is None:
            current.link[index] = Node()

        current.link[index].freq += 1
        if index == 0:  # end recursion
            return
        else:
            self.setitem_aux(current.link[index], key, pos + 1)

    def string_freq(self, query_str):
        """
        Checks how many times a given word occurs in the Trie.

        :param query_str: the word we are looking for
        :return: an integer representing how many times the word appears in the Trie
        :pre-condition: query_str consists of lowercase English alphabet letters only
        :post-condition: nothing is changed in Trie

        Assuming q is the number of characters in query_str,
        :time complexity: best case is O(1) when the first letter of query_str doesn't exist in Trie and worst case is
                          O(q) when we check for nodes the characters in query_str is pointing to
        :space complexity: O(1) because we only look at one node at a time in search()
        :aux space complexity: O(1)
        """
        word = self.search(query_str)
        if word is not None and word.link[0] is not None:
            return word.link[0].freq
        else:
            return 0

    def prefix_freq(self, query_str):
        """
        Checks how many words in the Trie has a given prefix.

        :param query_str: the prefix to look for in the Trie
        :return: an integer representing how many words have the the given prefix in Trie
        :pre-condition: query_str must only consist of lowercase English alphabet letters
        :post-condition: no changes made to Trie

        Assuming q is the number of characters in query_str,
        :time complexity: best case is O(1) when the first letter of query_str is not found in the Trie and worst case
                          is O(q) where we look at the nodes each character in query_str is pointing to
        :space complexity: O(1) because we only look at one node at a time in search()
        :aux space complexity: O(1)
        """
        prefix = self.search(query_str)
        if prefix is None:
            return 0
        else:
            return prefix.freq

    def search(self, query_str):
        """
        Searches for a string in the Trie and returns the node the last letter of the string is pointing to if
        it exists.

        :param query_str: the string we are searching for in the Trie
        :return: the node the last letter of query_str is pointing to if it exists, otherwise None
        :pre-condition: query_str must only consist of lowercase English alphabet characters
        :post-condition: nothing is changed in Trie

        Assuming q is the number of characters in query_str,
        :time complexity: best case is O(1) when the node the first letter points to doesn't exist and worst case is
                          O(q) because we must check the nodes for each character in query_str
        :space complexity: O(1) because we only look at one node at a time
        :aux space complexity: O(1)
        """
        current = self.root
        for letter in query_str:
            index = ord(letter) - 96
            if current.link[index] is not None:
                current = current.link[index]
            else:
                return None
        return current

    def wildcard_prefix_freq(self, query_str):
        """
        Checks for strings in the Trie that have a given prefix with a wildcard.

        :param query_str: the given prefix with a wildcard
        :return: a list of strings that have a prefix matching query_str
        :pre-condition: query_str must not be an empty string, wildcard character must be represented by the char '?',
                        all other characters in query_str besides the wildcard must be in lowercase English alphabets
        :post-condition: the list returned contains strings that have prefixes that matches the query_str

        Assuming q is the number of characters in query_str,
        S is the number of characters in all the strings in the Trie which have the matching prefix,
        :time complexity: best case is O(1) if the first letter of query_str doesn't even exist in the Trie and worst
                          case is O(q + S) when we call the auxiliary function recursively to get all the strings which
                          have the matching prefix
        Assuming N is the length of the longest word in output and M is the size of output so far,
        :space complexity:  O(N + M) because auxiliary function has this space complexity
        :aux space complexity: O(N + M)
        """
        current = self.root
        output_str = ""
        for pos in range(len(query_str)):
            if current is None:     # prefix doesn't even exist in Trie
                return []
            if query_str[pos] == '?':
                return self.wildcard_prefix_freq_aux(current, query_str, pos, output_str, [])
            else:
                output_str += query_str[pos]
                current = current.link[ord(query_str[pos]) - 96]

    def wildcard_prefix_freq_aux(self, current, query_str, pos, output_str, output):
        """
        Recursive function to check for strings in the Trie that have a given prefix with a wildcard.

        :param current: the node we are checking currently
        :param query_str: the given prefix with a wildcard
        :param pos: iterator for query_str to know which character in query_str we are looking at currently
        :param output_str: string which has the given prefix
        :param output: list of strings found in Trie which contain the given prefix
        :return: a list of strings that contain the given prefix
        :pre-condition: the wildcard must be represented by the character '?'. If query_str has any other characters
                        besides the wildcard, they must be lowercase English alphabet characters. query_str cannot be
                        an empty string
        :post-condition: output contains all the strings that have the given prefix so far in Trie

        Assuming q is the number of characters in query_str,
        S is the total number of characters in the strings that have the given prefix,
        :time complexity: best case is O(1) when the node the first letter is pointing to doesn't exist, and worst case
                          is O(q + S) because we have to check through all the nodes where the characters in query_str
                          and the other strings that have the matching prefix point to
        Assuming N is the length of the longest word in output and M is the size of output so far,
        :space complexity:  O(N + M) because it depends on output list and how deep the recursion goes, and each
                            recursive call only looks at one node which takes O(1) space and the recursion only goes
                            as deep as the length of the longest word that contains the given prefix
        :aux space complexity: O(N) because output is passed as a parameter
        """
        if current is None:
            return          # doesn't exist, go back

        if pos < len(query_str):    # prefix
            if query_str[pos] == '?':
                for i in range(1, len(current.link)):
                    if current.link[i] is None:
                        continue
                    self.wildcard_prefix_freq_aux(current.link[i], query_str, pos+1, output_str + chr(i+96), output)
            else:
                i = ord(query_str[pos]) - 96
                self.wildcard_prefix_freq_aux(current.link[i], query_str, pos+1, output_str + query_str[pos], output)
        else:   # suffix
            if current.link[0] is not None:     # output_str is a word that has the prefix
                for i in range(current.link[0].freq):  # for duplicate strings
                    output.append(output_str)
            for i in range(1, len(current.link)):
                if current.link[i] is None:
                    continue
                self.wildcard_prefix_freq_aux(current.link[i], query_str, pos, output_str + chr(i+96), output)

        return output

import timeit
import task1
import csv


def load_dictionary(hash_table, filename, time_limit=0):
    """
    Reads a file and adds each word to hash_table with integer 1 as the associated data.

    :param hash_table: list containing tuples of (key, value)
    :param filename: the name of the file to be read
    :param time_limit: the maximum time taken in seconds before error is raised
    :return: time taken in seconds for the function to process the file
    :pre-condition: the file should have only one word per line, time_limit is in seconds, file is a text file
    :post-condition: Each word in the file is inserted into hash_table as a key with integer 1 as data
    :complexity: best case is O(1) when there is only one word in the file
                 worst case is O(n) where n is the number of words processed before time_limit is reached
    """
    time = 0
    start_time = timeit.default_timer()
    with open(filename, 'r', encoding="utf-8") as file:
        for word in file:
            if word[-1] == "\n":
                word = word[:-1]
            hash_table[word] = 1
            if time_limit > 0:
                time = timeit.default_timer() - start_time
                if time >= time_limit:
                    raise TimeoutError("It went over the time limit!")
        return time


def load_dictionary_time(hash_base, table_size, filename, max_time):
    """
    Creates a new hash table for the words in filename and returns number of distinct words loaded into the hash table
    and time taken for that.

    :param hash_base: the hash base to be used in hash function
    :param table_size: the capacity of the hash table
    :param filename: the name of the file to be read
    :param max_time: the maximum amount of time in seconds the function is allowed to process
    :return: (words, time), where words is the number of distinct words added to the table, and time is the time taken
             in seconds for load_dictionary to complete if less or equal than max_time, and None otherwise
    :pre-condition: file should have one word per line, max_time is in seconds, file is a text file
    :post-condition: if load_dictionary raises TimeOutError, time is None
    :complexity: best case is O(1) if the file contains only one word
                 worst case is O(n) where n is the number of words processed before time runs out
    """
    hash_table = task1.HashTable(table_size, hash_base)
    try:
        time = load_dictionary(hash_table, filename, max_time)
    except TimeoutError:
        time = None
    words = hash_table.count
    return words, time


def table_load_dictionary_time(max_time):
    """
    Creates a csv file and writes in it the number of words processed and the time taken in seconds to do so.

    :param max_time: the maximum amount of time taken in seconds the function is allowed to run
    :return: a csv file with all the collected information
    :pre-condition: max_time is in seconds
    :post-condition: csv file is created with 5 columns
    :complexity: best case and worst case is O(n^3*m) where n is the length of b_combo, TABLESIZE_combo and dictionaries
                 and m is the number of lines (words) in a dictionary
    """
    b_combo = [1, 27183, 250726]
    tablesize_combo = [250727, 402221, 1000081]
    dictionaries = ['english_small.txt', 'english_large.txt', 'french.txt']

    with open('output_task2.csv', 'w', newline='') as file:
        output_writer = csv.writer(file, delimiter=',')
        for b in b_combo:
            for TABLESIZE in tablesize_combo:
                for dictionary in dictionaries:
                    num_of_words, time_taken = load_dictionary_time(b, TABLESIZE, dictionary, max_time)
                    if time_taken is None:
                        time_taken = "TIMEOUT"
                    output_writer.writerow([dictionary, TABLESIZE, b, num_of_words, time_taken])


if __name__ == '__main__':
    table_load_dictionary_time(120)

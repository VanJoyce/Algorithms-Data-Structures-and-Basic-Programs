# Vanessa Joyce Tan, 30556864
# Assignment 1 Task 1

""" - create count-array that is length (base-1) e.g. base 10 should have count array of length 9
    - number of count array should be equal to the number of digits
    - make sure to use a STABLE method because radix sort depends on stability (e.g. linked lists)
    - converting a number from decimal to binary takes a lot of space and is not recommended
    - in count array put the original number from the input list (decimal) not the binary conversion.
    - don't convert to different base
    - don't convert the number to string.

    HOW TO IMPLEMENT RADIX SORT FOR OTHER BASES (because conversion wastes memory space and time):
    - Assume the conversion doesn't exist.
    e.g. converting 4329 (dec) to base 5:
        to get rightmost column: (4329 // 5^0) % 5
        to get second rightmost column: (4329 // 5^1) % 5
        formula: num // (base to be converted to)^col_index % base to be converted to
                item // base ^ (col-1) % base

    SORTING STRINGS
    - Use a base of 26 (a = 0...........z=25)
    - sorting strings that are of different length:
        method 1 (tier noob)
        - make all strings same length by adding special character at the back e.g. cat____ (four underscores)
        - sorting is left aligned
        method 2 (shift everything to the right) (tier noob)
        - add special character on the left
        - need to shift count array
        (special character is of lowest priority) so 0 = _, 1 = a, 2 = b, ... 26 = z

        METHOD 1 AND METHOD 2 ADD COMPLEXITY BECAUSE ADDING SPECIAL CHARACTER TO SORT AND THEN REMOVING

        Method 3 (tier gold)
        if col < len(item):
            # exist, do the sorting
        else:
            # no exist, put in bucket 0

        Method 4 (as below) - tier diamond
    - how to make it O(N) where N is the sum of all string lengths
      instead of O(MN) where M is the length of the longest string and N is the number of strings
        1. pre-processing
            to sort the strings based on their length (can use counting sort cause their length are just numbers)
            [cat, taco, tags, gitgud, gudetama, food] sorted to be
            [cat, taco, tags, food, gitgud, gudetama]
        2. right align them (for visualisation purposes, no need to code)
        3. check each column from bottom to top instead (from gudetama to cat)
            - when you reach a characted that doesn't exist (i.e the word is shorter than column being checked), exit loop


    PLOTTING GRAPH
    - can use matplotlib (try not to use excel but can if you want to)
    - x axis is base, y is time



"""

'''
    for i in range(len(string_list)):              # for each string i want to know the length (so that i know where to look)
        if len(string_list[i]) == 0 or len(string_list[i]) == 1 or len(string_list[i]) == abs(p):                # would have gone back full rotation
            output.append(string_list[i])
        else:
            start = 0
            end = 0
            smthg = 0
            for j in range(len(string_list[i])):
                if string_list[i][j] != string_list[i + 1][j - p]:




    max_length = len(string_list[-1])
    for k in range(max_length):
        i = 0
        j = 0
        while i < len(string_list):          # O(NM)
            if len(comparison) < len(string):
                continue
            elif len(comparison) == len(string):

                output.append(string)
            else:
                break
    return output

    # check only in similar group (same length)
    # for each character in current string, 0 - p is same or not

'''


def sort_string_length(string_list):
    """
    Uses count sort to sort the strings in string_list by their lengths,

    :param string_list: a list of strings to be sorted by length
    :return: list of the strings from string_list sorted by their lengths in ascending order
    :time complexity: O(N + M) where N is the number of strings in string_list and M is the number of characters in the
                        longest string in string_list
    """
    max_string = string_list[0]
    for string in string_list:
        if len(string) > len(max_string):
            max_string = string

    count = []
    for i in range(len(max_string) + 1):
        count.append([])

    for string in string_list:
        count[len(string)].append(string)

    index = 0
    for lst in count:
        for string in lst:
            string_list[index] = string
            index += 1

    return string_list


import timeit


def counting_sort(num_list):
    maximum = num_list[0]
    for num in num_list:
        if num > maximum:
            maximum = num

    count = []
    for i in range(maximum + 1):
        count.append([])

    for num in num_list:
        count[num].append(num)

    index = 0
    for lst in count:
        for num in range(len(lst)):
            num_list[index] = num
            index += 1

    return num_list


if __name__ == "__main__":
    def test1():

        num_list = [2, 5, 14, 96, 1, 8]

        start_time = timeit.default_timer()
        counting_sort(num_list)
        time = timeit.default_timer() - start_time
        print(time)

        num_list = [18095545, 1844614, 396850, 213213, 21111, 3124798]

        start_time = timeit.default_timer()
        counting_sort(num_list)
        time = timeit.default_timer() - start_time
        print(time)

    test1()

"""
test from assignment 1
if __name__ == "__main__":
    def test1():

        num_list = [18446744073709551615,
                    18446744073709551614,
                    1,
                    11111111111111111111,
                    2111111111111111111,
                    311111111111111111]

        # num_list = [43,67,32,4,2,987]

        # print(radix_sort(num_list, 10))
        print(time_radix_sort())

    def test2():
        print(find_rotations(["aaa", "abc", "cab", "acb", "wxyz", 'yzwx'], 1))
        print(find_rotations(["aaa", "abc", "cab", "acb", "wxyz", 'yzwx'], 2))
        print(find_rotations(["aaa", "abc", "cab", "acb", "wxyz", 'yzwx'], 3))
        print(find_rotations(["aaa", "abc", "cab", "acb", "wxyz", 'yzwx'], 4))
        print(find_rotations(["aaa", "abc", "cab", "acb", "wxyz", 'yzwx'], 5))
        print(find_rotations(["aaa", "abc", "cab", "acb", "wxyz", 'yzwx'], -1))
        print(find_rotations(["aaa", "abc", "cab", "acb", "wxyz", 'yzwx'], -2))
        print(find_rotations(["aaa", "abc", "cab", "acb", "wxyz", 'yzwx'], -3))
        print(find_rotations(["aaa", "abc", "cab", "acb", "wxyz", 'yzwx'], -4))
        print(find_rotations(["aaa", "abc", "cab", "acb", "wxyz", 'yzwx'], -5))


    # test1()
    test2()
    # print(radix_sort_string(["yes", "no", "cat", "they", "maybe", "eventhough"]))
    # print(radix_sort_string(["hello", "fives", "eight", "cat", "tree"]))

"""
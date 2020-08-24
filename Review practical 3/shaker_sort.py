# Vanessa Joyce Tan, 30556864

import timeit
import csv
import random
random.seed(9)

def shaker_sort(a_list):
    """
    This function implements shaker sort.

    :param a_list: list of comparable items
    :return: None
    :complexity: both best case and worst case is O(n^2) where n is the length of a_list
    """
    n = len(a_list)
    mark_left = 0
    mark_right = n - 1
    while mark_left < mark_right:
        for i in range(mark_left, mark_right):
            if a_list[i] > a_list[i+1]:
                a_list[i], a_list[i+1] = a_list[i+1], a_list[i]
        mark_right -= 1
        for j in range(mark_right, mark_left, -1):
            if a_list[j] < a_list[j-1]:
                a_list[j], a_list[j-1] = a_list[j-1], a_list[j]
        mark_left += 1

def table_time_shaker_sort():
    """
    This function writes a line about time taken to create a random list and compute shaker_sort(a_list) into a csv file.

    :return: None
    """
    with open('output_ex3.csv', 'w', newline='') as csvfile:
        output_writer = csv.writer(csvfile, delimiter=',')
        n = 2
        while n <= 1024:
            a_list = []
            start_n = timeit.default_timer()
            for i in range(n):
                random_number = random.random()
                a_list.append(random_number)
            time_n = (timeit.default_timer() - start_n)

            start_list = timeit.default_timer()
            shaker_sort(a_list)
            time_list = (timeit.default_timer() - start_list)

            # Report time on a sorted list
            start_sorted = timeit.default_timer()
            shaker_sort(a_list)
            time_sorted = (timeit.default_timer() - start_sorted)

            # Report time on a reversed sorted list
            start_reverse = timeit.default_timer()
            a_list.reverse()
            shaker_sort(a_list)
            time_reverse = (timeit.default_timer() - start_reverse)

            output_writer.writerow([n,time_n,time_list,time_sorted,time_reverse])

            n = n << 1

def table_avg_time_shaker_sort():
    """
    This function writes a line about time taken to create 100 random lists and average time to compute shaker_sort(a_list) into a csv file.

    :return: None
    """
    with open('output_ex3_avg.csv', 'w', newline='') as csvfile:
        output_writer = csv.writer(csvfile, delimiter=',')
        n = 2
        while n <= 1024:
            start_n = timeit.default_timer()
            hundred = []
            for i in range(100):
                a_list = []
                for j in range(n):
                    random_number = random.random()
                    a_list.append(random_number)
                hundred.append(a_list)
            time_n = (timeit.default_timer() - start_n)

            start_sort = timeit.default_timer()
            for lst in hundred:
                shaker_sort(lst)
            time_sort = (timeit.default_timer() - start_sort)
            avg_time_sort = time_sort/100

            output_writer.writerow([n, time_n, avg_time_sort])

            n = n << 1

# table_time_shaker_sort()
# table_avg_time_shaker_sort()

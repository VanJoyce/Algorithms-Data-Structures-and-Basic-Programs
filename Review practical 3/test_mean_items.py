# Vanessa Joyce Tan, 30556864

import timeit
import mean_items
import csv
import random
random.seed(9)

def table_time_mean_items():
    """
    This function writes a line about time taken to compute mean_items(a_list) into a csv file.

    :return:
    """
    with open('output_ex2.csv', 'w', newline='') as csvfile:
        output_writer = csv.writer(csvfile, delimiter=',')
        n = 2
        while n <= 4096:
            start_n = timeit.default_timer()
            a_list = []
            for i in range(n):
                random_number = random.random()
                a_list.append(random_number)
            time_n = (timeit.default_timer() - start_n)

            start_mean = timeit.default_timer()
            mean_items.mean_items(a_list)
            time_mean = (timeit.default_timer() - start_mean)

            output_writer.writerow([n, time_n, time_mean])

            n = n << 1


# table_time_mean_items()
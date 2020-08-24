import timeit
import random
import Exercise2
import itertools


itemList = []
item = Exercise2.Item(random.randint(1, 10000), random.randint(1, 20))
itemList.append(item)
item = Exercise2.Item(random.randint(1, 10000), random.randint(1, 20))
itemList.append(item)
item = Exercise2.Item(random.randint(1, 10000), random.randint(1, 20))
itemList.append(item)
item = Exercise2.Item(random.randint(1, 10000), random.randint(1, 20))
itemList.append(item)
item = Exercise2.Item(random.randint(1, 10000), random.randint(1, 20))
itemList.append(item)
item = Exercise2.Item(random.randint(1, 10000), random.randint(1, 20))
itemList.append(item)


def bit_knapsack(itemList, capacity):
    bit_list = list(itertools.product('01', repeat=len(itemList)))

    feasible = []

    for lst in bit_list:
        value = 0
        weight = 0
        for i in range(len(lst)):
            if lst[i] == 1:
                value += itemList[i].value
                weight += itemList[i].weight
        if weight < capacity:
            feasible.append((value, lst))

    max_value = 0
    optimized = None
    for opt in feasible:
        if opt[0] > max_value:
            max_value = opt[0]
            optimized = opt

    return optimized


start_bit = timeit.default_timer()
bit_knapsack(itemList, 20)
bit_time = timeit.default_timer() - start_bit
print("Time taken for knapsack problem with brute force: " + str(bit_time))

start_dp = timeit.default_timer()
Exercise2.dp_knapsack(itemList, 20)
dp_time = timeit.default_timer() - start_dp
print("Time taken for knapsack problem with dynamic programming: " + str(dp_time))



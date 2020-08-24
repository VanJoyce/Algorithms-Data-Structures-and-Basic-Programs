"""
1. The cost is as least as possible. Lines with least unnecessary wasted space.
"""


def justify(word_list, width):
    """
    Justifies text given a list of words and number of characters.

    :param word_list: list of words in the text to be justified
    :param width: the number of characters on a line
    :return: total cost of justifying and list of lines showing solution to justification problem
    :pre-condition: word_list must only contain elements of type string, the width is bigger than the longest word in word_list
    :post-condition: total cost is the least cost possible when justifying
    :complexity: best case is O(1) when there is only one word in word_list
                 worst case is O(n^2)
    """
    inf = float("inf")

    # memory for wasted space if the line started with word i and ended with word j
    waste = [None] * (len(word_list))
    for j in range(len(waste)):
        waste[j] = [inf] * (len(word_list))

    # memory for cost
    cost = [None] * (len(word_list))
    for j in range(len(cost)):
        cost[j] = [inf] * (len(word_list))

    for i in range(len(word_list)):
        n = 1
        for j in range(len(word_list)):
            if i > j:
                continue
            elif i == j:
                waste[i][j] = width - len(word_list[i])
                cost[i][j] = waste[i][j]**3
            else:
                n += 1
                waste[i][j] = waste[i][j-1] - len(word_list[j]) - (n - 1)
                if waste[i][j] >= 0:
                    cost[i][j] = waste[i][j]**3

    cost_so_far = [inf] * (len(word_list) + 1)
    cost_so_far[-1] = 0

    line_break = [0] * (len(word_list) + 1)
    line_break[-1] = 5

    for m in range(len(word_list) - 1, -1, -1):
        cost_so_far[m] = cost[m][len(word_list) - 1]
        line_break[m] = len(word_list) - 1
        for n in range(len(word_list) - 1, -1, -1):
            if cost[m][n] == inf:
                continue
            else:
                temp_cost = cost[m][n] + cost_so_far[n+1]

                if temp_cost < cost_so_far[m]:
                    cost_so_far[m] = temp_cost
                    line_break[m] = n

    total_cost = cost_so_far[0]
    solution = []
    previous = 0
    word = 1
    line = ""
    for b in range(len(line_break)):
        if line_break[b] != previous:
            solution.append(line)
            line = ""
            previous = line_break[b]
            word = 1

        if word > 1:
            line += " "

        if b < len(word_list):
            line += word_list[b]
            word += 1

    return total_cost, solution


def test_justify():
    print(justify(["Tushar", "Roy", "likes", "to", "code"], 10))


test_justify()

"""
Vanessa Joyce Tan
30556864
Assignment 2
"""


def longest_oscillation(L):
    """
    Finds the longest oscillation in given list.

    :param L: list of integers
    :return: a tuple where first element of tuple is the length of oscillation and second element is a list of the
             indices that make up the oscillation in L
    :pre-condition: L must be a list of integers
    :post-condition: the indices in index_list will be in ascending order

    -------------------THIS TASK WAS IMPLEMENTED OPTIMALLY-------------------
    Assuming N is the length of list L,
    :time complexity: best case and worst case are both in O(N) time because every element in L needs to be checked.
    :space complexity:  O(N) because the input, L, has a length of N and length of the solution, index_list, depends on
                        the length of L. At most, the length of index_list will only be as big as L's length.
    :aux space complexity: O(N)
    """
    index_list = []
    if L is not None:
        if len(L) > 0:
            index_list.append(0)

        for i in range(1, len(L)):
            second_index = len(index_list) == 1
            prev_increase = second_index or L[index_list[-1]] > L[index_list[-2]]
            prev_decrease = second_index or L[index_list[-1]] < L[index_list[-2]]

            if L[i] < L[index_list[-1]] and prev_increase:
                if i == len(L)-1 or L[i+1] > L[i]:  # if next number is bigger, i is where a valley is
                    index_list.append(i)
            elif L[i] > L[index_list[-1]] and prev_decrease:
                if i == len(L)-1 or L[i+1] < L[i]:  # if next number is smaller, i is where a peak is
                    index_list.append(i)

    return len(index_list), index_list


def longest_walk(M):
    """
    Finds the longest increasing walk in a given matrix.

    :param M: an n x m matrix of integers represented as a list of lists
    :return:    a tuple whose first element is the longest increasing walk in M and the second element is a list of all
                the co-ordinates of the elements in that walk in order
    :pre-condition: elements in M should only be integers
    :post-condition: the resulting list of co-ordinates will be a subset of the co-ordinates of all the elements in M

    -------------------THIS TASK WAS IMPLEMENTED SUB-OPTIMALLY-------------------
    Assuming n is the number of rows and m is the number of columns in M,
    :time complexity:   best case and worst case are both O(nm log(nm)) because the recursive function has a time
                        complexity of O(log(nm)) and is called for each element in M. Even though the worst-case time
                        complexity of the recursive function longest_walk_aux() is O(nm), it is impossible for each and
                        every element in M to have a maximum recursion depth of nm.
    :space complexity: O(nm) due to size of M, memo and solution.
    :aux space complexity: O(nm) due to size of memo and solution.
    """
    memo = []
    if M is not None:
        for i in range(len(M)):
            lst = []
            for j in range(len(M[i])):
                lst.append(0)
            memo.append(lst)

    for n in range(len(memo)):
        for m in range(len(memo[n])):
            memo[n][m] = longest_walk_aux(M, memo, n, m)

    walk = 0
    coordinate = None
    solution = []
    for n in range(len(memo)):
        for m in range(len(memo[n])):
            if memo[n][m][0] > walk:
                walk = memo[n][m][0]
                coordinate = memo[n][m][1]
                solution = [(n, m)]

    while coordinate is not None:
        solution.append(coordinate)
        coordinate = memo[coordinate[0]][coordinate[1]][1]

    return walk, solution


def longest_walk_aux(M, memo, row, col):
    """
    Recursive call to fill memo for longest_walk function.

    :param M: the original matrix represented as a list of lists
    :param memo: a list of lists which stores the tuples. Each element in memo corresponds to the number in M.
    :param row: the row index of the current number
    :param col: the column index of the current number
    :return: a tuple whose first element contains the longest walk that starts with the current number and the
             coordinates of the next element in the longest walk
    :pre-condition: M and memo must be a list of lists. memo must be initialised with all 0s
    :post-condition: longest walk returned is longest walk that starts with current number.

    Assuming n is the number of rows and m is the number of columns in M,
    :time complexity:   best case is O(log(nm)) because time complexity depends on recursion depth and each recursive
                        call is in constant time since the for loops for the directions are constant.
                        worst case is O(nm) when recursive depth is equal to the number of elements in M (when the
                        longest walk includes all elements of M)
    :space complexity:  O(nm) because of the size of memo and M. Because they are both passed in each recursive call,
                        the number of recursive calls does not affect space complexity.
    :aux space complexity: O(nm) because each recursive call has constant space and maximum recursion depth is nm.
    """
    if row < 0 or col < 0 or row >= len(M) or col >= len(M[0]):     # edge cases when row or col is out of range
        return -1, None
    elif memo[row][col] != 0:       # already filled in memo
        return memo[row][col]
    else:
        max_walk = 0
        next_elem = None
        for v_step in range(-1, 2):
            for h_step in range(-1, 2):
                i = row + v_step
                j = col + h_step
                if v_step == 0 and h_step == 0:     # is current element, no need to check
                    continue
                if 0 <= i < len(M) and 0 <= j < len(M[0]) and M[i][j] > M[row][col]:
                    memo_neighbour = longest_walk_aux(M, memo, i, j)
                    memo[i][j] = memo_neighbour
                    if memo_neighbour[0] > max_walk:
                        max_walk = memo_neighbour[0]
                        next_elem = (i, j)
        return 1+max_walk, next_elem





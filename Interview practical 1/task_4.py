"""
Vanessa Joyce Tan
30556864
Interview Prac 1 Week 4
Task 4
"""

def bubble_sort(the_list):
    """
    This function implements bubble sort
    :param the_list: a list of comparable elements
    :return: None
    :raises: No exceptions
    :complexity: both best and worst case O(n^2), where n is len(the_list)
    """
    n = len(the_list)                           # assign the length of the_list to variable n
    for a in range(n-1):                        # repeats the loop from a = 0 until a = n-1 (loop for n - 1 times)
        for i in range(n-1):                    # repeats the loop until i = n-1 (loop for n - 1 times)
            item = the_list[i]                  # assign the_list[i] to variable item
            item_to_right = the_list[i+1]       # item_to_right refers to the element to the right of item
            if item > item_to_right:            # if item is more than item_to_right, execute following indented block
                # swap item and item_to_right
                the_list[i] = item_to_right     # assign value in item_to_right to the_list[i]
                the_list[i+1] = item            # assign value in item to the_list[i+1]

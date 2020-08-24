# Vanessa Joyce Tan, 30556864

def mean_items(a_list):
    """
    This function calculates and returns the mean of all the items in a_list

    :param a_list: list we want to calculate mean for
    :return: mean of all the items in a_list
    :raises: ZeroDivisionError
    :precondition: a_list must be a list of real numbers.
    :complexity: both best case and worst case is O(n) where n is the length of a_list
    """
    if (len(a_list) > 0):
        sum = 0
        for i in range(len(a_list)):
            sum += a_list[i]
        return sum / len(a_list)
    else :
        raise ZeroDivisionError


def test_mean_items():
    """
    This function tests the function mean_items(a_list)

    :return: None
    """
    assert mean_items([1,5]) == 3, "test1 failed"
    assert mean_items([4.3,6.8]) == 5.55, "test2 failed"
    assert mean_items([1,-5]) == -2, "test3 failed"
    assert mean_items([0,0,0,0]) == 0, "test4 failed"
    try:
        mean_items([])
        print("test5 failed")
    except ZeroDivisionError:
        print("test passed")

test_mean_items()


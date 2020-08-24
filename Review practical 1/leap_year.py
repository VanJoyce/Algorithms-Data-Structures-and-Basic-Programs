year = int(input('Enter year: '))
leap_year = False

def is_leap_year(year):
    """
    This function checks if the year is a leap year.
    :param year: the year
    :return: statement whether the year is a leap year or not.
    :raises: No exceptions
    :precondition: year must be a four digit integer.
    :complexity: best case and worst case both O(1).
    """
    if year %4 != 0:
        leap_year = False
    elif year % 100 != 0:
        leap_year = True
    elif year % 400 != 0:
        leap_year = False
    else:
        leap_year = True

    if leap_year:
        string = ""
    else:
        string = " not"
    # a simpler form would be: string = "" if leap_year  else " not"

    print(year, "is" + string, "a leap year")

is_leap_year(year)
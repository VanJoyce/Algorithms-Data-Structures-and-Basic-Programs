def print_menu():
    """
    This function prints the menu
    :return: menu of options
    :complexity: O(1) for both best case and worst case
    """
    print("\nMenu: ")
    print("1. Convert decimal into binary")
    print("2. Convert decimal into hexadecimal")
    print("3. Quit")

def binary(decimal):
    """
    This function converts decimal numbers into binary
    :param decimal: a number in decimal representation
    :return: the number in binary representation
    :precondition: decimal must be a positive number
    :complexity: best case is O(1) if the decimal number is less than 2, worst case is O(log n) where n is the decimal number
    """
    binary_number = ""
    if decimal == 0:
        binary_number += "0"
    else :
        while decimal != 0:
            binary_number = str(decimal % 2) + binary_number
            decimal //= 2
    return binary_number


def hexadecimal(decimal):
    """
    This function converts decimal numbers into hexadecimal
    :param decimal: a number in decimal representation
    :return: the number in hexadecimal representation
    :precondition: decimal must be a positive number
    :complexity: best case is O(1) if the decimal number is less than 16, worst case is O(log n) where n is the decimal number
    """
    hexadecimal_number = ""
    if decimal == 0:
        hexadecimal_number += "0"
    else:
        while decimal != 0:
            if (decimal % 16) <= 9:
                hexadecimal_number = str(decimal % 16) + hexadecimal_number
            elif (decimal % 16) == 10:
                hexadecimal_number = "A" + hexadecimal_number
            elif (decimal % 16) == 11:
                hexadecimal_number = "B" + hexadecimal_number
            elif (decimal % 16) == 12:
                hexadecimal_number = "C" + hexadecimal_number
            elif (decimal % 16) == 13:
                hexadecimal_number = "D" + hexadecimal_number
            elif (decimal % 16) == 14:
                hexadecimal_number = "E" + hexadecimal_number
            elif (decimal % 16) == 15:
                hexadecimal_number = "F" + hexadecimal_number
            decimal //= 16
    return hexadecimal_number

quit = False

while not quit:
    print_menu()
    command = int(input("\nEnter command: "))

    if command == 1:
        number = int(input("Number to convert to binary: "))
        print(str(number) + " in binary is " + binary(number))
    elif command == 2:
        number = int(input("Number to convert to hexadecimal: "))
        print(str(number) + " in hexadecimal is " + hexadecimal(number))
    elif command == 3:
        quit = True

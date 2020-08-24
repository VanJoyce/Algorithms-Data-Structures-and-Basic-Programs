def print_menu():
    print('\nMenu:')
    print('1. append')
    print('2. reverse')
    print('3. print')
    print('4. quit')
    print('5. pop')
    print('6. count')

def reverse(my_list):
    length = len(my_list)
    for i in range(length//2):
        temp = my_list[i]
        my_list[i] = my_list[length -i-1]
        my_list[length -i-1]=temp

def pop(my_list):
    """
    This function removes the last item of the list, and prints it.
    :param my_list: a list of any order
    :return: my_list without the last element
    :raises: No exceptions
    :precondition: my_list must not be empty
    :complexity: best case is O(1) when there is only one item in the list, worst case is O(n) where n is the length of my_list
    """
    print(my_list[len(my_list)-1])
    new_list = []
    for i in range(len(my_list)-1):
        new_list.append(my_list[i])
    return new_list

def count(my_list, value):
    """
    This function prints the number of times a given value appears in the list.
    :param my_list: a list of any order
    :param value: the value you want to check appears how many times in my_list
    :return: the number of times value appears in my_list
    :complexity: best case is O(1) when there is only one item in the list, worst case is O(n) where n is the length of my_list
    """
    counter = 0
    for i in range(len(my_list)):
        if my_list[i] == int(value):
            counter += 1
    return counter

my_list = [13,6,5,4,6]
quit = False
input_line = None

while not quit:
    print_menu()
    command = int(input("\nEnter command: "))

    if command == 1:
        item = input("Item? ")
        my_list.append(item)
    elif command == 2:
        reverse(my_list)
    elif command == 3:
        print(my_list)
    elif command == 4:
        quit = True
    elif command == 5:
        my_list = pop(my_list)
    elif command == 6:
        value = input("Value? ")
        print(count(my_list, value))
        

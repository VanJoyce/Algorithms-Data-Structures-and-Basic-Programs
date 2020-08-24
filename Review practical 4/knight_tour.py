import tour

def position():
    """
    Reads user input and moves knight to that position if it is a valid move

    :return: None
    :complexity: best case is O(1) and worst case is O(n) where n is the number of times the user has to input
    """
    while True:
        pos = input("Position (eg. 4d): ")
        row = int(pos[0])
        col = ord(pos[-1]) - 96
        if the_tour.valid_move(row, col):
            the_tour.move_knight(row, col)
            break
        else:
            print("That's an invalid move. Enter another position.")

def restart():
    """
    Empties the chess board and resets the knight to starting position at (1, 1)

    :return: None
    :complexity: best case and worst case is both O(n) where n is the length of the list 'next'
    """
    the_tour.moves.reset()
    the_tour.moves.add_last((1,1))
    nxt = the_tour.next_moves()
    outstring = "Next possible moves:\n"
    for i in range(nxt.length()):
        move = nxt.get_item(i)
        string = ""
        valid = the_tour.valid_move(move[0], move[1])
        if valid:
            string += str(move[0]) + chr(move[1]+96) + "\n"
            outstring += string
    print(outstring)

the_tour = tour.Tour()
while True:
    the_tour.show_tour()

    print("---MENU---")
    print("1    position")
    print("2    undo")
    print("3    save")
    print("4    restore")
    print("5    restart")
    print("6    quit")

    while True:
        try:
            option = input("Please select an option using its number: ")
            assert 0 < int(option) < 7
        except AssertionError:
            print("Please enter a number from the menu.")
            continue
        except ValueError:
            print("Please enter an integer.")
            continue
        break

    if option == "1":
        position()
    elif option == "2":
        try:
            the_tour.undo()
        except AssertionError:
            print("Can't undo anymore")
    elif option == "3":
        the_tour.copy()
    elif option == "4":
        try:
            the_tour.set()
        except AttributeError:
            print("You haven't saved before")
    elif option == "5":
        restart()
    elif option == "6":
        break
    else:
        continue



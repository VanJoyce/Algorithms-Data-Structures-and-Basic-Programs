from unsorted_list import List

class Tour:
    board_rows = 8
    board_cols = 8
    board_size = board_rows * board_cols

    directions = [(2, 1), (2, -1), (-2, 1), (-2, -1),(1, 2), (-1, 2), (1, -2), (-1, -2)]

    def __init__(self):
        """
        Creates an object of class Tour.

        :return:    a list data structure
        :complexity:    best and worst case: the complexity of List(Tour.board_size)
                        which is probably O(board_size)
        """
        # You may wish to add additional attributes to the object.
        self.moves = List(Tour.board_size)
        self.moves.add_last( (1, 1) ) # Set a starting position

    def move_knight(self, row, col):
        """
        Adds the new position of the knight into the tour.

        :param row: number representing which row to move to
        :param col: number representing which column to move to
        :return: None
        :raise: AssertionError when the position specified is out of the board
        :complexity: best and worst cases are both O(1)
        """
        assert self.moves.length() < Tour.board_size
        self.moves.add_last( (row, col) )

    def show_tour(self):
        """
        Displays the chess board with the position of the knight marked with a K,
        and all previous positions marked with a *

        :return: chess board marked with K and *
        :complexity: best and worst cases both O(n^2) where n is the number of rows/columns in the chess board.
        """
        for r in range(1, Tour.board_rows+1):
            for c in range(1, Tour.board_cols+1):
                pos = self.moves.index( (r, c) )
                cell_char = ' '
                if pos is not None:
                    if pos == self.moves.length()-1:
                        cell_char = 'K'
                    else:
                        cell_char = '*'

                print(cell_char, end='')
            print('')

    def next_moves(self):
        """
        Creates a list of possible next moves from the last position

        :return: a list of tuples representing positions of possible next moves
        :complexity: best case is O(1) and worst case is O(n) where n is the length of the list moves.
        """
        self.next = List(8)
        last_index = self.moves.length() - 1
        start = self.moves.get_item(last_index)
        for d in Tour.directions:
            row = start[0]+d[0]
            col = start[1]+d[1]
            not_out_of_bounds = (1 <= row <= 8) and (1 <= col <= 8)

            visited = False
            for ind in range(self.moves.length()):
                if (row, col) == self.moves.get_item(ind):
                    visited = True
                    break
                else:
                    continue

            if not visited and not_out_of_bounds:
                self.next.add_last((row, col))

        return self.next

    def valid_move(self, row, col):
        """
        Checks if position entered is a possible next move from the previous position.

        :param row: the row of the position specified
        :param col: the column of the position specified
        :pre-condition: row and col must be of int type
        :return: True if it's a valid move, False otherwise
        :complexity: best case and worst case is O(1)
        """
        nxt = self.next_moves()
        for ind in range(nxt.length()):
            if (row, col) == nxt.get_item(ind):
                return True
            else:
                continue
        return False

    def undo(self):
        """
        Undo the last move.

        :return: None
        :pre-condition: the length of the tour must be more than 1
        :post-condition: the length of the tour is one less than before
        :complexity: both best and worst case should be same as delete_item() function which is O(length*M)
        """
        try:
            assert self.moves.length() > 1
        except AssertionError:
            raise AssertionError("The knight never moved!")
        index = self.moves.length() - 1
        last_move = self.moves.get_item(index)
        self.moves.delete_item(last_move)

    def copy(self):
        """
        Makes a copy of the current chess board.

        :return: None
        :post-condition:    The copied board must be exactly the same as the current board.
                            If a move is made on the current board, the copied board must remain unchanged.
        :complexity: best and worst case is O(n) where n is the length of the tour
        """
        self.save = List(Tour.board_size)
        for i in range(self.moves.length()):
            position = self.moves.get_item(i)
            self.save.add_last(position)

    def set(self):
        """
        Resets the board to the last saved board.

        :return: None
        :complexity: best and worst case are both O(1)
        """
        self.moves = List(Tour.board_size)
        for i in range(self.save.length()):
            self.moves.add_last(self.save.get_item(i))

def test_move_knight():
    test_tour = Tour()
    try:
        test_tour.move_knight(3, 2)
        index = test_tour.moves.length() - 1
        assert test_tour.moves.get_item(index) == (3, 2)
    except AssertionError:
        print("move1 failed")
    try:
        test_tour.move_knight(4, 4)
        index = test_tour.moves.length() - 1
        assert test_tour.moves.get_item(index) == (4, 4)
    except AssertionError:
        print("move2 failed")
    try:
        test_tour.move_knight(1, 2)
        index = test_tour.moves.length() - 1
        assert test_tour.moves.get_item(index) == (1, 2)
    except AssertionError:
        print("move3 failed")
    print("move_knight passed")

def test_valid_move():
    test_tour = Tour()
    test_tour.move_knight(3,2)
    assert test_tour.valid_move(1, 1) == False, "valid1 failed"
    assert test_tour.valid_move(1, 3) == True, "valid2 failed"
    assert test_tour.valid_move(0, -1) == False, "valid3 failed"
    print("valid_move passed")

def test_undo():
    test_tour = Tour()
    try:
        assert test_tour.undo()
    except AssertionError:
        pass #undo1 passed
    test_tour.move_knight(3, 2)
    test_tour.undo()
    last = test_tour.moves.length() - 1
    assert test_tour.moves.get_item(last) == (1, 1), "undo2 failed"
    print("undo passed")

def test_copy():
    test_tour = Tour()

    test_tour.move_knight(3, 2)
    test_tour.move_knight(4, 4)
    test_tour.copy()

    last = test_tour.save.length() - 1
    assert test_tour.save.get_item(last) == (4, 4), "copy1 failed"

    test_tour.move_knight(3, 6)
    assert test_tour.save.get_item(last) == (4, 4), "copy2 failed"
    print("copy passed")

def test_set():
    test_tour = Tour()

    try:
        test_tour.set()
    except AttributeError:
        pass #no attribute 'save', "set1 passed"

    test_tour.move_knight(2, 3)
    test_tour.copy()
    test_tour.move_knight(4, 2)
    test_tour.set()
    last = test_tour.moves.length() - 1
    assert test_tour.moves.get_item(last) == (2, 3), "set2 failed"

    print("set passed")

if __name__ == '__main__':

    test_move_knight()
    test_valid_move()
    test_undo()
    test_copy()
    test_set()

    the_tour = Tour()

    the_tour.move_knight(2, 3)
    the_tour.move_knight(4, 2)
    the_tour.show_tour()
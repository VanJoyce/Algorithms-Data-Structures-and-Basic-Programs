import copy

def new_board():
    new_board = [[0,0,0,0,0,0,0,0],
                 [0,0,0,0,0,0,0,0],
                 [0,0,0,0,0,0,0,0],
                 [0,0,0,2,1,0,0,0],
                 [0,0,0,1,2,0,0,0],
                 [0,0,0,0,0,0,0,0],
                 [0,0,0,0,0,0,0,0],
                 [0,0,0,0,0,0,0,0]]
    return new_board

def print_board(board):
    c_label = "   | a | b | c | d | e | f | g | h "
    for r in range(len(board)):
        r_label = r + 1
        row = " " + str(r_label) + " "
        for c in range(len(board[r])):
            if board[r][c] == 1:
                row += "| B "
            elif board[r][c] == 2:
                row += "| W "
            elif board[r][c] == 0:
                row += "|   "
        print(row)
        print("-" * len(c_label))
    print(c_label)
            

def score(board):
    s1 = 0; s2 = 0
    for r in range(len(board)):
        for c in range(len(board[r])):
            if board[r][c] == 1:
                s1 += 1
            elif board[r][c] == 2:
                s2 += 1
    return (s1, s2)

def enclosing(board, player, pos, direct):
    r = pos[0]; c = pos[1]
    dr = direct[0]; dc = direct[1]
    i = r + 2*dr; j = c + 2*dc      #position counter for current player's stone
    m = r + dr; n = c + dc          #position counter for other player's stone
    stones = 0
    while 0 <= i < 8 and 0 <= j < 8:
        if board[i][j] == player:
            while i < m < r or r < m < i or j < n < c or c < n < j:
                if board[m][n] != player and board[m][n] != 0:
                    stones += 1
                    m += dr
                    n += dc
                else :
                    return False
            if stones == abs(i - r) - 1 or stones == abs(j - c) - 1:
                return True
            else :
                return False                  
        else :
            i += dr
            j += dc
    return False

direct_list = [(0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1)]

def valid_moves(board, player):
    valid_list = []
    for r in range(len(board)):
        for c in range(len(board[r])):
            for direct in direct_list:
                pos = (r, c)
                if enclosing(board, player, pos, direct) == True and board[r][c] == 0 and pos not in valid_list:
                    valid_list.append(pos)
    return valid_list

def nxt_player(board, player):
    if player == 1:
        next_player = 2
        valid_list = valid_moves(board, next_player)
        if valid_list == []:
            next_player = 1
            valid_list = valid_moves(board, next_player)
            if valid_list == []:
                next_player = 0
    else :
        next_player = 1
        valid_list = valid_moves(board, next_player)
        if valid_list == []:
            next_player = 2
            valid_list = valid_moves(board, next_player)
            if valid_list == []:
                next_player = 0
    return next_player

def next_state(board, player, pos):
    r = pos[0]; c = pos[1]
    next_board = board
    next_board[r][c] = player
    for direct in direct_list:
        dr = direct[0]; dc = direct[1]
        if enclosing(next_board, player, pos, direct) == True:
            m = r + dr; n = c + dc
            while next_board[m][n] != player:
                next_board[m][n] = player
                m += dr
                n += dc
    next_player = nxt_player(next_board, player)
    return (next_board, next_player)

def position(string):
    if len(string) > 2 or len(string) == 0:
        return None
    else:  
        string_list = []
        for character in string:
            string_list.append(character)
        r_label = ["1", "2", "3", "4", "5", "6", "7", "8"]
        c_label = ["a", "b", "c", "d", "e", "f", "g", "h"]
        for r in range(len(r_label)):
            if string_list[-1] == r_label[r]:
                for c in range(len(c_label)):
                    if string_list[0] == c_label[c]:
                        return (r, c)
        return None

def run_two_players():
    board = copy.deepcopy(new_board())
    player = 1
    while True:
        print_board(board)
        if player == 1:
            print("It's Player 1's turn (B)")
        else :
            print("It's Player 2's turn (W)")
        string = input('Pick a position to place a stone (in the format "d4"): ')
        if string == "q":
            break
        pos = position(string)
        if pos not in valid_moves(board, player):
            print("invalid move")
        else :
            (board, player) = next_state(board, player, pos)
            if player == 0:
                print_board(board)
                (s1, s2) = score(board)
                print("GAME OVER")
                if s1 > s2:
                    print("Player 1 wins!")
                elif s2 > s1:
                    print("Player 2 wins!")
                else :
                    print("It's a draw!")
                print("SCOREBOARD:")
                print("Player 1: " + str(s1))
                print("Player 2: " + str(s2))
                break

def maximal_score(board, player, valid_list):
    max_score = 0
    for pos in valid_list:
        r = pos[0]; c = pos[1]
        score = 0
        for direct in direct_list:
            if enclosing(board, player, pos, direct) == True:
                dr = direct[0]; dc = direct[1]
                i = r + dr
                j = c + dc
                while 0 <= i < 8 and 0 <= j < 8:
                    if board[i][j] != player and board[i][j] != 0:
                        score += 1
                    i += dr
                    j += dc
        if score > max_score:
            max_score = score
            position = pos
    return position
                
def run_single_player():
    board = copy.deepcopy(new_board())
    player = 1
    while True:
        print_board(board)
        print("It's your turn (B)")
        string = input('Pick a position to place a stone (in the format "d4"): ')
        if string == "q":
            break
        pos = position(string)
        if pos not in valid_moves(board, player):
            print("invalid move")
        else :
            (board, player) = next_state(board, player, pos)
            while player == 2:
                print_board(board)
                print("Player 2's turn (W)")
                pos = maximal_score(board, player, valid_moves(board, player))
                (board, player) = next_state(board, player, pos)
            if player == 0:
                print_board(board)
                (s1, s2) = score(board)
                print("GAME OVER")
                if s1 > s2:
                    print("Player 1 wins!")
                elif s2 > s1:
                    print("Player 2 wins!")
                else :
                    print("It's a draw!")
                print("SCOREBOARD:")
                print("Player 1: " + str(s1))
                print("Player 2: " + str(s2))
                break
        
    

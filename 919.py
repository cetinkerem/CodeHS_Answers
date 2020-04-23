"""
This program simulates the game of tic tac toe.
"""

# get_valid_index
# -----
# Get row or column from user
def get_valid_index(prompt):
    while True:
        try:
            index = int(input(prompt))
            if index >= 0 and index <= 2:
                return index
            print "Must be 0 - 2 inclusive!"
        except ValueError:
            print "Must be an integer!"

# game_is_over
# -----
# Return True if the game is over and False
# otherwise. Print a message indicating who
# won or whether there was a tie.
def game_is_over(board):
    for i in range(3):
        # Check horizontal
        if board[i][0] == board[i][1] == board[i][2] \
            and board[i][0] != " ":
            print board[i][0] + " wins!"
            return True
        
        # Check vertical
        if board[0][i] == board[1][i] == board[2][i] \
            and board[0][i] != " ":
            print board[0][i] + " wins!"
            return True
        
    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] \
        and board[0][0] != " ":
        print board[0][0] + " wins!"
        return True
    
    if board[2][0] == board[1][1] == board[0][2] \
        and board[2][0] != " ":
        print board[2][0] + " wins!"
        return True
    
    # Check tie
    if " " not in board[0] and " " not in board[1] \
        and " " not in board[2]:
        print "Tie game!"
        return True
    
    # Not over yet!
    return False
    
# print_board
# -----
# Print the board.
def print_board(board):
    for i in board:
        print "['" + "', '".join(i) + "']"

# Set up board
board = []
for i in range(3):
    board.append([" "] * 3)

# x goes first
turn = "x"

# Play tic tac toe
for i in range(9):
    print_board(board)
    print "It's " + turn + "'s turn."
    
    row = 0
    col = 0
    
    while 1:
        row = get_valid_index("Row: ")
        col = get_valid_index("Col: ")
    
        if board[row][col] != " ":
            print "That space is not empty"
            continue
        else:
            break
    
    board[row][col] = turn
    
    if game_is_over(board):
        break
    
    if turn == "x":
        turn = "o"
    else:
        turn = "x"

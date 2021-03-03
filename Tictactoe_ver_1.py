# TicTacToe

# Written in jupyter notebook so imported clear_output()
## ( from IPython.display import clear_output )
def display_board(board):
#   Simple Display board
## (   clear_output() )
    print(board[7] + '|' +board[8] + '|' +board[9])
    print(board[4] + '|' +board[5] + '|' +board[6])
    print(board[1] + '|' +board[2] + '|' +board[3])

## test_board_2 = [' ','1','2','3','4','5','6','7','8','9']
## display_board(test_board_2)

test_board = ['#','X','O','X','O','X','O','X','O','X']
display_board(test_board)

# function that can take in a player input and assign their marker as 'X' or 'O'
def player_input():
    marker = ''
    #     continue asking until user inputs correct answer
    while marker != 'X' and marker != 'O':
        marker = input("Player 1, Choose X or O: ").upper()

    player1 = marker

    if player1 == 'X':
        player2 = 'O'
    else:
        player2 = 'X'

    return (player1, player2)
# tuple formed in order to store p1 and p2 inputs
player1_marker, player2_marker = player_input()
# print(player1_marker)
# print(player2_marker)
# print(player_input())

# function that takes in the board list object, a marker ('X' or 'O'), and a desired position (number 1-9) and assigns it to the board
def place_marker(board, marker, position):
    board[position] = marker
# place_marker(test_board,'$',8)
# display_board(test_board)

# function that takes in a board and a mark (X or O) and then checks to see if that mark has won
def win_check(board, mark):
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or  # top row
            (board[4] == mark and board[5] == mark and board[6] == mark) or  # 2nd row
            (board[1] == mark and board[2] == mark and board[3] == mark) or  # bottom row
            (board[7] == mark and board[4] == mark and board[1] == mark) or  # left 1st column
            (board[8] == mark and board[5] == mark and board[2] == mark) or  # 2nd column
            (board[9] == mark and board[6] == mark and board[3] == mark) or  # right #last column
            (board[7] == mark and board[5] == mark and board[3] == mark) or  # left to right diagonally
            (board[1] == mark and board[5] == mark and board[9] == mark))  # rigth to left diagonally

win_check(test_board,'O')

# function to randomly decide which player goes first
import random

def choose_first():
    toss = random.randint(0,1)
    if toss == 0:
        return 'Player 1'
    else:
        return 'Player 2'

# function that returns a boolean indicating whether a space on the board is freely available
def space_check(board, position):
    return board[position] == " "

# function that checks if the board is full and returns a boolean value. True if full, False otherwise.
def full_board_check(board):
    for i in range(1, 10):
        if space_check(board, i):
            return False
    return True
full_board_check(test_board)

# function that asks for a player's next position (as a number 1-9) and checks if it's a free position
def player_choice(board):
    position = 0

    while position not in [1, 2, 3, 4, 5, 6, 7, 8, 9] or not space_check(board, position):
        position = int(input('Choose your next position: (1-9) '))

    return position

# function that asks the player if they want to play again
def replay():
    return input('Do you want to play again? Enter Yes or No: ').lower().startswith('yes')

# Using all functions made above to run the game
print('Welcome to Tic Tac Toe!')

while True:
    # Reset the board
    theBoard = [' '] * 10
    player1_marker, player2_marker = player_input()
    turn = choose_first()
    print(turn + ' will go first.')

    play_game = input('Are you ready to play? Enter Yes or No.')

    if play_game.lower() == 'yes':
        game_on = True
    else:
        game_on = False

    while game_on:
        if turn == 'Player 1':
            # Player1's turn.

            display_board(theBoard)
            position = player_choice(theBoard)
            place_marker(theBoard, player1_marker, position)

            if win_check(theBoard, player1_marker):
                display_board(theBoard)
                print('Congratulations! You have won the game!')
                game_on = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print('The game is a draw!')
                    break
                else:
                    turn = 'Player 2'

        else:
            # Player2's turn.

            display_board(theBoard)
            position = player_choice(theBoard)
            place_marker(theBoard, player2_marker, position)

            if win_check(theBoard, player2_marker):
                display_board(theBoard)
                print('Player 2 has won!')
                game_on = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print('The game is a draw!')
                    break
                else:
                    turn = 'Player 1'

    if not replay():
        break
import random
import sys
import time

WIDTH = 8
HEIGHT = 8
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

# color_text() example usage:
# print(color_text("This is a header", bcolors.HEADER))
# print(color_text("This is blue text", bcolors.OKBLUE))
# print(color_text("This is cyan text", bcolors.OKCYAN))
# print(color_text("This is green text", bcolors.OKGREEN))
# print(color_text("This is a warning", bcolors.WARNING))
# print(color_text("This is a failure", bcolors.FAIL))
# print(color_text("This is bold text", bcolors.BOLD))
# print(color_text("This is underlined text", bcolors.UNDERLINE))
def color_text(text, color):
    return f"{color}{text}{bcolors.ENDC}"

def clear_screen():
    print("\033[H\033[J", end="")

def draw_board(board):
    print(color_text('  12345678', bcolors.HEADER))
    print(color_text(' +--------+', bcolors.OKCYAN))
    for y in range(HEIGHT):
        print(f'%s{bcolors.OKCYAN}|{bcolors.ENDC}' % (y+1), end='')
        for x in range(WIDTH):
            if (board[x][y] == 'X'):
                print(f'{bcolors.OKGREEN}X{bcolors.ENDC}', end='')
            else:
                print(board[x][y], end='')
        print(f'{bcolors.OKCYAN}|{bcolors.ENDC}%s' % (y+1))
    print(color_text(' +--------+', bcolors.OKCYAN))
    print(color_text('  12345678', bcolors.HEADER))


def get_new_board():
    board = []
    for i in range(WIDTH):
        board.append([' '] * WIDTH)
    return board


def initiate_board(board):
    board[3][3] = 'X'
    board[3][4] = 'O'
    board[4][3] = 'O'
    board[4][4] = 'X'


# Display methods
def intro_message():
    print(f'''
                ██████╗░███████╗██╗░░░██╗███████╗███████╗██╗
                ██╔══██╗██╔════╝██║░░░██║██╔════╝██╔════╝██║
                ██████╔╝█████╗░░╚██╗░██╔╝█████╗░░█████╗░░██║
                ██╔══██╗██╔══╝░░░╚████╔╝░██╔══╝░░██╔══╝░░██║
                ██║░░██║███████╗░░╚██╔╝░░███████╗███████╗██║
                ╚═╝░░╚═╝╚══════╝░░░╚═╝░░░╚══════╝╚══════╝╚═╝

                Welcome to Reversi - The Strategic Game of Othello!

                Prepare to engage in an epic battle of wits and strategy. 
                Flip your opponent's pieces and dominate the board.
                May the best strategist win!

                To make a move, type the x and y coordinates of the piece you want to place.
                For example, to place a piece at the top left corner, type 1 1.
          ''')


def slow_print(text, delay=0.03):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def display_intro():
    clear_screen()
    intro_message()
    
    print("\n")
    slow_print(color_text("Press 'Enter' to begin..", bcolors.OKGREEN))
    
    # Final motivational message
    print("\n" + color_text("To quit the game, type 'Quit'.", bcolors.OKBLUE))

    # Brief pause
    # time.sleep(1)
    user_input = input()
    if user_input.lower().startswith('q'):
        sys.exit()
    else:
        clear_screen()
        print("Please select which symbol you would like to play as: X or O")
        symbol = input()
        if symbol.lower() == 'x':
            player_symbol = 'X'
            computer_symbol = 'O'
        else:
            player_symbol = 'O'
            computer_symbol = 'X'            
        board = get_new_board()
        initiate_board(board)
        # TODO: need to define who starts, but for now let's assume player starts
        players_turn(board, player_symbol)
        draw_board(board)
# /end Display methods

def players_turn(board, player_symbol):
    print(f"Player's turn ({player_symbol})")
    draw_board(board)
    print("Enter your move: ")
    
    while True:
        try:
            move = handle_move_input(input())
            if is_valid_move(board, move):
                break
            else:
                print(color_text("Invalid move. Please enter a valid move within the board values.", bcolors.FAIL))
        except ValueError:
            print(color_text("Invalid input format. Please enter row and column separated by a space.", bcolors.FAIL))
    
    make_move(board, move[0], move[1], player_symbol)
    return board

def handle_move_input(input):
    if input.lower().startswith('q'):
        sys.exit()
    x, y = input.split()
    x = int(x) - 1
    y = int(y) - 1
    return x, y

def make_move(board, x, y, symbol):
    board[y][x] = symbol
    return board

def is_valid_move(board, move):
    if len(move) != 2:
        return False
    row, col = move
    if not (0 <= row < len(board) and 0 <= col < len(board[0])):
        return False
    if board[row][col] != ' ':
        return False
    return True

def available_moves(board, symbol):
    moves = []
    # define valid available moves


display_intro()


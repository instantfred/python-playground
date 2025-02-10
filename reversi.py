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

def boot_game():
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
    return [player_symbol, computer_symbol]
# /end Display methods

def players_turn(board, player_symbol):
    print(f"Player's turn ({player_symbol})")
    # draw_board(board)
    print("Enter your move: ")
    
    while True:
        print('Enter your move or type "quit" to end the game.')
        try:
            move = handle_move_input(input())
            x, y = move
            if is_valid_move(board, player_symbol, x, y):
                break
            else:
                print(color_text("Invalid move. Please enter a valid move within the board values.", bcolors.FAIL))
        except ValueError:
            print(color_text("Invalid input format. Please enter row and column separated by a space.", bcolors.FAIL))
    print("making the move")
    make_move(board, player_symbol, move[0], move[1])
    return board

def handle_move_input(input):
    if input.lower().startswith('q'):
        print(color_text('Thanks for playing!', bcolors.UNDERLINE))
        sys.exit()
    x, y = input.split()
    x = int(x) - 1
    y = int(y) - 1
    return x, y

def make_move(board, symbol, xstart, ystart):
    tiles_to_flip = is_valid_move(board, symbol, xstart, ystart)

    if tiles_to_flip == False:
        return False

    board[xstart][ystart] = symbol
    for x, y in tiles_to_flip:
        board[x][y] = symbol
    return True

def is_on_board(x, y):
    return x >= 0 and x <= WIDTH - 1 and y >= 0 and y <= HEIGHT - 1

def is_on_corner(x, y):
    # Returns True if the position is in one of the four corners.
    return (x == 0 or x == WIDTH - 1) and (y == 0 or y == HEIGHT - 1)

def is_valid_move(board, tile, xstart, ystart):
    # Returns False if the player's move on space xstart, ystart is invalid.
    # If it is a valid move, returns a list of spaces that would become the player's if they made a move here.
    if not is_on_board(xstart, ystart) or board[xstart][ystart] != ' ':
        return False

    if tile == 'X':
        other_tile = 'O'
    else:
        other_tile = 'X'

    tiles_to_flip = []
    for xdirection, ydirection in [[0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1], [-1, 0], [-1, 1]]:
        x, y = xstart, ystart
        x += xdirection # First step in the x direction
        y += ydirection # First step in the y direction
        while is_on_board(x, y) and board[x][y] == other_tile:
            # Keep moving in this x & y direction.
            x += xdirection
            y += ydirection
            if is_on_board(x, y) and board[x][y] == tile:
                # There are pieces to flip over. Go in the reverse direction until we reach the original space, noting all the tiles along the way.
                while True:
                    x -= xdirection
                    y -= ydirection
                    if x == xstart and y == ystart:
                        break
                    tiles_to_flip.append([x, y])

    if len(tiles_to_flip) == 0: # If no tiles were flipped, this is not a valid move.
        return False
    return tiles_to_flip

def get_valid_moves(board, symbol):
    valid_moves = []
    for x in range(WIDTH):
        for y in range(HEIGHT):
            if is_valid_move(board, symbol, x, y) != False:
                valid_moves.append([x, y])
    return valid_moves

def print_score(board, player_symbol, computer_symbol):
    scores = get_score_of_board(board)
    print(color_text('You: %s points. Computer: %s points.' % (scores[player_symbol], scores[computer_symbol]), bcolors.OKGREEN))

def get_score_of_board(board):
    xscore = 0
    oscore = 0
    for x in range(WIDTH):
        for y in range(HEIGHT):
            if board[x][y] == 'X':
                xscore += 1
            if board[x][y] == 'O':
                oscore += 1
    return {'X':xscore, 'O':oscore}

def pick_initial_player():
    if random.randint(0, 1) == 0:
        return 'computer'
    else:
        return 'player'

def play_game(player_symbol, computer_symbol):
    board = get_new_board()
    initiate_board(board)
    turn = 'player' #pick_initial_player()
    clear_screen()
    print('The ' + turn + ' will go first.')

    while True:
        player_valid_moves = get_valid_moves(board, player_symbol)
        computer_valid_moves = get_valid_moves(board, computer_symbol)

        if player_valid_moves == [] and computer_valid_moves == []:
            return board # No one can move, so end the game.

        elif turn == 'player': # Player's turn
            if player_valid_moves != []:
                draw_board(board)
                print_score(board, player_symbol, computer_symbol)

                players_turn(board, player_symbol)
            turn = 'computer'


def main():
    player_symbol, computer_symbol = boot_game()
    play_game(player_symbol, computer_symbol)

main()


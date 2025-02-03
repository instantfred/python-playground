import random
import sys

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

def drawBoard(board):
    print(f'{bcolors.HEADER}  12345678{bcolors.ENDC}')
    print(f'{bcolors.OKCYAN} +--------+{bcolors.ENDC}')
    for y in range(HEIGHT):
        print(f'%s{bcolors.OKCYAN}|{bcolors.ENDC}' % (y+1), end='')
        for x in range(WIDTH):
            print(board[x][y], end='')
        print(f'{bcolors.OKCYAN}|{bcolors.ENDC}%s' % (y+1))
    print(f'{bcolors.OKCYAN} +--------+{bcolors.ENDC}')
    print(f'{bcolors.HEADER}  12345678{bcolors.ENDC}')


def getNewBoard():
    board = []
    for i in range(WIDTH):
        board.append([' '] * WIDTH)
    return board

board = getNewBoard()
drawBoard(board)

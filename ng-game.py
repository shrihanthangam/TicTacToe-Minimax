# Non graphical terminal tic tac toe

import random
import math

board = {1: ' ', 2: ' ', 3: ' ', 4: ' ',
         5: ' ', 6: ' ', 7: ' ', 8: ' ', 9: ' '}
player_sym = 'X'
robot_sym = 'O'

"""
board layout:
1 2 3
4 5 6
7 8 9
"""


def print_board(board):
    for i in range(1, 4):
        print(board[i] + "|" if i < 3 else board[i], end="")
    print("\n-----")
    for i in range(4, 7):
        print(board[i] + "|" if i < 6 else board[i], end="")
    print("\n-----")
    for i in range(7, 10):
        print(board[i] + "|" if i < 9 else board[i], end="")
    print("\n")


def check_draw(board):
    for i in range(1, 10):
        if board[i] == ' ':
            return False
    return True


def available_squares(board):
    total = []
    for i in range(1, 10):
        if board[i] == ' ':
            total.append(i)
    return total


def square_empty(board, position):
    if board[position] == ' ':
        return True
    return False


def make_move(board, letter, position):
    if square_empty(board, position):
        board[position] = letter
        if check_draw(board):
            print_board(board)
            print("Draw")
            exit()
        if check_win(board):
            if letter == player_sym:
                print_board(board)
                print("You won!")
                exit()
            else:
                print_board(board)
                print("You lost :(")
                exit()


def check_win(board):
    # Horizontal
    if board[1] == board[2] and board[2] == board[3] and board[1] != ' ':
        return board[1]
    elif board[4] == board[5] and board[5] == board[6] and board[4] != ' ':
        return board[4]
    elif board[7] == board[8] and board[8] == board[9] and board[7] != ' ':
        return board[7]

    # Vertical
    if board[1] == board[4] and board[4] == board[7] and board[1] != ' ':
        return board[1]
    elif board[2] == board[5] and board[5] == board[8] and board[2] != ' ':
        return board[2]
    elif board[3] == board[6] and board[6] == board[9] and board[3] != ' ':
        return board[3]

    # Diagnol
    if board[1] == board[5] and board[5] == board[9] and board[1] != ' ':
        return board[1]
    elif board[3] == board[5] and board[5] == board[7] and board[3] != ' ':
        return board[3]

    return None


def dumb_comp_move(board):
    position = random.choice(available_squares(board))
    make_move(board, robot_sym, position)


def smart_computer_move(board):
    best_score = -math.inf
    best_move = 0

    for move in available_squares(board):
        board[move] = robot_sym
        score = minimax(board, False)
        board[move] = ' '
        if score > best_score:
            best_score = score
            best_move = move
    make_move(board, robot_sym, best_move)


def minimax(board, maximize):
    if check_win(board) == robot_sym:
        return 10 + len(available_squares(board))
    elif check_win(board) == player_sym:
        return -10 - len(available_squares(board))
    elif check_draw(board):
        return 0

    if maximize:
        bestScore = -math.inf
        for move in available_squares(board):
            board[move] = robot_sym
            score = minimax(board, False)
            board[move] = ' '

            if score > bestScore:
                bestScore = score
        return bestScore
    else:
        bestScore = math.inf
        for move in available_squares(board):
            board[move] = player_sym
            score = minimax(board, True)
            board[move] = ' '

            if score < bestScore:
                bestScore = score
        return bestScore


def player_move(board):
    position = int(input("What position do you want to play in: 1-9: "))
    while not square_empty(board, position):
        position = int(
            input("Invalid Position: What position do you want to play in: 1-9: "))
    make_move(board, player_sym, position)


while not check_win(board):
    print_board(board)
    player_move(board)
    print_board(board)
    # dumb_comp_move(board)
    smart_computer_move(board)

"""
Justin Luft
lab10.py
"""
def build_board():
    list = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    return list
def display_board(board):
    print(board[0], ' | ', board[1], ' | ', board[2], '\n')
    print('--------------')
    print(board[3], ' | ', board[4], ' | ', board[5], '\n')
    print('--------------')
    print(board[6], ' | ', board[7], ' | ', board[8], '\n')
def is_legal(board, num):
    if num > 9 or num < 1:
        return False
    elif 'O' == board[num - 1] or 'X' == board[num - 1]:
        return False
    else:
        return True
def game_won(board):
    if board[0] == 'O' and board[1] == 'O' and board[2] == 'O':
        print('Player 1 has won.')
        return True
    elif board[0] == 'O' and board[3] == 'O' and board[6] == 'O':
        print('Player 1 has won.')
        return True
    elif board[0] == 'O' and board[4] == 'O' and board[8] == 'O':
        print('Player 1 has won.')
        return True
    elif board[3] == 'O' and board[4] == 'O' and board[5] == 'O':
        print('Player 1 has won.')
        return True
    elif board[6] == 'O' and board[7] == 'O' and board[8] == 'O':
        print('Player 1 has won.')
        return True
    elif board[7] == 'O' and board[4] == 'O' and board[1] == 'O':
        print('Player 1 has won.')
        return True
    elif board[8] == 'O' and board[5] == 'O' and board[2] == 'O':
        print('Player 1 has won.')
        return True
    elif board[6] == 'O' and board[4] == 'O' and board[2] == 'O':
        print('Player 1 has won.')
        return True
    elif board[0] == 'O' and board[1] == 'O' and board[2] == 'O':
        print('Player 2 has won.')
        return True
    elif board[0] == 'X' and board[3] == 'X' and board[6] == 'X':
        print('Player 2 has won.')
        return True
    elif board[0] == 'X' and board[4] == 'X' and board[8] == 'X':
        print('Player 2 has won.')
        return True
    elif board[3] == 'X' and board[4] == 'X' and board[5] == 'X':
        print('Player 2 has won.')
        return True
    elif board[6] == 'X' and board[7] == 'X' and board[8] == 'X':
        print('Player 2 has won.')
        return True
    elif board[7] == 'X' and board[4] == 'X' and board[1] == 'X':
        print('Player 2 has won.')
        return True
    elif board[8] == 'X' and board[5] == 'X' and board[2] == 'X':
        print('Player 2 has won.')
        return True
    elif board[6] == 'X' and board[4] == 'X' and board[2] == 'X':
        print('Player 2 has won.')
        return True
    else:
        return False
def fill_spot(board, num, mark):
        board[num - 1] = mark
        return board
def game_over(board):
    acc = 0
    numbersacc = 0
    for i in board:
        numbersacc = numbersacc + 1
        if i != str(numbersacc):
            acc = acc + 1
    if game_won(board) == True:
        return True
    elif acc == 9:
        print("The game was a tie")
        return True
    else:
        return False



def play_game():
    board = build_board()
    display_board(board)
    i = -1
    while game_over(board):
        i = i + 1
        if i % 2 == 0:
            player = 'player1'
            mark = 'O'
        else:
            player = 'player2'
            mark = 'X'
        num = eval(input('Hello, ' + player + ' please type the position'))
        if is_legal(board, num):
            fill_spot(board, num, mark)
        display_board(board)
        if game_over(board):
            break
    print('---The game is over---')

    pass


play_game()


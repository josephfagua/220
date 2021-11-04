"""
Name: Joseph Fagua
lab10.py
"""


def buildBoard():
    return [1, 2, 3, 4, 5, 6, 7, 8, 9]


def displayBoard(board):
    print("{} | {} | {}".format(board[0], board[1], board[2]))
    print("{} | {} | {}".format(board[3], board[4], board[5]))
    print("{} | {} | {}".format(board[6], board[7], board[8]))


def isLegal(board, pos):
    if board[pos - 1] == "x" or board[pos - 1] == "o":
        return False
    else:
        return True


def fillSpot(board, pos, playerOneChar):
    if isLegal(board, pos):
        board[pos - 1] = playerOneChar
    else:
        return


def fillSpot2(board, pos, playerTwoChar):
    if isLegal(board, pos):
        board[pos - 1] = playerTwoChar
    else:
        return



def gameWon(board):
    if board[0] == "x" and board[1] == "x" and board[2] == "x":
        return True
    if board[0] == "o" and board[1] == "o" and board[2] == "o":
        return True
    elif board[3] == "x" and board[4] == "x" and board[5] == "x":
        return True
    elif board[3] == "o" and board[4] == "o" and board[5] == "o":
        return True
    elif board[6] == "x" and board[7] == "x" and board[8] == "x":
        return True
    elif board[6] == "o" and board[7] == "o" and board[8] == "o":
        return True
    elif board[0] == "x" and board[4] == "x" and board[8] == "x":
        return True
    elif board[0] == "o" and board[4] == "o" and board[8] == "o":
        return True
    elif board[0] == "x" and board[3] == "x" and board[6] == "x":
        return True
    elif board[0] == "o" and board[3] == "o" and board[6] == "o":
        return True
    elif board[1] == "x" and board[4] == "x" and board[7] == "x":
        return True
    elif board[1] == "o" and board[4] == "o" and board[7] == "o":
        return True
    elif board[2] == "x" and board[5] == "x" and board[8] == "x":
        return True
    elif board[2] == "o" and board[5] == "o" and board[8] == "o":
        return True
    elif board[2] == "x" and board[4] == "x" and board[6] == "x":
        return True
    elif board[2] == "o" and board[4] == "o" and board[6] == "o":
        return True
    else:
        return False


def gameOver(board):
    acc = 0
    for num in board:
        if num == "x" or num == "o":
            acc = acc + 1
    if gameWon(board):
        return True
    elif acc == 9:
        return True
    else:
        return False


def playGame():
    board = buildBoard()
    displayBoard(board)
    playerOneChar = "x"
    playerTwoChar = "o"
    while gameOver(board) == False:
        pos = eval(input("Player 1 make your move"))
        fillSpot(board, pos, playerOneChar)
        displayBoard(board)
        gameWon(board)
        gameOver(board)
        pos = eval(input("Player 2 make your move"))
        fillSpot2(board, pos, playerTwoChar)
        displayBoard(board)
        gameWon(board)
        gameOver(board)


def main():
    playGame()


main()

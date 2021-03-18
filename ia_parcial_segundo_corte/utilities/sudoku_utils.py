""" 
Juan José Montenegro Pulido
Camilo Andrés Romero Maldonado
 """
import numpy as np

""" Obtiene el valor del estado actual del sudoku """


def get_value(current_state):
    board = current_state.board
    return -np.sum(board == 0)


""" Determina si es o no un estado válido """


def validate_state(currentState):
    board = currentState.board
    boardT = board.T
    startSquareRow = 0
    startSquareColumn = 0
    for index in range(len(board)):
        row = board[index]
        column = boardT[index]
        square = board[startSquareRow:startSquareRow +
                       2, startSquareColumn:startSquareColumn + 3]
        startSquareRow += 2
        startSquareRow %= 6
        startSquareColumn += 3
        startSquareColumn %= 6
        for number in range(1, 7):
            if(np.sum(row == number) > 1 or np.sum(column == number) > 1 or np.sum(square == number) > 1):
                return False
    return True

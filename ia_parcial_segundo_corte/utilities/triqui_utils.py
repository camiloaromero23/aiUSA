""" 
Juan José Montenegro Pulido
Camilo Andrés Romero Maldonado
 """
from os import system

""" Diccionario de movimientos para hacer más simple la entrada de datos """
MOVES = {1: [0, 0], 2: [0, 1], 3: [0, 2],
         4: [1, 0], 5: [1, 1], 6: [1, 2],
         7: [2, 0], 8: [2, 1], 9: [2, 2], }
IA_TEXT = '\033[1m\033[91mIA Move\033[0m'
HUMAN_TEXT = '\033[1m\033[92mYour Turn\033[0m'

""" Limpia la consola """


def clean_console():
    system('clear')


""" Retorna un número entre 1 y 9 el cual es válido en el diccionario """


def get_movement():
    move = 0
    while move < 1 or move > 9:
        try:
            move = int(input('Insert move 1-9:\n'))
        except (KeyError, ValueError):
            # clean_console()
            print('Bad choice')
    return move


""" Realiza cambio a la matriz inicial debido al primer movimiento del humano en el tablero para evitar ejecuciones """


def first_move(initial_board, letter):
    print(HUMAN_TEXT)
    board = initial_board
    is_space_none = True
    while(is_space_none):
        is_space_none = False
        move = get_movement()
        row = MOVES[move][0]
        column = MOVES[move][1]
        if not board[row][column]:
            board[row][column] = letter
    return board

"""
Juan José Montenegro Pulido
Camilo Andrés Romero Maldonado

La gráfica de comparación se encuentra en el archivo triqui_graficas.png
 """
import numpy as np

from utilities.State import TicTacToeState as State
from utilities.triqui_utils import *

""" Retorna el valor del estado: 1 si gana la máquina, -1 si gana el humano o 0 si no hay ganador """


def get_value(current_state):
    global executions
    executions += 1
    BOARD = current_state.board
    ROWS = BOARD
    COLUMNS = BOARD.T
    DIAG = BOARD.diagonal()
    OP_DIAG = np.fliplr(BOARD).diagonal()

    for index in range(0, len(BOARD)):
        CURRENT_ROW = ROWS[index]
        CURRENT_COLUMN = COLUMNS[index]
        ROW_WIN = validate_winner(CURRENT_ROW)
        COLUMN_WIN = validate_winner(CURRENT_COLUMN)
        if ROW_WIN:
            return ROW_WIN
        if COLUMN_WIN:
            return COLUMN_WIN

    DIAG_WIN = validate_winner(DIAG)
    OP_DIAG_WIN = validate_winner(OP_DIAG)
    if DIAG_WIN:
        return DIAG_WIN
    if OP_DIAG_WIN:
        return OP_DIAG_WIN
    return 0


""" Recibe el caso de victoria y retorna 1 o -1 según si gana el humano o la máquina, si no se cumple alguna condición, no retorna (Python retorna None por defecto) """


def validate_winner(win_case):
    if((win_case == None).any() == False):
        letter = win_case[0]
        if((letter == win_case).all()):
            if(letter == machine_letter):
                return 1
            return -1


""" Genera los estados mínimos de cada posible tablero según el algoritmo de minimax """


def generate_min_states(current_state, letter, opponent_letter):
    value = get_value(current_state)
    # keep Searching
    if(value == 0 and (current_state.board == None).any()):
        children_values = []
        # generateStates
        board = current_state.board
        for row_index in range(0, len(board)):
            for column_index in range(0, len(board[0])):
                if(board[row_index][column_index] == None):
                    new_board = np.copy(board)
                    new_board[row_index][column_index] = letter
                    new_state = State(new_board)
                    current_state.addChild(new_state)
                    children_values.append(generate_max_states(
                        new_state,  opponent_letter, letter))

        value = min(children_values)
        current_state.value = value
        return value

    current_state.value = value
    return value


""" Genera los estados máximos de cada posible tablero según el algoritmo de minimax """


def generate_max_states(current_state, letter, opponent_letter):
    value = get_value(current_state)
    # keep Searching
    if(value == 0 and (current_state.board == None).any()):
        children_values = []
        # generateStates
        board = current_state.board
        for row_index in range(0, len(board)):
            for column_index in range(0, len(board[0])):
                if(board[row_index][column_index] == None):
                    new_board = np.copy(board)
                    new_board[row_index][column_index] = letter
                    new_state = State(new_board)
                    current_state.addChild(new_state)
                    children_values.append(generate_min_states(
                        new_state,  opponent_letter, letter))

        value = max(children_values)
        current_state.value = value
        return value

    current_state.value = value
    return value


""" Retorna un nuevo estado del tablero después de que el humano ingrese una posición válida en el tablero """


def user_move(current_state):
    print(HUMAN_TEXT)
    is_space_none = True

    while(is_space_none):
        move = get_movement()
        row = MOVES[move][0]
        column = MOVES[move][1]
        if(not current_state.board[row][column]):
            current_board = np.copy(current_state.board)
            current_board[row][column] = human_letter
            is_space_none = False
            newState = State(current_board)
            for state in current_state.children:
                if (state == newState):
                    current_state = state
                    break
        else:
            print('This Position Is Busy')
    return current_state


""" Definición inicial del tablero """
none_array = np.array([None, None, None])
initial_board = np.array([none_array, none_array, none_array])

""" Inicialización del tablero con opción de escoger letra y realización del primer movimiento """
machine_letter, human_letter = None, None
clean_console()
while (not human_letter or (human_letter != 'X' and human_letter != 'O')):
    human_letter = input('Choose your Letter (X or O)\n').upper()
    machine_letter = 'O' if human_letter == 'X' else 'X'
print(f'Human Letter:{human_letter}')
clean_console()
print(f'{initial_board}\n')
initial_board = first_move(initial_board, human_letter)

""" Creación del estado inicial """
initial_state = State(initial_board)
current_state = initial_state
executions = 0  # Variable que determina la cantidad de ejecuciones realizadas


ia_turn = True
print('Loading...')
# Este if se hace porque inicialmente se había realizado el ejercicio para
if(ia_turn):
    generate_max_states(current_state, machine_letter, human_letter)
else:
    generate_min_states(current_state, human_letter, machine_letter)
print(f'{current_state}\n')

""" Ejecución del algoritmo, se mantiene en el ciclo mientras se cumpla que no haya empate y que haya alguna posición vacía en el tablero"""
while (get_value(current_state) == 0 and (current_state.board == None).any()):
    if(ia_turn):
        # Asigna al estado actual el mejor estado hijo de la máquina según el estado que esté en ese momento
        current_state.children.sort(key=lambda x: x.value, reverse=True)
        current_state = current_state.children[0]
    else:
        # Asigna al estado actual el movimiento del humano
        current_state = user_move(current_state)
    clean_console()
    if ia_turn:
        print(IA_TEXT)
    print(f'{current_state}\n')
    ia_turn = not ia_turn  # Cambio de turno

""" Imprime el ganador o si es empate """
if(current_state.value == 1):
    print('\033[1m\033[91mIA WIN\033[0m')
elif(current_state.value == -1):
    print('\033[1m\033[92mYOU WIN\033[0m')
else:
    print('\033[1m\033[93mTIE\033[0m')

# Número de ejecuciones totales
print(f'\033[1m\033[94m{executions}\033[0m executions')

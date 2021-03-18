"""
Juan José Montenegro Pulido
Camilo Andrés Romero Maldonado

Gráfica en el archivo grafica_hill_climbing.jpeg

Conclusión:
Es posible observar la gran cantidad de iteraciones que son realizadas con el paso del tiempo, sin embargo, la variación stochastic logra resolver y encontrar el máximo con un número inferior respecto a las demás variaciones.

"""
import random

import matplotlib.pyplot as plt
import numpy as np

from utilities.State import SudokuState as State
from utilities.sudoku_utils import *

""" Genera los estados de first choice """


def generate_first_choice_states(current_state):
    global visited_states
    board = current_state.board
    new_states = []
    for rows in range(len(board)):
        for columns in range(len(board[0])):
            if(board[rows, columns] == 0):
                for number in range(1, 7):
                    new_board = np.copy(board)
                    new_board[rows, columns] = number
                    new_state = State(new_board)
                    if(new_state not in visited_states):
                        new_state.value = get_value(new_state)
                        if(new_state.value > current_state.value and validate_state(new_state)):
                            new_states.append(new_state)
                            return new_states

    return new_states


""" Genera los estados de random restart """


def generate_random_restart_states(current_state):
    global visited_states
    board = current_state.board
    new_states = []
    for rows in range(len(board)):
        for columns in range(len(board[0])):
            if(board[rows, columns] == 0):
                new_board = np.copy(board)
                new_board[rows, columns] = random.randint(1, 6)
                new_state = State(new_board)
                if(new_state not in visited_states):
                    new_state.value = get_value(new_state)
                    if(validate_state(new_state)):
                        new_states.append(new_state)

    return new_states


""" Genera los estados de steepest """


def generate_steepest_states(current_state):
    global visited_states
    board = current_state.board
    new_states = []
    for rows in range(len(board)):
        for columns in range(len(board[0])):
            if(board[rows, columns] == 0):
                new_board = np.copy(board)
                new_board[rows, columns] = random.randint(1, 6)
                new_state = State(new_board)
                if(new_state not in visited_states):
                    new_state.value = get_value(new_state)
                    if(validate_state(new_state)):
                        new_states.append(new_state)

    return new_states


""" Genera los estados de stochastic """


def generate_stochastic_states(current_state):
    global visited_states
    board = current_state.board
    new_states = []
    for rows in range(len(board)):
        for columns in range(len(board[0])):
            if(board[rows, columns] == 0):
                for number in range(1, 7):
                    new_board = np.copy(board)
                    new_board[rows, columns] = number
                    new_state = State(new_board)
                    if(new_state not in visited_states):
                        new_state.value = get_value(new_state)
                        if(validate_state(new_state)):
                            new_states.append(new_state)

    return new_states


""" Inicialización del tablero de sudoku """
board = np.array([[0, 0, 3, 0, 1, 0], [5, 6, 0, 3, 2, 0], [0, 5, 4, 2, 0, 3], [
                 2, 0, 6, 4, 5, 0], [0, 1, 2, 0, 4, 5], [0, 4, 0, 1, 0, 0]])
initialState = State(board)
print('Initial State:\n')
print(f'{initialState}\n\n')

# Ejecución de First Choice
first_choice_costs = []
visited_states = []
current_state = initialState
current_state.value = get_value(current_state)
first_choice_costs.append(current_state.value)
new_states = generate_first_choice_states(current_state)
while (len(new_states) > 0):
    visited_states.append(current_state)
    current_state = new_states[0]
    new_states = generate_first_choice_states(current_state)
    first_choice_costs.append(current_state.value)

print('First Choice\nBest Solution: \n')
print(current_state)
print(f'{current_state.value}\n\n')

# Ejecución de Random Restart
random_restart_costs = []
current_state = initialState
visited_states = []
solutions = []
repetitions = 100
for repetition in range(0, repetitions):
    current_state = initialState
    current_state.value = get_value(current_state)
    random_restart_costs.append(current_state.value)
    new_states = generate_random_restart_states(current_state)
    while (len(new_states) > 0):
        visited_states.append(current_state)
        new_states.sort(key=lambda x: x.value, reverse=True)
        best_state = new_states[0]
        if(best_state.value > current_state.value):
            current_state = new_states[0]
        new_states = generate_random_restart_states(current_state)
        random_restart_costs.append(current_state.value)
    solutions.append(current_state)

solutions.sort(key=lambda x: x.value, reverse=True)
current_state = solutions[0]
print('Random Restart\nBest Solution: \n')
print(current_state)
print(f'{current_state.value}\n\n')

# Ejecución de Steepest
steepest_costs = []
visited_states = []
current_state = initialState
current_state.value = get_value(current_state)
steepest_costs.append(current_state.value)
new_states = generate_steepest_states(current_state)
while (len(new_states) > 0):
    visited_states.append(current_state)
    new_states.sort(key=lambda x: x.value, reverse=True)
    best_state = new_states[0]
    if(best_state.value > current_state.value):
        current_state = new_states[0]
    new_states = generate_steepest_states(current_state)
    steepest_costs.append(current_state.value)

print('Stepest\nBest Solution: \n')
print(current_state)
print(f'{current_state.value}\n\n')

# Ejecución de Stochastic
stochastic_costs = []
current_state = initialState
current_state.value = get_value(current_state)
stochastic_costs.append(current_state.value)
new_states = generate_stochastic_states(current_state)
while (len(new_states) > 0):
    visited_states.append(current_state)
    selected_state = current_state
    while (selected_state.value <= current_state.value):
        index = random.randint(0, len(new_states) - 1)
        selected_state = new_states[index]
    current_state = selected_state
    new_states = generate_stochastic_states(current_state)
    stochastic_costs.append(current_state.value)

print('Stochastic\nBest Solution: \n')
print(current_state)
print(f'{current_state.value}\n\n')

""" Grafica todos los costos de cada versión """
plt.plot(first_choice_costs)
plt.plot(random_restart_costs)
plt.plot(steepest_costs)
plt.plot(stochastic_costs)
plt.xlabel('Iteration')
plt.ylabel('Cost')
plt.legend(['First Choice', 'Random Restart', 'Stepest', 'Stochastic'])
plt.show()

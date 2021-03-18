"""
Juan José Montenegro Pulido
Camilo Andrés Romero Maldonado

Gráfica en el archivo grafica_simulated_annealing.jpeg

Conclusión:
En el algoritmo de Simulated Annealing es importante tener en cuenta que, si se realiza con altas temperaturas y tasas de enfriamiento lentas, se garantiza que se encuentre el estado máximo global. Por ende el mejor es el quinto test, en el cual se requiere un menor tiempo para encontrar la respuesta óptima.
"""
import math
import random

import matplotlib.pyplot as plt
import numpy as np

from utilities.State import SudokuState as State
from utilities.sudoku_utils import *

""" Inicialización del tablero y creación de estado inicial """
BOARD = np.array([[0, 0, 3, 0, 1, 0], [5, 6, 0, 3, 2, 0], [0, 5, 4, 2, 0, 3], [
                 2, 0, 6, 4, 5, 0], [0, 1, 2, 0, 4, 5], [0, 4, 0, 1, 0, 0]])
INITIAL_STATE = State(BOARD)
print('Initial State:\n')
print(f'{INITIAL_STATE}\n\n')

""" Método para reducir la temperatura según el factor de decrecimiento """


def decrease_temperature(current_temperature, decreasing_factor):
    return current_temperature * decreasing_factor


""" Método para generar los estados de simulated annealing """


def generate_simulated_annealing_state(current_state, visited_states):
    global INITIAL_STATE
    initial_board = INITIAL_STATE.board
    current_board = current_state.board
    new_state = None
    while (new_state is None):
        random_row = random.randint(1, len(BOARD) - 1)
        random_column = random.randint(1, len(BOARD) - 1)
        if(initial_board[random_row, random_column] == 0):
            new_number = random.randint(0, 6)
            new_board = np.copy(current_board)
            new_board[random_row, random_column] = new_number
            new_state = State(new_board)
            if(validate_state(new_state) and new_state not in visited_states):
                new_state.value = get_value(new_state)
            else:
                new_state = None

    return new_state


""" Método de ejecución de simulated annealing """


def simulated_annealing(initial_temperature, decreasing_factor):
    visited_states = []
    current_temperature = initial_temperature
    current_state = INITIAL_STATE
    temperatures = [initial_temperature]
    current_state.value = get_value(current_state)
    execution = 1
    """ Se ejecuta mientras la temperatura sea mayor al valor mínimo de temperatura"""
    while (current_temperature > 0.01):
        execution += 1
        visited_states.append(current_state)
        new_state = generate_simulated_annealing_state(
            current_state, visited_states)
        if(new_state.value > current_state.value):
            current_state = new_state
        else:
            choose_rate = current_temperature/initial_temperature
            if (random.random() <= choose_rate):
                current_state = new_state
        current_temperature = decrease_temperature(
            current_temperature, decreasing_factor)
        temperatures.append(current_temperature)
    print('Simulated Annealing\nBest Solution:\n')
    print(current_state)
    print(current_state.value)
    temperatures = np.array(temperatures)
    plt.plot(range(0, execution), temperatures)


""" Ejecuciones de simulated annealing según diferentes temperaturas y diferentes factores de decrecimiento """
simulated_annealing(1000.00, 1 - random.random()*5/100)
simulated_annealing(1000.00, 1 - math.e ** 2)
simulated_annealing(1000.00, 0.8*random.random()+random.random())
simulated_annealing(100.00, 1 - random.random()*5/100)
simulated_annealing(100.00, 1 - math.e ** 2)
simulated_annealing(100.00, 0.8*random.random()+random.random())

""" Grafica el cambio de la temperatura sobre el tiempo de cada una de las ejecuciones """
plt.xlabel('Time')
plt.ylabel('Temperature')
plt.legend(['First test', 'Second test', 'Third test',
            'Fourth test', 'Fifth test', 'Sixth test'])
plt.show()

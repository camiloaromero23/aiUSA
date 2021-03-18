from utilities.utilities import getRoute, readFile
from algorithms.bfs import bfs
import sys
from collections import defaultdict
import copy


class Graph:
    inv_array = []

    def __init__(self, puzzle):
        self.puzzle = puzzle
        self.width, self.height = len(puzzle), len(puzzle)
        self.graph = defaultdict(set)
        self.objective_node = '1 2 3 \n8 0 4 \n7 6 5 '

    def init_graph(self):
        self.graph[self.puzzle_to_string(self.puzzle)]

    def puzzle_to_string(self, puzzle):
        string_puzzle = ''
        rowIndex = 0
        for row in puzzle:
            for value in row:
                string_puzzle += f'{str(value)} '
            rowIndex += 1
            if(rowIndex < self.width):
                string_puzzle += '\n'
        return string_puzzle

    def puzzle_to_matrix(self, string_puzzle):
        matrix_puzzle = []
        puzzle_rows = string_puzzle.split('\n')
        for row in puzzle_rows:
            row_str_values = row.strip().split(' ')
            row_values = []
            for value in row_str_values:
                row_values.append(int(value))
            matrix_puzzle.append(row_values)
        return(matrix_puzzle)

    def add_child(self, node, child):
        self.graph[node].add(child)

    def expand_node(self, current_node):
        puzzle_in_node = self.puzzle_to_matrix(current_node)
        #print(f'Puzzle in Node:{puzzle_in_node}')
        next_node = []
        for row in range(self.width):
            for column in range(self.height):
                if(puzzle_in_node[row][column] == 0):
                    if (column > 0):
                        next_node = copy.deepcopy(puzzle_in_node)
                        next_node[row][column] = next_node[row][column - 1]
                        next_node[row][column - 1] = 0
                        self.add_child(
                            current_node, self.puzzle_to_string(next_node))
                    if (column < self.width - 1):
                        next_node = copy.deepcopy(puzzle_in_node)
                        next_node[row][column] = next_node[row][column + 1]
                        next_node[row][column + 1] = 0
                        self.add_child(
                            current_node, self.puzzle_to_string(next_node))
                    if (row > 0):
                        next_node = copy.deepcopy(puzzle_in_node)
                        next_node[row][column] = next_node[row - 1][column]
                        next_node[row - 1][column] = 0
                        self.add_child(
                            current_node, self.puzzle_to_string(next_node))
                    if (row < self.height - 1):
                        next_node = copy.deepcopy(puzzle_in_node)
                        next_node[row][column] = next_node[row + 1][column]
                        next_node[row + 1][column] = 0
                        self.add_child(
                            current_node, self.puzzle_to_string(next_node))

    def get_inv_count(self):
        inv_count = 0
        for i in range(self.width):
            for j in range(i + 1, self.width):
                if (self.inv_array[i] > self.inv_array[j]):
                    inv_count += 1
        return inv_count

    def add_first_row(self):
        first_row = self.puzzle[0]
        for value in first_row:
            if(value != 0):
                self.inv_array.append(value)

    def add_last_column(self):
        for value in range(self.width):
            last_column_value = puzzle[value][self.width-1]
            if (not last_column_value in self.inv_array and last_column_value != 0):
                self.inv_array.append(last_column_value)

    def add_last_row(self):
        for value in range(self.width):
            last_row_value = puzzle[self.width-1][-value-1]
            if (not last_row_value in self.inv_array and last_row_value != 0):
                self.inv_array.append(last_row_value)

    def add_first_column(self):
        for value in range(self.width):
            first_column_value = puzzle[-value][0]
            if (not first_column_value in self.inv_array and first_column_value != 0):
                self.inv_array.append(first_column_value)

    def add_center_value(self):
        center_value = puzzle[self.width-2][self.width-2]
        if center_value != 0:
            self.inv_array.append(center_value)

    def get_inv_array(self):
        self.add_first_row()
        self.add_last_column()
        self.add_last_row()
        self.add_first_column()
        self.add_center_value()

    def is_solvable(self):
        self.get_inv_array()
        inv_count = self.get_inv_count()
        return (inv_count % 2 == 0)

    def bfs(self):
        self.init_graph()
        visited = []
        queue = []
        route = []
        aux_route = []
        current_node = list(self.graph)[0]
        visited.append(current_node)
        queue.append(current_node)
        route.append(current_node)
        aux_route.append([current_node, ''])

        self.expand_node(current_node)
        while queue:
            current_node = queue.pop(0)
            if current_node == self.objective_node:
                break
            for child_node in self.graph[current_node]:
                if not child_node in visited:
                    queue.append(child_node)
                    visited.append(child_node)
                    route.append(child_node)
                    aux_route.append([child_node, current_node])
                    self.expand_node(child_node)

        if(not self.objective_node in route):
            return None
        else:
            return getRoute(route, aux_route, self.objective_node)


puzzle = readFile('thirdExerciseFiles/test7.txt', False)
graph = Graph(puzzle)
if(graph.is_solvable()):
    route = graph.bfs()
    state_number = 1
    for movement in route:
        output = f'''State #{state_number}
{movement}
'''
        print(output)
        state_number += 1
else:
    print('Not Solvable puzzle')

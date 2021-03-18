from algorithms.dfs import dfs
from utilities.utilities import readFile
from utilities.Graph import Graph
import sys


def initializeMapping(labyrinth, height, width):

    mapping = []
    rowIndex = 0
    for row in range(width*height):
        mapping.append([])
        columnIndex = 0
        for column in range(height*width):
            mapping[rowIndex].append(0)
            columnIndex += 1
        rowIndex += 1
    rowIndex = 0

    return mapping


def labyrinthToMapping(labyrinth):
    height = len(labyrinth)
    width = len(labyrinth[0]) if height else 0
    mapping = initializeMapping(labyrinth, height, width)
    nodeIndex = 0
    rowIndex = 0
    for row in range(width):
        columnIndex = 0
        for column in range(height):
            if (row < width - 1 and labyrinth[rowIndex][columnIndex] != 1 and labyrinth[rowIndex + 1][columnIndex] != 1):
                mapping[nodeIndex][nodeIndex + width] = 1
                mapping[nodeIndex + width][nodeIndex] = 1
            if (column < height - 1 and labyrinth[rowIndex][columnIndex] != 1 and labyrinth[rowIndex][columnIndex + 1] != 1):
                mapping[nodeIndex][nodeIndex + 1] = 1
                mapping[nodeIndex + 1][nodeIndex] = 1

            nodeIndex += 1
            columnIndex += 1
        rowIndex += 1

    return mapping


def mappingToNames(labyrinth):
    nodeNames = []
    nodeNumber = 0
    rowIndex = 0
    for row in labyrinth:
        columnIndex = 0
        for column in row:
            nodeNames.append('{}'.format(nodeNumber))
            columnIndex += 1
            nodeNumber += 1
        rowIndex += 1
    return nodeNames


def getObjectiveNode(labyrinth):
    rowIndex = 0
    nodeName = 0
    for row in labyrinth:
        columnIndex = 0
        for column in row:
            if (labyrinth[rowIndex][columnIndex] == 2):
                return '{}'.format(nodeName)
            columnIndex += 1
            nodeName += 1
        rowIndex += 1
    return None


labyrinth = readFile('fourthExerciseFiles/')


initialPos = input(
    'Ingrese la posición inicial de la forma: 0 0 para (0,0)\n').strip().split(' ')

objectiveNode = getObjectiveNode(labyrinth)
mapping = labyrinthToMapping(labyrinth)
nodeNames = mappingToNames(labyrinth)
if(initialPos[0] == ''):
    initialPos = nodeNames[0]
else:
    x = int(initialPos[0])
    y = int(initialPos[1])
    try:
        if labyrinth[y][x] != 1:
            pos = y * len(labyrinth[0]) + x
        else:
            print(
                '\033[93m'+'Inicie de nuevo el programa con una posición inicial que no sea una pared en el laberinto'+'\033[0m')
            sys.exit()
    except:
        print(
            '\033[93m'+'Inicie de nuevo el programa con una posición inicial que esté dentro del laberinto'+'\033[0m')
        sys.exit()
    initialPos = nodeNames[pos]

graph = Graph()
graph.generateGraph(nodeNames, mapping)
route = dfs(graph, graph.nodes[initialPos], objectiveNode)
print(route)

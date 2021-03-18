from algorithms.bfs import bfs
from utilities.utilities import readFile
import sys


def getInvCount(invArray, n):
    inv_count = 0
    for i in range(n):
        for j in range(i + 1, n):
            if (invArray[i] > invArray[j]):
                inv_count += 1
    return inv_count


def addFirstRow(invArray, firstRow):
    for value in firstRow:
        if(value != 0):
            invArray.append(value)
    return invArray


def addLastColumn(invArray, puzzleLength):
    for value in range(puzzleLength):
        lastColumnValue = puzzle[value][puzzleLength-1]
        if (not lastColumnValue in invArray and lastColumnValue != 0):
            invArray.append(lastColumnValue)
    return invArray


def addLastRow(invArray, puzzleLength):
    for value in range(puzzleLength):
        lastRowValue = puzzle[puzzleLength-1][-value-1]
        if (not lastRowValue in invArray and lastRowValue != 0):
            invArray.append(lastRowValue)
    return invArray


def addFirstColumn(invArray, puzzleLength):
    for value in range(puzzleLength):
        firstColumnValue = puzzle[-value][0]
        if (not firstColumnValue in invArray and firstColumnValue != 0):
            invArray.append(firstColumnValue)
    return invArray


def addCenterValue(invArray, puzzleLength):
    centerValue = puzzle[puzzleLength-2][puzzleLength-2]
    if centerValue != 0:
        invArray.append(centerValue)
    return invArray


def getInvArray(puzzle):
    invArray = []
    puzzleLength = len(puzzle)
    invArray = addFirstRow(invArray, puzzle[0])
    invArray = addLastColumn(invArray, puzzleLength)
    invArray = addLastRow(invArray, puzzleLength)
    invArray = addFirstColumn(invArray, puzzleLength)
    invArray = addCenterValue(invArray, puzzleLength)
    return invArray


def isSolvable(puzzle):
    invArray = getInvArray(puzzle)
    invCount = getInvCount(invArray, len(invArray))
    return (invCount % 2 == 0)


def generateNodeNames(puzzle, objectiveNode):
    firstNode = str(puzzle)
    nodeNames = {firstNode}
    height, width = len(puzzle), len(puzzle)
    index = 0
    while(not objectiveNode in nodeNames):
        nextNode = [[], [], []]
        rowIndex = 0
        puzzleChanged = False
        for row in range(len(puzzle)):
            if(puzzleChanged):
                break
            columnIndex = 0
            for column in range(len(puzzle)):
                if(puzzleChanged):
                    break
                if (row < width - 1 and puzzle[rowIndex + 1][columnIndex] == 0 and (not str(puzzle[rowIndex][columnIndex] in nodeNames))):
                    print('Down')
                    nextNode = puzzle
                    nextNode[rowIndex +
                             1][columnIndex] = nextNode[rowIndex][columnIndex]
                    nextNode[rowIndex][columnIndex] = 0
                    puzzleChanged = True
                if (column < height - 1 and puzzle[rowIndex][columnIndex + 1] == 0 and (not str(puzzle[rowIndex][columnIndex] in nodeNames))):
                    print('Right')
                    nextNode = puzzle
                    nextNode[rowIndex][columnIndex +
                                       1] = nextNode[rowIndex][columnIndex]
                    nextNode[rowIndex][columnIndex] = 0
                    puzzleChanged = True
                if (row > 0 and puzzle[rowIndex - 1][columnIndex] == 0 and (not str(puzzle[rowIndex][columnIndex] in nodeNames))):
                    print('Up')
                    nextNode = puzzle
                    nextNode[rowIndex -
                             1][columnIndex] = nextNode[rowIndex][columnIndex]
                    nextNode[rowIndex][columnIndex] = 0
                    puzzleChanged = True
                if (column > 0 and puzzle[rowIndex][columnIndex - 1] == 0 and (not str(puzzle[rowIndex][columnIndex] in nodeNames))):
                    print('Left')
                    nextNode = puzzle
                    nextNode[rowIndex][columnIndex -
                                       1] = nextNode[rowIndex][columnIndex]
                    nextNode[rowIndex][columnIndex] = 0
                    puzzleChanged = True
                columnIndex += 1
            rowIndex += 1
            puzzle = nextNode
        nodeNames.add(str(nextNode))
        index += 1
        if(index > 20):
            break
    return nodeNames


puzzle = readFile('thirdExerciseFiles/test5.txt', False)
print(puzzle)
if(isSolvable(puzzle)):
    objectiveNode = '[[1, 2, 3], [8, 0, 4], [7, 6, 5]]'
    nodeNames = generateNodeNames(puzzle, objectiveNode)
    print('nodeNames', nodeNames)
    print('length', len(nodeNames))
    # bfs()
else:
    print('Not Solvable puzzle')

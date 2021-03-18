import sys


def readFile(directory, readFileName=True):
    fileName = directory
    if(readFileName):
        fileName += input(
            'Ingrese el nombre del archivo a leer\nEjemplo: nombreArchivo\n')
    inputFile = []
    try:
        with open(fileName, 'r') as f:
            for row in f:
                line = list(map(int, row.strip().split(' ')))
                inputFile.append(line)
    except FileNotFoundError:
        print(
            '\033[93m'+'Inicie de nuevo el programa con un archivo que exista'+'\033[0m')
        sys.exit()
    except:
        print(
            '\033[93m'+'Inicie de nuevo el programa con un archivo que tenga una entrada válida'+'\033[0m')
        sys.exit()
    return inputFile


def getRoute(route, auxRoute, objectiveNode):
    objectiveIndex = route.index(objectiveNode)
    objectiveRoute = [auxRoute[objectiveIndex][0]]
    while(not route[0] in objectiveRoute):
        fatherIndex = route.index(auxRoute[objectiveIndex][1])
        objectiveRoute[:0] = [route[fatherIndex]]
        objectiveIndex = fatherIndex
    return objectiveRoute

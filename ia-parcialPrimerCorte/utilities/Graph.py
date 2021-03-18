from collections import defaultdict
from .Node import Node


class Graph:
    nodes = defaultdict(list)

    def addNode(self, node, childNode):
        self.nodes[node].append(childNode)

    def generateGraph(self, nodeNames, graphMapping):
        nodes = []
        # Initialize tree nodes
        for nodeName in nodeNames:
            nodes.append(Node(name=nodeName).name)
        # Adds father to child nodes
        fatherIndex = 0
        for nodesArray in graphMapping:
            childIndex = 0
            for nodeMap in nodesArray:

                if (nodeMap == 1):
                    # print('nodosAntes', self.nodes)
                    self.addNode(nodes[fatherIndex], nodes[childIndex])
                    # print('nodosDespués', self.nodes)
                else:
                    # print('ultimo', nodes[fatherIndex])
                    self.nodes[nodes[fatherIndex]]
                childIndex += 1
            fatherIndex += 1
        # self.nodes = nodes

    def __str__(self):
        return str(self.nodes)

    def __repr__(self):
        return self.__str__()

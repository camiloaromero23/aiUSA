from utilities.utilities import getRoute


def bfs(graph, initialNode, objectiveNode):
    key_list = list(graph.nodes.keys())
    val_list = list(graph.nodes.values())
    visited = []
    queue = []
    route = []
    auxRoute = []
    currentNode = initialNode
    currentNodeKey = key_list[val_list.index(currentNode)]
    visited.append(currentNodeKey)
    queue.append(currentNodeKey)
    route.append(currentNodeKey)
    auxRoute.append([currentNodeKey, ''])
    while queue:
        currentNode = queue.pop(0)
        if currentNode == objectiveNode:
            break
        for childNode in graph.nodes[currentNode]:
            if not childNode in visited:
                queue.append(childNode)
                visited.append(childNode)
                route.append(childNode)
                auxRoute.append([childNode, currentNode])
    if(not objectiveNode in route):
        return None
    else:
        return getRoute(route, auxRoute, objectiveNode)

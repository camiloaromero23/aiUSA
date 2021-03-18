from utilities.utilities import getRoute


def dfs(graph, initialNode, objectiveNode):
    key_list = list(graph.nodes.keys())
    val_list = list(graph.nodes.values())
    visited = []
    stack = []
    route = []
    auxRoute = []
    currentNode = initialNode
    visited.append(key_list[val_list.index(currentNode)])
    stack.append(key_list[val_list.index(currentNode)])
    route.append(key_list[val_list.index(currentNode)])
    auxRoute.append([key_list[val_list.index(currentNode)], ''])

    while (stack):
        currentNode = stack.pop()
        if currentNode == objectiveNode:
            visited.append(currentNode)
            break
        if (not currentNode in visited):
            visited.append(currentNode)
        for node in reversed(graph.nodes[currentNode]):
            if (not node in visited):
                stack.append(node)
                route.append(node)
                auxRoute.append([node, currentNode])

    if(not objectiveNode in route):
        return None
    else:
        return getRoute(route, auxRoute, objectiveNode)

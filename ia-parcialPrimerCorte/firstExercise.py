from algorithms.bfs import bfs
from algorithms.dfs import dfs
from utilities.Graph import Graph
from utilities.Node import Node
from utilities.utilities import readFile


graph = Graph()

mapping = readFile('firstExerciseFiles/cannibalsAndMissionairesMap.txt', False)
nodeNames = ['CCCMMM_', 'CCCMM _M', 'CCMMM C', 'CCCM MM', 'CCMM_MC_', 'CMMM_CC_', 'CCMMM_C', 'CCMM_C_M', 'CCMM_M_C',
             'MMM_CC_C', 'CCMM_M_C', 'CMMM_C_C', 'CCM_MM_C', 'MMM_C_CC', 'MMC _M_CC', 'MMM_C_CC', 'MM_MC_CC', 'MC_MM_CC', 'CCM_M_CM',
             'CMM_C_CM', 'CM_CM_CM', 'CM_CC_MM', 'CCM_M_CM', 'CC_MM_CM', 'CMM_C_MC', 'CC_C_MMM', 'CC_M_CMM', 'CC_C_MMM', 'CC_CM_MM', 'C_CC_MMM',
             'C_MM_CCM', 'C_M_CCMM', 'C_C_CMMM', 'C_CC_MMM', '_CCCMMM']
graph.generateGraph(nodeNames, mapping)

route = bfs(graph, graph.nodes['CCCMMM_'], '_CCCMMM')
print(route)

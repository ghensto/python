from read_graph_file import *
#from MinHeap import *
import operator
from collections import OrderedDict

row, col, graph = matrix()
edge = []
vertex = []
weight = []
matrix = [[float('Inf') for i in range(row)] for j in range(col)]
p = {}
rank = {}
path = [[ float('Inf')  for i in range(row)] for j in range(col)]
Adj = [[]]*row

def Edge():
    for k in graph:
        vertex.append(k)
        for v in graph[k]:
            edge.append((k,v[0]))

def printMatrix():      
    for i in range(len(matrix)):
        for k in range(len(matrix[0])):
            print matrix[i][k],' ',
        print ''

            


Edge()
print graph

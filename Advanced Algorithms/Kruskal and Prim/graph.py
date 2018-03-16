from read_graph_file import *
from MinHeap import *
import operator
from collections import OrderedDict
from heapq import*
import copy

row, col, graph = matrix()
edge = []
vertex = []
weight = []
matrix = [[float('Inf') for i in range(row)] for j in range(col)]
p = {}
rank = {}
path = [[ float('Inf')  for i in range(row)] for j in range(col)]

def Edge():
    for k in graph:
        vertex.append(k)
        for v in graph[k]:
            edge.append((k,v[0]))

def Weight():
    for i in graph:
        u = int(i)
        for e in graph[i]:
            v = int(e[0])
            weight.append(((u,v),e[1]))

    for i in range(len(weight)):
        u = weight[i][0][0]
        v = weight[i][0][1]
        w = weight[i][1]
        matrix[u][v] = w
        path[u].append((w,u,v))
        path[v].append((w,v,u))

def printMatrix():
    for i in range(len(matrix)):
        for k in range(len(matrix[0])):
            print matrix[i][k],' ',
        print ''

def Adjlst():
    Adj = copy.deepcopy(matrix)
    
    for i in range(row):
        Adj[i] = filter(lambda a: a != 0, Adj[i])
    return Adj



Edge()
Weight()
Adj = Adjlst()

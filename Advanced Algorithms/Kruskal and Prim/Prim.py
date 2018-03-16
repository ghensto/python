# Module that reads the text file containing informations about the graph
from read_graph_file_prim import*
import operator
from MinHeap import *

row, col, graph = matrix()
result = [['0' for i in range(row)] for j in range(col)]

'''
 * Name:                Prim
 * Input arguments:     vertex where to start the spannning tree
 * Output arguments:    None
 * Function:            returns minimum spanning tree starting at vertex start
'''
def Prim(start):
    pred = []
    mst = {}
    pq = [(0,None,start)]
    
    for i in graph:
        mst[i] = []
        
    while pq:
        
        wt,u,v = pq.pop(0)
        if v in pred:
            continue

        pred.append(v)

        if u is not None and v is not None:
            mst[u].append((v,wt))
        
        for u,w in graph[v].items():
            min_insert(pq,(w,v,u))

    #Removes key with empty value from dictionary 
    MST = dict((k, v) for k, v in mst.iteritems() if v)
    return MST

def printResult():
    for k,v in tree.items():
        #print k, v
        if len(v) > 1:
            for i in range(len(v)):
                if int(k) < int(v[i][0]):
                    result[int(k)][int(v[i][0])] = v[i][1]
                    result[int(v[i][0])][int(k)] = v[i][1]
                else:
                    result[int(v[i][0])][int(k)] = v[i][1]
                    result[int(k)][int(v[i][0])] = v[i][1]
        else:
            result[int(k)][int(v[0][0])] = v[0][1]
            result[int(v[0][0])][int(k)] = v[0][1]
    
    for i in range(len(result)):
        for k in range(len(result[0])):
            print result[i][k],' ',
        print ''


print "Prim's Algorithm"

tree = Prim('0')
##print 'The adjacency-list of the spanning tree starting at vertex 0 is:'
##print tree,'\n'

print 'The adjacency-matrix of the spanning tree is:'
printResult()

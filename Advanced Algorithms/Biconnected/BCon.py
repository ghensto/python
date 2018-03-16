# Module that reads the text file containing informations about the 
# graph to be processed
from read_graph_file import *

# Gets informations about the graph from the text file
row, col, graph = matrix()
#print graph

##0 1 0 0 0 0 0 0 0 0
##1 0 1 1 0 0 0 0 0 0
##0 1 0 0 1 0 0 0 0 0
##0 1 0 0 1 0 0 0 0 0
##0 0 0 0 0 0 0 0 0 0
##0 0 0 1 0 0 1 1 0 0
##0 0 0 0 0 1 0 1 0 0
##0 0 0 0 0 1 1 0 1 1
##0 0 0 0 0 0 0 1 0 0
##0 0 0 0 0 0 0 1 0 0

##0 1 0 1 0 0
##1 0 1 0 1 0
##0 1 0 1 1 1
##1 0 1 0 0 0
##0 1 1 0 0 1
##0 0 1 0 1 0

edge = []
visited = [0]*row
parent = [0]*row
d = [0]*row
low = [0]*row
stack = []
count = 0
Bcom = []
articulation = []
bridge = []

'''
 * Name:                BCon
 * Input arguments:     None
 * Output arguments:    None
 * Function:            prints biconnected components, bridges and articulations
'''
def BCon():
    for u in graph.keys():
        visited[int(u)] = False
        
    for u in graph.keys():
        parent[int(u)] = None
        
    for u in graph.keys():
        
        if not visited[int(u)]:
            DFS_Visit(int(u))

    print "The biconnected components are: "
    print Bcom

    print "The bridges are: "
    print bridge

    print "The articulations points are: "
    print articulation

'''
 * Name:                DFS_Visit
 * Input arguments:     vertex
 * Output arguments:    None
 * Function:            computes biconnected components, bridges and articulations
'''
def DFS_Visit(u):
    visited[u] = True
    global count
    count += 1
    d[u] = count
    low[u] = d[u]
    children = 0
    
    for v in graph[str(u)]:
        
        if not visited[int(v)]:
            stack.append((u,int(v)))
            parent[int(v)] = u
            children += 1
            DFS_Visit(int(v))

            low[u] = min(low[u],low[int(v)])

            # Appends Bcon components
            if (parent[u] == None and children > 1)  or (parent[u] != None and low[int(v)] >= d[u]):
                while (u,v) not in Bcom and stack:
                    Bcom.append(stack.pop())
            
            # Appends articulations
            if parent[u] != None and low[int(v)] >= d[u] or (parent[u] == None and children > 1):
                if u not in articulation:
                    articulation.append(u)
            
            # Appends bridges
            if low[int(v)] > d[u] :    
                bridge.append((u,int(v)))
                    
              
        elif parent[u] is not int(v) and d[int(v)] < d[u]:
                low[u] = min(low[u],d[int(v)])
                stack.append((u,int(v)))

                
'''
 * Name:                Edge
 * Input arguments:     None
 * Output arguments:    None
 * Function:            returns list of egedes
'''

def Edge():
    for k in graph:
        for v in graph[k]:
            if (int(v),int(k)) not in edge and (int(k),int(v)) not in edge: 
                edge.append((int(k),int(v)))
            

Edge()
BCon()



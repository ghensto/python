# Module that contains graph, edges, vertices and adjacency-matrix
from graph import*

# Module that reads the text file containing informations about the 
# graph to be processed
from read_graph_file import*

# Gets informations about the graph from the text file
row, col, graph = matrix()

# Initializes the array for the MST
result = [['0' for i in range(row)] for j in range(col)]

'''
 * Name:                MAKE_SET
 * Input arguments:     node 'x'
 * Output arguments:    none
 * Function:            creates a singleton set, the single node in the  
 *                      corresponding tree; has an initial rank of 0
 '''
def MAKE_SET(x):
    p[x] = x
    rank[x] = 0


'''
 * Name:                UNION
 * Input arguments:     nodes 'x' and 'y'
 * Output arguments:    none
 * Function:            calls the function LINK and find to merge nodes x and y
 '''
def UNION(x,y):
    LINK(FIND_SET(x), FIND_SET(y))


'''
 * Name:                LINK
 * Input arguments:     nodes 'x' and 'y'
 * Output arguments:    none
 * Function:            Link nodes x and y by rank. Link root of smaller tree to
 *                      root of larger tree
 '''
def LINK(x,y):
    if rank[x] > rank[y]:
        p[y] = x

    else:
        p[x] = y
        if rank[x] == rank[y]:
            rank[y] = rank[y] + 1

'''
 * Name:                FIND_SET
 * Input arguments:     nodes 'x'
 * Output arguments:    none
 * Function:            returns the parent of a node x
 '''
def FIND_SET(x):
    if p[x] != x:
        p[x] = FIND_SET(p[x])
    return p[x]


'''
 * Name:                kruskal
 * Input arguments:     list of edges with their weight 
 * Output arguments:    None
 * Function:            returns minimum spanning tree
 '''
def kruskal(weight):

    # Creates new sets from each vertex
    for v in graph:
        MAKE_SET(v)
    
    # Initializes the minimum spannning tree list
    mst = []
    
    # Sorts the edges in nondecreasing order by weight  
    edges = sorted(weight, key=operator.itemgetter(1))
    
    # Removes edges with weight 0
    for i in range(len(edges) - 1, -1, -1):
        if edges[i][1] == 0:
            del edges[i]
    # 
    for e in range(len(edges)):
        weight, v1, v2 = edges[e][1], edges[e][0][0], edges[e][0][1]
        
        # Determines whether two vertices v1 and v2 belong to the same tree
        if FIND_SET(str(v1)) != FIND_SET(str(v2)):
        
            # Combine trees
            UNION(str(v1), str(v2))
            
            # Adds edges to minimum spannning tree
            mst.append(edges[e])
    return mst


'''
 * Name:                printResult
 * Input arguments:     None 
 * Output arguments:    print adjacency-matrix of minimum spanning tree
 * Function:            returns minimum spanning tree
 '''
def printResult():
    
    # Populates the adjacency-matrix of the MST 
    for (u,v), w in sorted(MST):
        result[u][v] = w
        result[v][u] = w
    
    # Displays the adjacency-matrix of the MST
    for i in range(len(result)):
        for k in range(len(result[0])):
            print result[i][k],' ',
        print ''

MST = kruskal(weight)

for (u,v),w in MST:
    if u > v:
        x,y,z = v,u,w
        MST.remove(((u,v),w))
        MST.append(((x,y),z))

print "Kruskal's Algorithm\n"

##print 'The edges that build the spanning tree are:'
##print MST,'\n'


print 'The adjacency-matrix of the spanning tree is:'
printResult()

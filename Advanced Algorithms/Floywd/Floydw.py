from graph import*

print "Floyd-Warshall Algorithm"

'''
 * Name:                Floyd
 * Input arguments:     None
 * Output arguments:    None
 * Function:            returns adjacency matrix
 '''
def Floyd():
    for k in range(len(matrix)):
        for i in range(len(matrix)):
            for j in range(len(matrix)):
                matrix[i][j] = min(matrix[i][j] , (matrix[i][k]+ matrix[k][j]))
        printMatrix()
        print '\n', '\n'

Floyd()

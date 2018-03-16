
def matrix():
    
    with open("graph_file.txt") as f:
        rows = f.readline().lstrip("rows = ")
        cols = f.readline().lstrip("cols = ")

    rows = int(rows)
    cols = int(cols)
    #print rows
    #print cols

    m = []
    with open("graph_file.txt") as f:
        for line in f:
            if line.startswith(('INF', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9')):
                m.append(line.strip().split())

    for i in range(len(m)):
        for j in range(len(m[i])):
            if m[i][j] != 'INF':
                m[i][j] = int(m[i][j])


    graph = {}
    temp = []

    for i in range(rows):
        for j in range (cols):
            if m[i][j] != 'INF':
                temp.append([str(j), m[i][j]])

        graph[str(i)] = temp
        temp = []

    #print(graph)
    return rows, cols, graph

##matrix()

def createAdj(n,m):
    adjList=[[] for i in range(n)]
    for _ in range(m):
        u,v=input(),input()
        adjList[u].append(v)
        adjList[v].append(u)

def printAdj(adjList):
    # U parent vertice V adjacent Vertices
    for u,v in enumerate(adjList):
        print(u,v)
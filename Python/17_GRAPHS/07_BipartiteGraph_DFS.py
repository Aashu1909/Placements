def dfsCheck(adj,sourceNode,color):
    if color[sourceNode]==-1:
        color[sourceNode]=1

    for adjNode in adj[sourceNode]:
        if color[adjNode]==-1:
            color[adjNode]=1-color[sourceNode]
            #now recursive call for depth traversal
            if dfsCheck(adj,adjNode,color)==False:
                return False
        else:
            # Its already Coloured
            if color[sourceNode]==color[adjNode]:
                return False
    return True


def checkBipartite(adj,V):
    color=[-1]*V
    for i in range(V):
        if color[i]==-1:
            if dfsCheck(adj,i,color)==False:
                return False
    return True
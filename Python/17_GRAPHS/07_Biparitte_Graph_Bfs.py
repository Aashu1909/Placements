# Bipartite Graph-Its defined as graph that can be coloured using two colors
# such that no two adjacent node have the same color
# if a graph has a odd lenght cycle its not a bipartite graph
# Basically checking a graph is bipartite is similar to the check a cycle using bfs
# with som extra check such that checking the color of the parent node and the adj node must not be same 
# for the given node
# we are taking Two colors as 0,1
from collections import deque
def bfsCheck(adj,sourceNode,color):
    queue=deque()
    queue.append(sourceNode)
    color[sourceNode]=1
    while len(queue)>0:
        node=queue.popleft()
        for adjNode in adj[node]:
            # if its not colored
            if color[adjNode]==-1:
                color[adjNode]=1-color[node]
                queue.append(adjNode)
            else:
                #the node is already being colored before and has the same color as the parent
                if color[adjNode]==color[node]:
                    return False
    return True

def checkBipartite(adj,V):
    color=[-1]*V
    for i in range(V):
        if color[i]==-1:
            if bfsCheck(adj,i,color)==False:
                return False
    return True


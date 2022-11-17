# Topological sort means the linear ordering of the vertices of a given graph
# in such way u->v that u will always come before v.
# it can be only done for DAG(Directed Acyclic Graphs) 
def findtopoSort(adj,sourceNode,visited,stack):
    visited[sourceNode]=True
    for adjNode in adj[sourceNode]:
        if visited[adjNode]==False:
            findtopoSort(adj,adjNode,visited,stack)
    stack.append(sourceNode)

def topoSort(adj,V):
    visited=[False]*V
    stack=[]
    for i in range(V):
        if visited[i]==False:
            findtopoSort(adj,i,visited,stack)
    topoSort=[]
    while stack:
        topoSort.append(stack.pop())
    return topoSort
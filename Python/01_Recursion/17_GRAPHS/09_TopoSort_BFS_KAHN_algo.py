# TOPOLOGICAL Sort Using BFS 
# Its a sliglty tweaked version of thr regular BFS algo 
# Since Topological sort is possible only on DAG 

# Basically in the end we want to be in linear ordereing ie is u->v then u should come before v
# the topo order

import collections
def topoSort(V, adj):
    # Code here
    # Here we use the concept of indegree
    indegree=[0]*V
    for i in range(V):
        for node in adj[i]:
            indegree[node]+=1

    queue=collections.deque()
    for i in range(V):
        if indegree[i]==0:
            queue.append(i)
    topo=[]
    while len(queue)!=0:
        node=queue.popleft()
        topo.append(node)
        for adjNode in adj[node]:
            indegree[adjNode]-=1
            if indegree[adjNode]==0:
                queue.append(adjNode)

    return topo

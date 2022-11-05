import collections
# Here to detect a cycle using BFS using Kahn algorithm
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
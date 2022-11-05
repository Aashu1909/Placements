def indegree(adj):
    v=len(adj)
    indegree=[0]*v
    for adjNode in adj:
        indegree[adjNode]+=1
    
    return indegree



def checkForCycle(source,parent,visited,adj):
    visited[source]=True
    for adjNode in adj[source]:
        if visited[adjNode]==False:
            if checkForCycle(adjNode,source,visited,adj):
                return True
        else:
            # is the node has been previosly visited 
            if adjNode!=parent:
                return True
    # if the dfs call never return a true that means it dosent have a cycle
    return False

def isCycleDfs(adj,V):
    visited=[False]*V
    for i in range(V):
        if visited[i]==False and checkForCycle(source=i,parent=-1,visited=visited,adj=adj):
            return True
    return False
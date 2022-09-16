# Basically when compared to Undirected Traversal its a bit different'
# Here we maintain two Visited arrays
# One normal visited and one dfs visited to maintain the direction of the traversal

def check_cycle_dfs(adj,sourceNode,visited,dfs_visited):
    visited[sourceNode]=True
    dfs_visited[sourceNode]=True
    for adjNode in adj[sourceNode]:
        if visited[adjNode]==False:
            if check_cycle_dfs(adj,adjNode,visited,dfs_visited):
                return True
        else:
            # return True if the element is Visited in both visited and dfs_visited
            if dfs_visited[adjNode]:
                return True
    #there are no adjNode left to be visited we change dfs_visited[sourceNdoe] back to False
    # and return False 
    dfs_visited[sourceNode]=False
    return False
    


def isCyclicDirectedGraph(adj,V):
    visited=[False]*V
    dfs_visited=[False]*V
    for i in range(V):
        if visited[i]==False:
            if check_cycle_dfs(adj,i,visited,dfs_visited):
                return True
    return False


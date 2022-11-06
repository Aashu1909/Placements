def dfs_recursive(adjlist,souce,visited,dfs):
    visited[souce]=True
    dfs.append(adjlist[souce])
    for u in adjlist[souce]:
        if visited[u]==False:
            dfs_recursive(adjlist,u,visited,dfs)

def dfs_graph(adjlist,vertices,source):
    visited=[False]*vertices
    dfs=[]
    dfs_recursive(adjlist,source,visited,dfs)
    
#Conected component of graph using dfs 
#Disconnected graph

def dfs_recursive_d(adjlist,souce,visited,dfs):
    visited[souce]=True
    dfs.append(adjlist[souce])
    for u in adjlist[souce]:
        if visited[u]==False:
            dfs_recursive(adjlist,u,visited,dfs)

def dfs_graph_disconnected(adjlist,vertices):
    visited=[False]*vertices
    dfs=[]
    count=0
    for u in range(vertices):
        if visited[u]==False:
            dfs_recursive_d(adjlist,u,visited,dfs)
            count+=1
    return count

    
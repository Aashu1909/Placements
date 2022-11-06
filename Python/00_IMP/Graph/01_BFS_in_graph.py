# Here adjacency Matrix represent the nested list where each 
# element in the nested list contain its adjacent Element
from collections import deque
# adjacency list,v:no of vertices, source:starting Point

def bfs_graph(adjList,v,source):
    visited_arr=[False]*(v)
    queue=deque()
    visited_arr[source]=True
    queue.append(source)
    bfs=[]
    while len(queue)>0:
        u=queue.popleft()
        bfs.append(u)
        for vertices in adjList[u]:
            if visited_arr[vertices]==False:
                visited_arr[vertices]=True
                queue.append(vertices)
    
    return bfs

# Also when we have to find the number of connected graph component 
# Also Called as a number of island in the graph
# There may given a graph with no souce or Disconnected graph

def bfs(adjList,source,visited, bfs):
    queue=deque()
    visited[source]=True
    queue.append(source)
    while len(queue)!=0:
        node=queue.popleft()
        for adj in adjList[node]:
            if visited[adj]==False:
                queue.append(adj)
                visited[adj]=False
    
def bsf_disconnected(adjList,v):
    visited=[False]*v
    count=0
    bfs=[]
    for i in range(0,v):
        if visited[i]==False:
            bfs(adjList,source=i,visited=visited,bfs=bfs)
            count+=1
    return count
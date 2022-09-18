# basically the question is to find the minumum number of edges,
# required from the source to travel to all the vertices in th e graph
from collections import deque
INF=10**20
def shortest_path(adjList,source):
    distance=[INF]*len(adjList)
    visited=[False]*len(adjList)
    queue=deque()
    distance[source]=0
    queue.append(source)
    visited[source]=True
    while len(queue)>0:
        u=queue.popleft()
        for adj in adjList[u]:
            if visited[adj]==False:
                distance[adj]=distance[u]+1
                visited[adj]=True
                queue.append(adj)
    return distance
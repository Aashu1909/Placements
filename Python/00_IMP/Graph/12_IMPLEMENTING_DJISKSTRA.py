# Shortest distance from a souce to destination using Dijkastra algorithm
# Source should be zero and we have a weighted graph 
import heapq
# Here we are using a priority queue which has to be a minimum heap
# in the priority queue we will be storing [node, dist]

def dijkstra(V, adj, src):
    #code here
    MAX=10**20
    distance=[MAX for _ in range(V)]
    distance[src]=0
    heap=[]
    heap.append(src)
    while heap:
        node=heapq.heappop(heap)
        for adjNode,wt in adj[node]:
            if distance[node]+wt<distance[adjNode]:
                distance[adjNode]=distance[node]+wt
                heapq.heappush(heap,adjNode)
    return distance
    
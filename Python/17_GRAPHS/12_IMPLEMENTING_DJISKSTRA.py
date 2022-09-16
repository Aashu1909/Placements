# Shortest distance from a souce to destination using Dijkastra algorithm
# Source should be zero and we have a weighted graph 
import heapq

# Here we are using a priority queue which has to be a minimum heap
# in the priority queue we will be storing [node, dist]

def dijkstra(V, adj, src):
    #code here
    MAX=10**20
    heap=[]
    heap.append([src,0])
    distance=[MAX]*V
    distance[src]=0
    while heap:
        node=heapq.heappop(heap)
        for adjNode,dist in adj[node[0]]:
            if distance[node[0]]+dist <distance[adjNode]:
                distance[adjNode]=distance[node[0]]+dist
                heapq.heappush(heap,([adjNode,distance[adjNode]]))
    return distance
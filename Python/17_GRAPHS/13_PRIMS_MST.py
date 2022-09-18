# O(N^2) time and space is O[n]
def prims_mst(adj,V):
    key=[10**20 for _ in range(V)]
    parent=[-1 for _ in range(V)]
    mstSet=[False for _ in range(V)]
    # Key[0]=0
    key[0]=0
    parent[0]=-1
    #Traversing for n-1 edges
    for count in range(V-1):
        #Finding the minimum edge amoung the keys and storing its index
        mini=10**20
        node=0
        for v in range(V):
            if mstSet[v]==False and key[v]<mini:
                mini=key[v]    
                node=v
        # Now taking node to be a part MST
        mstSet[node]=True
        # now finding the minimum adjacent of the node
        for adjNode in adj[node]:
            vertice,wt=adjNode[0],adjNode[1]
            # If its not the part of the tree and wt is less then key[vertice]
            if(mstSet[vertice]==False and wt<key[vertice]):
                parent[vertice]=node 
                key[vertice]=wt
    ans=0
    for w in key:
        ans+=w
        
    return ans
    # return parent

import heapq
def spanningTree(self, V, adj):
    #code here
    key=[10**20 for _ in range(V)]
    parent=[-1 for _ in range(V)]
    mstSet=[False for _ in range(V)]
    # Key[0]=0
    key[0]=0
    parent[0]=-1
    heap=[]
    heapq.heappush(heap,[0,0])
    #Traversing for n-1 edges
    for count in range(V-1):
        #Finding the minimum edge amoung the keys and storing its index
        node=heapq.heappop(heap)[1]
        # Now taking node to be a part MST
        mstSet[node]=True
        # now finding the minimum adjacent of the node
        for adjNode in adj[node]:
            vertice,wt=adjNode[0],adjNode[1]
            # If its not the part of the tree and wt is less then key[vertice]
            if(mstSet[vertice]==False and wt<key[vertice]):
                parent[vertice]=node 
                key[vertice]=wt
                heapq.heappush(heap,[key[vertice],vertice])
    ans=0
    for w in key:
        ans+=w
    
        return ans
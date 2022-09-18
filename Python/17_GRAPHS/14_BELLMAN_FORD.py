# def bellman_ford(adj,V):
def isNegativeWeightCycle(self, v, adj):
    #Code here
    dist=[100000000]*v
    dist[0]=0
    
    for i in range(1,v):
        for j in adj:
            u=j[0]
            v=j[1]
            cost=j[2]
            if(dist[u]+cost<dist[v]):
                dist[v]=dist[u]+cost
    count=0
    for j in adj:
        u=j[0]
        v=j[1]
        cost=j[2]
        if(dist[u]+cost<dist[v]):
            dist[v]=dist[u]+cost
            count+=1
# if it has -ve cycle then relaxation will take place.. hence count will be set to not 0
    if(count!=0):  
        return 1
    else:
        return 0
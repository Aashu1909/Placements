class Pair():
    def __init__(self,first,second):
        self.first=first
        self.second=second

def findtopoSort(adj,sourceNode,visited,stack):
    visited[sourceNode]=True
    for adjNode in adj[sourceNode]:
        if visited[adjNode.first]==False:
            findtopoSort(adj,adjNode,visited,stack)
    stack.append(sourceNode)

def shortestPath(start,adj,V):
    visited=[False]*V
    stack=[]
    for i in range(V):
        if visited[i]==False:
            findtopoSort(adj,i,visited,stack)
    
    distance=[10**20 for _ in range(V)]
    # Src = 0
    distance[start]=0
    while len(stack)!=0:
        node=stack.pop()
        if distance[node]!=10**20:
            for adjNode in adj[node]:
                if distance[node]+adjNode.second<distance[adjNode.first]:
                    distance[adjNode.first]=distance[node]+adjNode.second
    for i in range(V):
        print(distance[i] if distance[i]!=10**20 else "INF")

if __name__=="__main__":
    n,m=map(int,input().split())
    adj=[Pair(-1,-1) for _ in range(n)]
    for i in range(m):
        node,vertice,wt=map(int,input().split())
        adj[node].first=vertice
        adj[node].second=wt
    # adj=[(0, 4, 1), (1, 2, 3), (2, 3, 6), (3, -1, -1), (4, 5, 4), (5, 3, 1)]
    print([(i,adj[i].first,adj[i].second) for i in range(n)])
    shortestPath(0,adj,n)

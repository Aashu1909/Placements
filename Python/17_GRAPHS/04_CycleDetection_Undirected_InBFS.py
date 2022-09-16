from collections import deque

def checkForCycle(self,source,adj,visited):
    queue=deque()
    visited[source]=True
                    # parent
    queue.append([source,-1])
    
    while len(queue)>0:
        node,parent=queue.popleft()
        for adjNode in adj[node]:
            if visited[adjNode]==False:
                visited[adjNode]=True
                queue.append((adjNode,node))
            elif parent!=node:
                return True
    return False


def isCycle(self, V, adj):
    #Code here
    visited=[False]*V
    for i in range(V):
        if visited[i]==False:
            if self.checkForCycle(i,V,adj,visited):
                return True
    return False
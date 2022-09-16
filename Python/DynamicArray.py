def dynamicArray(n, queries):
    # Write your code here
    arr=[[] for _ in range(n)]
    lastAns=0    
    lenQueries=len(queries)
    for i in range(lenQueries):
        query=[int(x) for x in queries[i]]
        x,y=query[1],query[2]
        if query[0]==1:
            arr[(x^lastAns)%n].append(y)
        elif query[0]==2:
            idx=(x^lastAns)%n
            lastAns=arr[idx][y%len(arr[idx])]
            print(lastAns)

def dynamicArr2(n,q):
    l = [[] for _ in range(n)]
    latsans = 0
    for i in range(len(q)):
        query=[int(x) for x in q[i]]
        a,x,y=query[0],query[1],query[2]
        if a == 1:
            l[(x^latsans)%n].append(y)
        else:
            t = (x^latsans)%n
            latsans = l[t][y%len(l[t])]
            print(latsans)
        #print(a, x, y, l)
                       

query=[[1,0,5],[1,1,7],[1,0,3],[2,1,0],[2,1,1]]
dynamicArray(2,query)
dynamicArr2(2,query)


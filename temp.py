import heapq
def c(arr,k):
    n=len(arr)
    heap=[]
    ans=[]
    for i in range(k):
        heapq.heappush(heap,(-arr[i],i))

    ans.append(-heap[0][0])
    print(heap)
    for i in range(k,n):
        heapq.heappush(heap,(-arr[i],i))
        # # print(heap[0][1],(i-k))
        while len(heap)!=0 and heap[0][1]<=(i-k):
            print(-heap[0][1],(i-k))
            print("pop",heapq.heappop(heap))
        ans.append(-heap[0][0])
        
    return ans

arr=[7,11,3,9,-3,10,5,6,7]
k = 3
print(c(arr,k))
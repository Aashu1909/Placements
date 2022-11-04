import time
begin=time.time()
from collections import deque
def printFirstNegativeInteger(arr,n,k):
    # code here
    queue=deque()
    # first we add all negative element in window size k-1
    for i in range(k-1):
        if arr[i]<0:
            queue.append(arr[i])
    ans=[]
    for i in range(k-1,n):
        if arr[i]<0:
            queue.append(arr[i])

        if len(queue)!=0:
            ans.append(queue[0])
            if queue[0]==arr[i-k+1]:
                queue.popleft()
        else:
            ans.append(0)
    
    return ans

def solve2(arr,n,k):
    q=deque()
    

test_case=[0]
print(printFirstNegativeInteger(test_case))




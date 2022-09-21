from collections import Counter
def relativeSort (arr, N, A2, M):
    # Your Code Here
    hashmap=dict(Counter(arr) )
    ans=[]
    for i in range(M):
        if A2[i] in hashmap:
            for _ in range(hashmap[A2[i]]):
                ans.append(A2[i])
            hashmap.pop(A2[i])
    rem=[]  
    for key,value in hashmap.items():
        for i in range(value):
            rem.append(key)
    rem.sort()
    ans.extend(rem)
    return ans
A1 = [2, 1, 2, 5, 7, 1, 9, 3, 6, 8, 8]
A2 = [2, 1, 8, 3]
print(relativeSort(A1,len(A1),A2,len(A2)))
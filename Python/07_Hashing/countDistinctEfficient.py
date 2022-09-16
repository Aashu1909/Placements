import time
begin=time.time()

# Ques
# test_case
# O/p

def countDistinctElementK(arr,k):
    hashmap={}
    n=len(arr)
    for i in range(k):
        hashmap[arr[i]]=hashmap.get(arr[i],0)+1
    print(hashmap)
    for i in range(k,n):
        if hashmap[arr[i-k]]==1:
            hashmap.pop(arr[i-k])
        else:
            hashmap[arr[i-k]]-=1
        hashmap[arr[i]]=hashmap.get(arr[i],0)+1
        print(len(hashmap))

test_case=[1,2,2,1,3,1,1,3]
countDistinctElementK(test_case,4)

time.sleep(1)
end=time.time()
print(f"Total Time Taken:{end-begin}")
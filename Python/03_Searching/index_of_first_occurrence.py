import time
begin=time.time()
# Ques index of first occurence
# test_case=[5,10,10,20,20]
# O/p 1
def indexOfFirstOccurence(arr,element):
    low=0
    high=len(arr)-1
    while (low<=high):
        mid=(high+low)//2
        if arr[mid]>element:
            high=mid-1
        elif arr[mid]<element:
            low=mid+1
        else:
            if (mid==0) or (arr[mid-1]!=arr[mid]):
                return mid
            else:
                high=mid-1
    return -1

test_case=[5,7,7,8,8,10]
print(indexOfFirstOccurence(test_case,8))











time.sleep(1)
end=time.time()
print(f"Total Time Taken:{end-begin}")
import time
begin=time.time()
# Ques Index of last occurence of a number
# test_case=[5,10,10,10,20,20]
# O/p 3
def indexOfLastOccurence(arr,element):
    low=0
    high=len(arr)-1
    while (low<=high):
        mid=(low+high)//2
        if (arr[mid]>element):
            high=mid-1
        elif(arr[mid]<element):
            low=mid+1
        else:
            if (mid==(len(arr)-1)) or (arr[mid]!=arr[mid+1]):
                return mid
            else:
                low=mid+1
    return -1

test_case=[5,10,10,10,20,20] #len=6
print(indexOfLastOccurence(test_case,element=20))











time.sleep(1)
end=time.time()
print(f"Total Time Taken:{end-begin}")
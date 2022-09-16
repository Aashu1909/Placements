import time
begin=time.time()
# Ques Implement Binary search (search when the array is sorted)   
# test_case=[10,20,30,45,50,60,97] ele=97
# O/p: 7
def Iterative_binary_search(arr,ele):
    low=0
    high=len(arr)-1
    while low<=high:
        mid=(low+high)//2
        if arr[mid]==ele:
            return mid
        elif arr[mid]>ele :
            high=mid-1
        else:
            low=mid+1
    return -1

def recursive_binary_search(arr,low,high,ele):
    if low>high:    #base condition
        return -1
    
    mid=(low+high)//2
    if arr[mid]==ele:
        return mid
    elif arr[mid]>ele:
        return recursive_binary_search(arr,low,mid-1,ele)
    else:
        return recursive_binary_search(arr,mid+1,high,ele)

test_case=[10,20,30,45,50,60,97]
print(Iterative_binary_search(test_case,55))
test_case=[10,20,30,45,50,60,97]
low=0
high=len(test_case)-1
print(recursive_binary_search(test_case,low,high,55))











time.sleep(1)
end=time.time()
print(f"Total Time Taken:{end-begin}")
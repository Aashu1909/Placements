import time
begin=time.time()

# test_case=[11,12,15,18,2,5,6,8]
# O/p true 4

# Here MID represent minimum element in the sorted arr
# And index of the minimum element represents the number of times this array has been rotated
def numberOfTimesSortedArrIsrotated(arr):
    n=len(arr)
    print(arr)
    res=arr[0]
    start=0
    end=n-1
    while start<=end:
        if arr[start]<=arr[end]:
            return arr[start]

        mid=start+(end-start)//2
        nextt=(mid+1)%n
        prev=(mid+n-1)%n    
        if arr[mid]<=arr[prev] and arr[mid]<=arr[nextt]:
            return arr[mid]
        elif  arr[start]<=arr[mid]:
            start=mid+1
        elif arr[mid]>=arr[end]:
            end=mid-1
    print(0)
    return res

test_case=[15, 18, 2, 3, 6, 12]
print(numberOfTimesSortedArrIsrotated(test_case))











time.sleep(1)
end=time.time()
print(f"Total Time Taken:{end-begin}")
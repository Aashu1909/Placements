import time
begin=time.time()
# Ques implementation of merge sort
# Its a divide and conquer algorithm

def Merge(arr,low,mid,high):
    left=arr[low:mid+1]
    right=arr[mid+1:high+1]
    k=low
    i=j=0
    while (i<len(left)) and (j<len(right)):
        if left[i]<right[j]:
            arr[k]=left[i]
            k+=1
            i+=1
        else:
            arr[k]=right[j]
            j=j+1
            k=k+1
            
    while (i<len(left)):
        arr[k]=left[i]
        k=k+1
        i=i+1
    while (j<len(right)):
        arr[k]=right[j]
        j+=1
        k+=1

def Merge_sort(arr,left,right):
    if left<right:
        mid=(left+right)//2
        Merge_sort(arr,left,mid)
        Merge_sort(arr,mid+1,right)
        Merge(arr,left,mid,right)

test_case=[10,5,30,15,7]
Merge_sort(test_case,left=0,right=len(test_case)-1)
print(test_case)









time.sleep(1)
end=time.time()
print(f"Total Time Taken:{end-begin}")
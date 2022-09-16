import time
begin=time.time()

# Ques implementation of quick sort using Laumuto partition

def loumuto_partition(arr,low,high):#low=0 high len(arr)-1
    pivot=arr[high]
    i=low-1
    for j in range(low,high):
        if (arr[j]<=pivot):
            i=i+1
            arr[i],arr[j]=arr[j],arr[i]
    arr[i+1],arr[high]=arr[high],arr[i+1]#arr[high]=pivot
    return i+1 # resulted index of pivot element when the array is sorted

def quick_sort(arr,low,high):
    if low<high:
        pivot_idx=loumuto_partition(arr,low,high)
        quick_sort(arr,low,pivot_idx-1)
        quick_sort(arr,pivot_idx+1,high)


test_case=[8, 4, 7, 9, 3, 10, 5]
low=0
high=len(test_case)-1
quick_sort(test_case,low,high)
print(*test_case)











time.sleep(1)
end=time.time()
print(f"Total Time Taken:{end-begin}")
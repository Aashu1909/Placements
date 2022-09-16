import time
begin=time.time()
# Q.Implement Loumuto partition scheme o(N) and o(1) aux-space
# Last element is considered as pivot
# test_case=[10,80,30,90,40,50,70] pivot=70
# O/p[10,30,40,50,70,90,80]
# So here if the element is smaller than pivot,then i=i+1 and swapped with j
# and at last arr[i+1],arr[high]=arr[hig],arr[i+1]
def Laumuto_partition(arr,low,high):
    pivot=arr[high]
    i=low-1
    for j in range(low,high):
        if (arr[j]<pivot):
            i=i+1
            arr[i],arr[j]=arr[j],arr[i]
    arr[i+1],arr[high]=arr[high],arr[i+1]
    return i+1
test_case=[10,80,30,90,40,50,70]
low=0
high=len(test_case)-1
print(Laumuto_partition(test_case,low,high))

time.sleep(1)
end=time.time()
print(f"Total Time Taken:{end-begin}")
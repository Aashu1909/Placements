import time
begin=time.time()
# Ques:Implement Bubble sort in python 
# test_case=[2,10,8,7]
# O/p [2,7,8,10]
# O(N^2) time O(1)
def bubble_sort(arr):
    swap=0
    for i in range(len(arr)-1):
       for j in range(0,len(arr)-i-1):
        if arr[j]>arr[j+1]:
            arr[j],arr[j+1]=arr[j+1],arr[j]
    return arr
test_case=[8,22,7,9,31,19,5,13]
print(bubble_sort(test_case))











time.sleep(1)
end=time.time()
print(f"Total Time Taken:{end-begin}")
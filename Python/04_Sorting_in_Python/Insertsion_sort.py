import time
begin=time.time()
# Ques Implement insertion sort
# It is the most efficient algo for small array,alse implemented in Hybrid algo(Tim-sort,Intro-Sort)
# It require o(n) in best case
# Idea of insertion sort that it maintains |sorted|unsorted| in this region.

def inserion_sort(arr):
    for i in range(1,len(arr)):
        curr_element=arr[i]
        j=i-1
        # iterate till arr[i]<arr[j]
        while j>=0 and curr_element<arr[j]:
            arr[j+1]=arr[j]
            j=j-1
        arr[j+1]=curr_element
    return arr

test_case=[20,5,40,60,10,30]
print(inserion_sort(test_case))











time.sleep(1)
end=time.time()
print(f"Total Time Taken:{end-begin}")
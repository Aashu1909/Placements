import time
begin=time.time()
# Q.Implementation of selection sort
# The idea of selection sort is to keep finding the minimum and placing it at  
# its optimal location in the array 
# Inplace algo requires o(1) aux space
#Selection sort is not a stable sortin g algorithm ie order of same element may not remain the same
# O(N^2) and o(1)
def selection_sort(arr):
    for i in range(0,len(arr)-1):
        min_index=i
        for j in range(i+1,len(arr)):
            if (arr[min_index]>arr[j]):
                min_index=j
        arr[i],arr[min_index]=arr[min_index],arr[i]
    return arr

test_case=[10,5,8,20,2,18]
print(selection_sort(test_case))











time.sleep(1)
end=time.time()
print(f"Total Time Taken:{end-begin}")
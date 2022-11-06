import time
begin=time.time()
# Q.task is to arrange element such tthat all the element 
# on the left is smaller than the Pivot element and larger on the right
# test_case=[3,8,6,12,10,7]
# O/p [3,6,7,2,12,10]  ,[6,3,7,12,8,10 ] theta(N) theta(N)space
def partition(arr,p):
    pivot_ele=arr[p]
    temp=[]
    for element in arr:
        if element<=pivot_ele:
            temp.append(element)
    for element in arr:
        if element>pivot_ele:
            temp.append(element)
    for i in range(len(arr)):
        arr[i]=temp[i]
    return arr
test_case=[5,13,6,9,12,8,11]
print(partition(test_case,6))









time.sleep(1)
end=time.time()
print(f"Total Time Taken:{end-begin}")
import time
begin=time.time()
# Ques merge two sorted list in python 
# a=[10,15] b=[5,6,6,30,40]
# O/p [5,6,6,10,15,30,40]
def merge_sorted_arr(arr1,arr2):
    m=len(arr1)
    n=len(arr2)
    i=j=0
    merge_arr=[]
    while i<m and j<n:
        if arr1[i]<arr2[j]:
            merge_arr.append(arr1[i])
            i=i+1
        else:
            merge_arr.append(arr2[j])
            j=j+1

    while i<m:
        merge_arr.append(arr1[i])
        i+=1

    while j<n:
        merge_arr.append(arr2[j])
        j+=1
    return merge_arr

a=[10,15] 
b=[5,6,6,30,40]
print(merge_sorted_arr(a,b))











time.sleep(1)
end=time.time()
print(f"Total Time Taken:{end-begin}")
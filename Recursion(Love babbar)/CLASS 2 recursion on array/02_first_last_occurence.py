def first_occ(arr,index,target):
    if index==len(arr):
        return -1
    if arr[index]==target:
        return index
    else:
        return first_occ(arr,index+1,target)

def last_occ(arr,index,target):
    if index<0:
        return -1 
    if arr[index]==target:
        return index
    else:
        return last_occ(arr,index-1,target)

def all_occ(arr,index,target):
    if index==len(arr):
        print(-1)
        return
    if arr[index]==target:
        print(index,end=" ")
    all_occ(arr,index+1,target)

arr=[1,2,5,5,5,6,7]
# print(first_occ(arr,0,5))
# print(last_occ(arr,len(arr)-1,5))
print(all_occ(arr,0,5))
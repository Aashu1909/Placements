def print_arr(arr,index):
    if index==len(arr):
        return 
    print(arr[index])
    print_arr(arr,index+1)

def rev_print_arr(arr,index):
    if index==len(arr):
        return 
    rev_print_arr(arr,index+1)
    print(arr[index])

def reverse_pr(arr,index):
    if index<0:
        return   
    reverse_pr(arr,index-1)
    print(arr[index])
temp=[1,2,3,4,5,6]
# print_arr(arr,0)
# rev_arr1(arr,len(arr)-1)
reverse_pr(temp,len(temp)-1)
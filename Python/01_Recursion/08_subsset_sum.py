# In this Problem we are given an array 
# we need to find number of susets which equal to the given sum
# [10,5,2,3,6] k=8
# op 2 [5,3] [2,6]


# Here in the recursion tree we will have 2 options either take the index or pass the index (untake) the index

# Also we can reduce the number of recursion call by adding the if statement
# And if the comdition are met

def sum_subset(subset_arr,arr,subset_sum,index,k):
    if index==len(arr):
        if subset_sum==k:
            print(subset_arr)
        return 
    if index>len(arr):
        return 
    #Taking the index 
    subset_sum+=arr[index]
    subset_arr.append(arr[index])
    sum_subset(subset_arr,arr,subset_sum,index+1,k)
    # Pass the index so we have to remove and then call the function 
    subset_sum-=arr[index]
    # as the element we remove had been added at last only so we can use the POP method 
    subset_arr.pop()
    sum_subset(subset_arr,arr,subset_sum,index+1,k)


temp=[]
arr=[10,5,2,3,6]
k=8
print(sum_subset(temp,arr,0,0,k))
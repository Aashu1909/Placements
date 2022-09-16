# Partition Equal Subset Sum
# Here we have to take the array and divide them into 2 subsets
def partitionEqual(arr):
    if sum(arr)%2!=0:
        return False
    half_sum=sum(arr)/2
    n=len(arr)
    return solve(n-1,arr,half_sum)


def solve(index,target,arr)->bool:
    if target==0:
        return True
    if index==0:
        return (target==arr[index])

    notTake=solve(index-1,target,arr)
    take=False
    if arr[index]<=target:
        take=solve(index-1,target-arr[index],arr)
    return (take or notTake)
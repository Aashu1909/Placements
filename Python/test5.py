def findMin(nums) -> int:
    start=0
    n=len(nums)
    end=n-1
    res=nums[start]
    if nums[start]<nums[end]:
        return nums[start]
    while start<=end:

        mid=start+(end-start)//2
        nex=(mid+1)%n
        prev=(mid-1+n)%n
        print(start,mid,end)
        if nums[mid]<=nums[nex] and nums[mid]<=nums[prev]:
            return nums[mid]
        elif nums[start]<=nums[mid]:
            start=mid+1
        elif nums[mid]<=nums[end]:
            end=mid-1
    
    return res
#        0 1 2 3 
nums = [3,3,3,1]
print(findMin(nums))



t=int(input())
while t>0:
    lenght_wall,N=list(map(int,input().split()))
    bar=list(map(int,input().split()))
    solve(bar,lenght)
    t-=1
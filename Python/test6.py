def fourSum(nums, target):
    n=len(nums)
    left,right=0,n-1
    left1,right1=1,n-2
    ans=[]
    nums.sort()
    while left<right and left1<right1:
        fourSum=nums[left]+nums[right]+nums[left1]+nums[right1]
        print(fourSum)
        print(left,left1,right1,right)
        if fourSum==target:
            ans.append([nums[left],nums[left1],nums[right1],nums[right]])
            left1+=1
            left+=1
            right-=1
            right1-=1
        elif fourSum<target:
            left1+=1
            left+=1
        else:
            right-=1
            right1-=1
    return ans

nums = [1,0,-1,0,-2,2]
target = 0
print(fourSum(nums,target))
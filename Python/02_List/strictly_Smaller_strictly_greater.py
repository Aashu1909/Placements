
def countElements(nums):
    MinumumNumber=min(nums)
    MaximumNumber=max(nums)
    res=0
    for i in nums:
        if(MinumumNumber < i < MaximumNumber):
            res+=1
    return (res)

nums= [11,7,2,15]
print(countElements(nums))
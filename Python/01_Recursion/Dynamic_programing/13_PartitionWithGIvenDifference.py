# ReCursion+Memoization
def solve(index,sum,nums,dp):
    if (index==0):
        if (sum==0 and nums[index]==0): return 2 #Because 2 subsequence will generate one with 0 another eithout 0
        if (sum==0): return 1#only one subsequence will generate
        return 0
    if (index,sum) in dp:
        return dp[(index,sum)]
    notTake=0+solve(index-1,sum,nums,dp)
    take=0
    if(nums[index]<=sum):
        take=solve(index-1,nums,sum-nums[index])
    dp[(index,sum)]=notTake+take
    return dp[(index,sum)]

def partitionWithGivenDiff(nums,sum):
    n=len(nums)
    dp={}
    return solve(n-1,sum,nums,dp)

def countPartitions(nums,d):
    totalSum=sum(nums)
    if(totalSum-d<0) or ((totalSum-d)%2): return False
    return partitionWithGivenDiff(nums,(totalSum-d)//2)
    
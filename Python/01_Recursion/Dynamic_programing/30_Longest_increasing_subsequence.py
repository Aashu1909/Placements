from bisect import bisect_left as lower_bound
class Solution:
    # Tn of O(n*n) space n*n + n aux stack recursion
    def lengthOfLIS(self, nums) -> int:
        n=len(nums)
        dp=[[-1 for _ in range(n+1)] for _ in range(n)]
        def solve(index,prev_index):
            if index==n:
                return 0
            if dp[index][prev_index+1]!=-1:
                return dp[index][prev_index+1]
            take=0
            if prev_index==-1 or nums[prev_index]<nums[index]:
                take=1+solve(index+1,index)
            notTake=solve(index+1,prev_index)
            dp[index][prev_index+1]=max(take,notTake)
            return dp[index][prev_index+1]
        return solve(0,-1)
    
    # Tn O(Nlogn) space N
    def optimised_LIS(self,nums):
        n=len(nums)
        temp=[]
        l=0
        for i in range(n):
            if temp and temp[-1]<nums[i]:
                temp.append(nums[i])
                l+=1
            else:
                ind=lower_bound(temp,nums[i])
                if not temp and ind==0:
                    l+=1
                    temp.append(nums[i])
                temp[ind]=nums[i]
        print(temp)
        return l

    def print_LIS(self,arr):
        n=len(arr)
        ans=[]
        def solve(index,prev_index,subseq):
            if index==n:
                ans.append(subseq[:])
                return
            if prev_index==-1 or arr[prev_index]<arr[index]:
                subseq.append(arr[index])
                solve(index+1,index,subseq)
                subseq.pop()
            solve(index+1,prev_index,subseq)
        solve(0,-1,[])
        return len(ans)


nums = [10,9,2,5,3,7,101,18]
obj=Solution()
print(obj.print_LIS(nums))
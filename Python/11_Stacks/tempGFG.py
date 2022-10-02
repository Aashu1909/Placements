class Solution:
    #Function to calculate the span of stockâ€™s price for all n days.
    def prev_greater(self,arr):
        n=len(arr)
        ans=[]
        stack=[]
        for i in range(n):
            while stack and stack[-1][0]<arr[i]:
                stack.pop()
            if len(stack)!=0:
                ans.append(stack[-1])
            else:
                ans.append((-1,-1))
            stack.append((arr[i],i))
        return ans
    
    def calculateSpan(self,a,n):
        #code here
        prev=self.prev_greater(a)
        result=[]
        for i in range(n):
            diff=i-prev[i][1]
            result.append(diff)
        return result
    
obj=Solution()
n=int(input())
arr=list(map(int,input().split()))
exp_ans=list(map(int,input().split()))
ans=obj.calculateSpan(arr,n)
for i in range(n):
    if ans[i]!=exp_ans[i]:
        print(i)
        print(ans[i],exp_ans[i])
print("correct")




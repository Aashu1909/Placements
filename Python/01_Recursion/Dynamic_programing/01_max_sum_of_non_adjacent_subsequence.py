# Given a list with n number of elements we need to find the 
# max sum that can be  formend by subsequence formed by Non adjacent element

# 1.MEMOIZATION Tn(O(N)) S(O(N)+O(N)stack)
def solve(index,arr,dp):
    # if n is negative that means that idx was at 1 can since we 
    # require non adjacent element we have to  subtract 2 from it hence we return 0
    if index<0:
        return 0
    # if index==0 that means f(2) has called this because f(1) cannot call because of adjacency
    if index==0:
        return arr[index]
    if index in dp:
        return dp[index]
    pick=arr[index]+solve(index-2,arr,dp)
    not_pick=0+solve(index-1,arr)
    dp[index]=max(pick,not_pick)
    return dp[index]

# 2 Tabulization Tn(O(N)) S(O(N)+O(N)stack)
# So tabulation is like building from 0->n
# Bottom up dp
def solve1(arr):
    n=len(arr)
    dp=[-1]*(n)
    #so when index is negative
    negative=0
    dp[0]=arr[0]
    for idx in range(1,len(arr)):
        pick=arr[idx]+(negative if (idx-2<0)else dp[idx-2])
        not_pick=0+dp[idx-1]
        dp[idx]=max(pick,not_pick)
    return dp[n-1]

# 3. Space optimization Tn(O(N)) Sn(O(1)))
def solve1(arr):
    prev2=0
    negative=0
    prev=arr[0]
    curr=0
    for idx in range(1,len(arr)):
        pick=arr[idx]+(negative if (idx-2<0)else prev2)
        not_pick=0+prev
        curr=max(pick,not_pick)
        prev2=prev
        prev=curr
    return prev

def maxNonAdjSum(arr):
    return solve(arr,len(arr))


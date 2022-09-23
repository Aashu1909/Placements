# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/
# Find the maximum profit you can achieve. You may complete at most k transactions.
class Solution:
    def maxProfit(self, k: int, prices) -> int:
        n=len(prices)
        dp=[[[-1 for _ in range(k+1)] for _ in range(2)] for _ in range(n)]
        def solve(i,canBuy,t):
            if i==n:
                return 0
            if t==0:
                return 0
            profit=0
            if dp[i][canBuy][t]!=-1: return dp[i][canBuy][t]
            if canBuy:
                buy=(-prices[i])+solve(i+1,0,t)
                not_buy=solve(i+1,1,t)
                profit=max(buy,not_buy)
            else:
                sell=(prices[i])+solve(i+1,1,t-1)
                hold=solve(i+1,0,t)
                profit=max(sell,hold)
            dp[i][canBuy][t]=profit
            return dp[i][canBuy][t]
        return solve(0,1,k)


k = 2
prices = [3,2,6,5,0,3]
obj=Solution()
print(obj.maxProfit(k,prices))

# Input: k = 2, prices = [3,2,6,5,0,3]
# Output: 7
# Explanation: Buy on day 2 (price = 2) and 
# sell on day 3 (price = 6), profit = 6-2 = 4.Then buy on day 5 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.

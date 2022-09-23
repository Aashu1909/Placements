# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/
# Find the maximum profit you can achieve. You may complete at most two transactions.

class Solution:
    def maxProfit(self, prices) -> int:
        n=len(prices)
        dp=[[[-1]*3 for _ in range(2)] for _ in range(n)]
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
        return solve(0,1,2)

prices = [3,3,5,0,0,3,1,4]
obj=Solution()
print(obj.maxProfit(prices))
# Input: prices = [3,3,5,0,0,3,1,4]
# Output: 6
# Explanation: Buy on day 4 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.
# Then buy on day 7 (price = 1) and sell on day 8 (price = 4), profit = 4-1 = 3.
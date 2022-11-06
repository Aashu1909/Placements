# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/

class Solution:
    def maxProfit(self, prices) -> int:
        dp=[[-1]*2 for _ in range(len(prices))]
        n=len(prices)
        def solve(i,canBuy):
            if i==len(prices):
                return 0
            if dp[i][canBuy]!=-1:
                return dp[i][canBuy]
            profit=0
            if canBuy==1:
                not_buy=solve(i+1,1)
                buy=(-prices[i])+solve(i+1,0)
                profit=max(buy,not_buy)
            else:
                sell=prices[i]+solve(i+1,1)
                hold=solve(i+1,0)
                profit=max(sell,hold)
            # print(i,buy)
            dp[i][canBuy]=profit
            return dp[i][canBuy]
        return solve(0,1)

    def tabulization(self,prices):
        n=len(prices)
        dp=[[0]*2 for _ in range(len(prices)+1)]
        dp[n][0]=0
        dp[n][1]=0
        for i in range(n-1,-1,-1):
            for canBuy in range(0,2):
                profit=0
                if canBuy==1:
                    buy=(-prices[i])+dp[i+1][0]
                    not_buy=dp[i+1][1]
                    profit=max(buy,not_buy)
                else:
                    sell=prices[i]+dp[i+1][1]
                    hold=dp[i+1][0]
                    profit=max(sell,hold)
                # print(profit)
                dp[i][canBuy]=profit
        # print(dp)
        return dp[0][1]

prices = [7,1,5,3,6,4]
obj=Solution()
print(obj.maxProfit(prices))
print(obj.tabulization(prices))
# Input: prices = [7,1,5,3,6,4]
# Output: 7
# Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
# Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.
# Total profit is 4 + 3 = 7.
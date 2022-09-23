# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
class Solution:
    def maxProfit(self, prices) -> int:
        mini=prices[0]
        n=len(prices)
        profit=0
        for i in range(1,n):
            if mini>prices[i]:
                mini=prices[i]
            profit=max(profit,prices[i]-mini)
            
        return profit

prices = [7,1,5,3,6,4]
obj=Solution()
print(obj.maxProfit(prices))
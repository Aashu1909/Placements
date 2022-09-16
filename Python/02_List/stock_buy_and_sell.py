# Assume we know the Prices of a stock for upcoming 5 days
# return the max profit that can be made during this period.



def max_profit(price,start,end):
    if end<=start:
        return 0
    profit=0
    for i in range(start,end):
        for j in range(i+1,end+1):
            if price[j]>price[i]:
                curr_profit=price[j]-price[i]+max_profit(price,start,i-1)+max_profit(price,j+1,end)
                print(price[j],":",price[i]," ",curr_profit)
                profit=max(profit,curr_profit)
                print(profit)
    return profit
test_case=[1, 5, 3, 8, 12]
print(max_profit(test_case,0,len(test_case)-1))
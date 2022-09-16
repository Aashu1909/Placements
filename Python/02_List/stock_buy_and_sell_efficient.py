# Assume we know the Prices of a stock for upcoming 5 days
# return the max profit that can be made during this period.

def max_profit(price):
    profit=0
    for i in range(len(price)):
        if price[i]>price[i-1]:
            profit+=price[i]-price[i-1]
            print(price[i],"-",price[i-1],"=",profit)
    return profit

test_case=[1, 5, 3, 2, 12]
print(max_profit(test_case))
# Basically here the idea is to find the nearest greter element to the left
# and storing the pair which consist the element and its corresponding index
# (nearestGreterToLeft,INDEX)

# The problem is till how many consecutive days the stock price is greater than its left arr
def stock_span(arr):
    n=len(arr)
    stack=[(-1,0)]
    index_arr=[]
    for i in range(n):
        while stack and stack[-1][0]<arr[i]:
            stack.pop()
        if stack:
            index_arr.append(stack[-1])
        else:
            # Stack is Emptys
            index_arr.append((-1,i))
        stack.append((arr[i],i))

    result=[]
    for i in range(0,n):
        result.append(i-index_arr[i][1])
    return result

arr=[100,80,60,70,60,75,85]
# [0, 1, 1, 2, 1, 4, 6]
print(arr)
print(stock_span(arr))
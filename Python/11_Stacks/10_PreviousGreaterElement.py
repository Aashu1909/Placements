# Here we are given an array we have to find Prev greater element 
# for each element for the input array

def prev_greater_element_naive(arr):
    n=len(arr)
    prev_greater=[]
    for i in range(n):
        has_greater=False
        for j in range(i-1,-1,-1):
            if arr[j]>arr[i]:
                has_greater=True
                prev_greater.append(arr[j])
                break
        if has_greater==False:
            prev_greater.append(-1)
    return prev_greater

# Efficient solution based on stock span problem
def prev_greater_element(arr):
    stack=[]
    n=len(arr)
    ans=[-1]
    stack.append(arr[0])
    for i in range(1,n):
        while stack and stack[-1]<=arr[i]:
            stack.pop()
        if stack:
            ans.append(stack[-1])
        else:
            # if stack is Empty append -1 coz there is no greater element on left.
            ans.append(-1)
        stack.append(arr[i])
    return ans
    

arr=[20,30,10,5,15]
print(arr)
print(prev_greater_element_naive(arr))
print('Efficient',prev_greater_element(arr))

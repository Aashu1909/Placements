def next_greater(arr):
    n=len(arr)
    stack=[]
    ans=[]
    for i in range(n-1,-1,-1):
        while stack and stack[-1]<arr[i]:
            stack.pop()
        if stack:
            ans.append(stack[-1])
        else:
            ans.append(-1)
        stack.append(arr[i])
    ans.reverse()
    return ans

arr=[1,3,2,4]
print(arr)
print(next_greater(arr))
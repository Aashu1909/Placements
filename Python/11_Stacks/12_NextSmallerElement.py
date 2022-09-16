'''
Problem:- to find the next smaller element in the array
'''
def next_smaller(arr):
    n=len(arr)
    stack=[]
    ans=[]
    for i in range(n-1,-1,-1):
        while stack and stack[-1]>arr[i]:
            stack.pop()
        if stack:
            ans.append(stack[-1])
        else:
            ans.append(-1)
        stack.append(arr[i])
    ans.reverse()
    return ans
arr=[6,2,5,4,5,1,6]
print(arr)
print(next_smaller(arr))
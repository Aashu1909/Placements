'''
Problem:- to find the next smaller element in the array
'''
def next_smaller(arr):
    n=len(arr)
    stack=[]
    nsr=[]
    for i in range(n-1,-1,-1):
        while stack and stack[-1]>arr[i]:
            stack.pop()
        if stack:
            nsr.append(stack[-1])
        else:
            nsr.append(-1)
        stack.append(arr[i])
    nsr.reverse()
    return nsr
arr=[6,2,5,4,5,1,6]

# op [2, 1, 4, 1, 1, -1, -1]
print(arr)
print(next_smaller(arr))
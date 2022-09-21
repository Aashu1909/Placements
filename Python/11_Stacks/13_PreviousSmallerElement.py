'''
Q-To find the prev smaller element in the array 
'''
def previous_smaller(arr):
    n=len(arr)
    stack=[]
    ans=[]
    ans.append(-1)
    stack.append(arr[0])
    for i in range(1,n):
        while stack and stack[-1]>arr[i]:
            stack.pop()
        if stack:
            ans.append(stack[-1])
        else:
            ans.append(-1)
        stack.append(arr[i])
    return ans
    
arr=[2,6,4,7,3]
# op [-1, 2, 2, 4, 2]
print(arr)
print(previous_smaller(arr))

# def longestSubarray(arr):
#     # Write your code here
#     count=0
#     result=0
#     for i in range(1,len(arr)):
#         if abs(arr[i-1]-arr[i])<=0:
#             count+=1
#         else:
#             result=max(result,count)
#             count=0
#     return result

# ops=0
def solve (N,A):
    # code here
    ops=0
    ans=[]
    while len(set(A))>1 and ops<40:
        mn=min(A)
        mx=max(A)
        r=mn if mn!=0 else mx
        start,end=0,0
        temp=[]
        print(A)
        for i in range(start,len(A)):
            if (A[i]!=0 and not temp):
                temp.append(start)
            if i!=0:
                if A[i]!=A[i-1]:
                    temp.append(i)
                    start=i
                    break    
            A[i]=A[i]%r
            # temp_end=i
        ops+=1
        ans.append(temp)
    return ans
            
print(solve(6,[2, 2, 2, 3, 3, 3]))


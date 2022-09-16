# The question is to genertate number with rwo given number which only contain these num only
from collections import deque
def generate_number(a,b,n):
    que=deque()
    que.append(a)
    que.append(b)
    count=0
    ans=[]
    while count<n:
        curr_string=que[0]
        ans.append(curr_string)
        que.popleft()
        que.append(curr_string+a)
        que.append(curr_string+b)
        count+=1
    return ans

a='1'
b='2'
print(generate_number(a,b,10))
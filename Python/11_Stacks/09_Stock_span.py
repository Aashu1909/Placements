# Method 1 
# Naive
def print_span(arr):
    n=len(arr)
    span_list=[]
    for i in range(n):
        span=1
        for j in range(i-1,-1,-1):
            if arr[i]>=arr[j]:
                span+=1
            else:
                break
        span_list.append(span)
    return span_list

# Efficient Method 
def print_span(arr):
    stack=[]
    stack.append(arr[0])
    span_list=[1]
    for i in range(1,len(arr)):
        while stack and arr[stack[-1]]<=arr[i]:
            stack.pop()
        span= i+1 if len(stack)==0 else i-stack[-1]
        span_list.apped(span)
        stack.append(i)
    return span_list
    



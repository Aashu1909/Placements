# This nearest smaller function return the index of the NSL element present in the array 
def nearest_smaller_left(arr):
    n=len(arr)
    stack=[]
    index_arr=[-1]
    for i in range(1,n):
        while stack and stack[-1][0]>arr[i]:
            stack.pop()
        if stack:
            index_arr.append(stack[-1][1])
        else:
            # No Nearest Smaller Left element in arr 
            index_arr.append(-1)
        stack.append((arr[i],i))
    
    return index_arr

def nearest_smaller_right(arr):
    stack=[]
    n=len(arr)
    index_arr=[]
    psuedo_index=n
    for i in range(n-1,-1,-1):
        while stack and stack[-1][0]>arr[i]:
            stack.pop()
        if stack:
            index_arr.append(stack[-1][1])
        else:
            # if there is no nearest smaller in the right of the element
            index_arr.append(psuedo_index)
        stack.append((arr[i],i))
    
    index_arr.reverse()
    return index_arr

def maximum_area_histogram(arr):
    nsl=nearest_smaller_left(arr)
    nsr=nearest_smaller_right(arr)
    n=len(arr)
    width_arr=[0]*n
    for i in range(n):
        width_arr[i]=(nsr[i]-nsl[i])-1#-1 because of the 
    area_arr=[0]*n
    for i in range(n):
        area_arr[i]=width_arr[i]*arr[i]
    print('width',width_arr)
    print('area',area_arr)
    return max(area_arr)


arr=[6,3,5,4,5,2,6]
# width [1, 5, 1, 3, 1, 7, 1]
# area [6, 15, 5, 12, 5, 14, 6]
#ans 15

# print(arr)
# print(nearest_smaller_left(arr))
# print(nearest_smaller_right(arr))
print(maximum_area_histogram(arr))
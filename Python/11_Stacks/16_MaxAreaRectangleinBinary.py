from re import L


def nearest_smaller_left(arr):
    n=len(arr)
    index_arr=[]
    stack=[]
    psuedo_index=-1
    for i in range(n):
        while stack and stack[-1][0]>arr[i]:
            stack.pop()
        if len(stack)!=0:
            index_arr.append(stack[-1][0])
        else:
            index_arr.append(psuedo_index)
        stack.append((arr[i],i))
    return index_arr

def nearest_smaller_right(arr):
    n=len(arr)
    index_arr=[]
    stack=[]
    psuedo_index=n
    for i in range(n-1,-1,-1):
        while stack and stack[-1][0]>arr[i]:
            stack.pop()

        if len(stack)!=0:
            index_arr.append(stack[-1][0])
        else:
            index_arr.append(psuedo_index)
        stack.append((arr[i],i))
    
    return index_arr

def maximum_area_histogram(arr):
    left_smaller_index_arr=nearest_smaller_left(arr)
    right_smaller_index_arr=nearest_smaller_right(arr)
    print('left_indx',left_smaller_index_arr)
    print('right_indx',right_smaller_index_arr)
    n=len(arr)
    width_arr=[0]*n
    for i in range(n):
        width_arr[i]=right_smaller_index_arr[i]-left_smaller_index_arr[i]-1
    area_arr=[0]*n
    for i in range(n):
        area_arr[i]=width_arr[i]*arr[i]

    return max(area_arr)


def max_area_bin_matrix(matrix):
    n=len(matrix)
    m=len(matrix[1])
    first_row=[0]*m
    # firstly converting binary matrix to 1D matrix
    # For first row
    for j in range(m):
        first_row[j]=matrix[0][j]
    mx_area=maximum_area_histogram(first_row)
    print(mx_area)
    print(first_row)
    for i in range(1,n):
        for j in range(m):
            if matrix[i][j]==0:
                first_row[j]=0
            else:
                first_row[j]+=matrix[i][j]
        print(first_row)
        mx_area=max(mx_area,maximum_area_histogram(first_row))
    
    return mx_area

arr=[   [0,1,1,0],
        [1,1,1,1],
        [1,1,1,1],
        [1,1,0,0]
    ]

print(max_area_bin_matrix(arr))
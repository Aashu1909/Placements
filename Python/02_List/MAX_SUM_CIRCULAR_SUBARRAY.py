# arr[]=[10,5,-5]

def sum_circular_subarray(arr):
    result=arr[0]
    for i in range(len(arr)):
        curr_sum=arr[i]
        curr_max=arr[i]
        for j in range(1,len(arr)):
            index=(i+j)%len(arr)
            curr_sum+=arr[index]
            curr_max=max(curr_max,curr_sum)
        result=max(curr_max,result)
    return result

test_case=[5,-2,3,4]
print(sum_circular_subarray(test_case))

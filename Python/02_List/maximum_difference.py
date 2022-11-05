# Q find the maximum difference b/t two element in the list
# Complexity O(N^2) space O(1)
def maximum_difference(arr):
    max_diff=None
    for i in range(0,len(arr)):
        for j in range(i+1,len(arr)):
            if  max_diff==None or (arr[j]-arr[i])>max_diff :
                max_diff=arr[j]-arr[i]
    return max_diff

# So here the trick is to find the max at every moment and minimum of minValue of all the element 
# Time O(N) space o(1)
def max_difference_efficient(arr):
    minValue=arr[0]
    maximum_difference=arr[1]-arr[0]
    for i in range(len(arr)):
        maximum_difference=max(maximum_difference,(arr[i]-minValue))
        minValue=min(minValue,arr[i])
    return maximum_difference


test_case=[2,3,10,6,4,8,1]
print(maximum_difference(test_case))
print(max_difference_efficient(test_case))
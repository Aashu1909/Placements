# [2,0,2] element here represents height of the bar
# the question is how much water you can collect between bar
# O/P 2
# I/P arr[]=[3,0,1,2,5]
# O/P=3
# Array in sorted order

# To solve this problem we need need to find the max on left side
# and max on right side.
# Then result+=min(lmax,rmax)-arr[i]
# for i in range(1,len(arr)-1)
    # lmax=3 rmax=5
        # result+=3-0
        # result+=3-1
        # result+=3-2
        # result=6
# First Naive solution 
def get_water(arr):
    result=0
    right_max=None
    for i in range(1,len(arr)-1):
        left_max=arr[i]
        # Loop for finding the Leftmax
        for j in range(i+1):
            left_max=max(left_max,arr[j])
        right_max=arr[i]
        for k in range(i+1,len(arr)):
            right_max=max(right_max,arr[k])
        
        result+=(min(left_max,right_max)-arr[i])
    return result
test_case=[5,2,0,3,6]
print(get_water(test_case))
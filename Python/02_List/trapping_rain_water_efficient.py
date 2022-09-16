# element here represents height of the bar
# the question is how much water you can collect between bar
# I/P arr[]=[3,0,1,2,5]
# O/P=6
# if Array in sorted order return  
# To solve this problem we need need to find the max on left side
# and max on right side.
# Then result+=min(lmax,rmax)-arr[i]
# for i in range(1,len(arr)-1)
    # lmax=3 rmax=5
        # result+=3-0
        # result+=3-1
        # result+=3-2
        # result=6

# Efficient solution
def get_water(arr):
    # here we first compute lmax and right explicitly 
    # Then we compute the result
    # initiating lmax list
    # left[i] contains height of tallest bar to the
    # left of i'th bar including itself
    n=len(arr)
    left = [0]*n
 
    # Right [i] contains height of tallest bar to
    # the right of ith bar including itself
    right = [0]*n
 
    # Initialize result
    water = 0
 
    # Fill left array
    left[0] = arr[0]
    for i in range( 1, n):
        left[i] = max(left[i-1], arr[i])
 
    # Fill right array
    right[n-1] = arr[n-1]
    for i in range(n-2, -1, -1):
        right[i] = max(right[i + 1], arr[i]);
 
    # Calculate the accumulated water element by element
    # consider the amount of water on i'th bar, the
    # amount of water accumulated on this particular
    # bar will be equal to min(left[i], right[i]) - arr[i] .
    for i in range(0, n):
        water += min(left[i], right[i]) - arr[i]
 
    return water
test_case=[0,1,0,2,1,0,1,3,2,1,2,1]


print(get_water(test_case))
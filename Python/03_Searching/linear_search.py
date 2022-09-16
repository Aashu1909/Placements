# linear search can be used in an unsorted array
# in this algorithm if element is present in the list return the index
# else return -1
def linear_search(arr,ele):
    for i in range(len(arr)):
        if ele==arr[i]:
            return i
    return -1

test_case=[10,7,28,3,6,7]
print(linear_search(test_case,6))
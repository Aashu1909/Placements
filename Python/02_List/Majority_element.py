# An element is called majority element is it appear more than N/2 times
# complexity o(n^2) complexity of 
def majority_element(arr):
    for i in range(len(arr)):
        if (arr.count(arr[i]))>(len(arr)//2):
            return arr[i]

# the above solution requires O(N^2) complexity

# if a counter is used it will take O(N) time to construct a counter
# And accessing value usiong it will be O(1)
# Total time complexity =O(N)+
from collections import Counter
def majority_element_counter(arr):
    c_arr=Counter(arr)
    for element in c_arr:
        if c_arr[element]>len(arr)//2:
            return element
    return -1


test_case=[8,7,6,8,6,6,6,6]
# print(majority_element(test_case))
print(majority_element_counter(test_case))



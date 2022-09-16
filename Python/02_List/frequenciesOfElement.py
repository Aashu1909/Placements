# Q1 Print Frequencies of element in sorted array
def print_frequency(arr):
    count_dict={i:arr.count(i) for i in arr}
    return count_dict
test_case=[5,5,10,10,12,12,12,13]
print(print_frequency(test_case))
    

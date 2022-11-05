# arr=[10,12,14,7,8] op3 [14,7,8]
# arr=[5,10,20,6,3,8] op3 [6,3,8]
# Naive solution Time Complexity O(n^2)


def max_even_odd(arr):
    result=1
    for i in range(len(arr)):
        curr_len=1
        for j in range(i,len(arr)):
            if (arr[j]%2==0 and arr[j-1]%2!=0) or (arr[j]%2!=0 and arr[j-1]%2==0):
                curr_len+=1
            else:
                break
        result=max(result,curr_len)
    return result

# idea is seeing the consecutive element 
# if the ((ith element divisible by 2) and i+1 should not be divisible by 2)) and vice versaw
def max_even_odd_efficient(arr):
    result=1
    curr=1
    for i in range(1,len(arr)):
        if (arr[i]%2==0 and arr[i-1]%2!=0) or (arr[i]%2!=0 and arr[i-1]%2==0):
            curr+=1
            result=max(result,curr)
        else:
            curr=1
    return result

test_case=[10,12,14,7,8]
print(max_even_odd(test_case))
print(max_even_odd_efficient(test_case))
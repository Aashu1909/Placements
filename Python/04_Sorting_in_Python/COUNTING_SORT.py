# Counting Sort is a Non Compn based stable sorting algorithm based on count of dictinct element of the arary
# Time Complexity: O(n+k) where n is the number of elements in the input array and k is the range of input. 
# Auxiliary Space: O(n+k)
def count_sort(arr,n):
    cnt_arr=[0]*(max(arr)+1)
    for i in range(n):
        cnt_arr[arr[i]]+=1
    # For the position array what we do is add the prev
    #element count to the current element count
    for i in range(1,len(cnt_arr)):
        cnt_arr[i]=cnt_arr[i-1]+cnt_arr[i]
    # print(cnt_arr)
    sorted_arr=[0]*n
    # Now what we are basically doing after creating the position array from the cnt_arr
    #we are firstly decrementing the count and after then placing the decremented index at the sorted_arr
    for i in range(n-1,-1,-1):
        cnt_arr[arr[i]]-=1
        sorted_arr[cnt_arr[arr[i]]]=arr[i]
    return sorted_arr

test=[1, 3, 2, 3, 4, 1, 6, 4, 3]
print(count_sort(test,len(test)))
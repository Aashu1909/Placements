# arr[]=[0,1,1,0,1,0]  O/p 2
# arr=[1,1,1,1] O/p=4
# arr=[1,0,1,1,1,1,0,1] o/p 4
# naive solution O(N^2) O(1)
def get_count(arr):
    result=0
    for i in range(0,len(arr)-1):
        count=0
        for j in range(i,len(arr)-1):
            if arr[j]==1:
                count+=1
            else:
                break
            result=max(result,count)
    return result
# Efficient
def get_count_efficient(arr):
    result=0
    count=0
    for i in range(0,len(arr)-1):
        if arr[i]==0:
            count=0
        else:
            count+=1
        result=max(result,count)
    return result
test_case=[1,0,1,1,1,1,0,1]
print(get_count(test_case))
print(get_count_efficient(test_case))
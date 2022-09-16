# first of all a number is a leader if it greater than all
# the number on ots right hand side

def leader_in_array(arr):
    leader=[]
    for i in range(len(arr)):
        is_leader=True
        for j in range(i+1,len(arr)):
            if arr[j]>arr[i]:
                is_leader=False
                break
        if is_leader==True:
            leader.append(arr[i])
    return leader

# Here since the last element will always be the leader
# So traverse the list from the end and compare it with the current element 
# arr[i]>curr_leader curr_leader=arr[i]
# Complexity O(n)

def leader_efficient(arr):
    leader=[]
    curr_leader=arr[len(arr)-1]
    print(curr_leader)
    leader.append(curr_leader)
    for i in range(len(arr)-2,-1,-1):
        if arr[i]>curr_leader:
            curr_leader=arr[i]
            leader.append(curr_leader)
    return leader

test_case=[7,10,4,2,6,5,2]
print(leader_in_array(test_case))
print(leader_efficient(test_case))


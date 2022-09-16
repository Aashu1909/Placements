def cell(arr, days):
    new = arr[:] #get a copy of the array
    n = len(arr)

    if n == 1: print [0] #when only 1 node, return [0]

    for _ in range(days):
        new[0] = arr[1] #determine the edge nodes first
        new[n - 1] = arr[n - 2]

        for i in range(1, n-1):
            new[i] = 1 - (arr[i-1] == arr[i+1]) #logic for the rest nodes
        arr = new[:] #update the list for the next day

    return new

arr = [1, 1, 1, 0, 1, 1, 1, 1]
days = 2
print(cell(arr, days))
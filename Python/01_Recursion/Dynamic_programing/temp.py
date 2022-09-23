from bisect import bisect_left as lower_bound
from bisect import bisect_right as upper_bound

arr=[1,3,45,5,35,25,22,64,65,65,78]
k=44
for i ,v in enumerate(arr):
    print(f"{i}:{v}",end=" ")
print()
print('lower_bound',lower_bound(arr,k))
print('upper_bound',upper_bound(arr,k))

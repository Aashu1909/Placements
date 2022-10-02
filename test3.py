from functools import cmp_to_key
arr=[(1,5),(2,4),(3,3),(4,2),(5,1)]
def compare(a,b):
    print(a,b)
    if a[1]<b[1]:
        return 1
    return -1
print(arr)
arr.sort(key=cmp_to_key(compare))
for i,j in arr:
    print(i,j)
# print("1">"2")
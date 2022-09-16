import time
begin=time.time()

# Q.Given three index we need to combine the two subaraays formed by 
# Low-mid mid+1-high such that low-high results in a sorted form
# test_case[10,15,20,11,13] low=0 mid=2 high=4 [10,15,20] [11,13]
# O/p [10,11,13,15,20]

def merge(a, low, mid, high):
    left = a[low:mid + 1]
    right = a[mid + 1:high + 1] 
    i = j = 0
    k = low
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            a[k] = left[i]
            k += 1
            i += 1
        else:
            a[k] = right[j]
            k += 1
            j += 1
    while i < len(left):
        a[k] = left[i]
        i += 1
        k += 1
    while j < len(right):
        a[k] = right[j]
        j += 1
        k += 1


a = [10, 15, 20, 40, 8, 11, 55]
merge(a, 0, 3, 6)
print(*a) #this helps to print a list without using a loop










time.sleep(1)
end=time.time()
print(f"Total Time Taken:{end-begin}")
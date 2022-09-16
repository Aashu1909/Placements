def reverse_a_list(l):
    low=0
    high=len(l)-1
    while(low<high):
        temp=l[low]
        l[low]=l[high]
        l[high]=temp
        low+=1
        high-=1
    return l

test_list=[10,20,30,55,60]
print(reverse_a_list(test_list))
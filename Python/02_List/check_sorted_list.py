def check_sorted_list(l):
    if len(l)<=1:
        return True
    for i in (range(len(l)-1)):
        if l[i]>l[i+1]:
            return False
    return True

test_list=[10,20,30,45,45]
print(check_sorted_list(test_list))

    
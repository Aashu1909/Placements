def left_rotate_one(l):
    temp=l[0]
    list_lenght=len(l)-1
    for i in range(list_lenght):
        l[i]=l[i+1]
    l[list_lenght]=temp
    return l

# Direct Method 
def direct_method(l):
    temp_l=l[1:]+l[0:1]
    return temp_l

def direct_method_2(l):
    l.append(l.pop(0))
    return l

def left_rotate_d(l,d):
    while d>0:    
        temp=l[0]
        list_lenght=len(l)-1
        for i in range(list_lenght):
            l[i]=l[i+1]
        l[list_lenght]=temp
        d-=1
    return l

def right_rotate_d(l,d):
    list_lenght=len(l)-1
    while d>0:    
        temp=l[len(l)-1]
        for i in range(list_lenght,0,-1):
            l[i]=l[i-1]
        l[0]=temp
        d-=1
    return l



# test_list=[10,20,30,55,60]
test_list=[-1,-100,3,99]

# for i in range(4):
#     print(left_rotate_one(test_list))
#     print("Direct",direct_method(test_list))
# print("d")
print(right_rotate_d(test_list,2))
# print("Direct",direct_method_d(test_list,4))

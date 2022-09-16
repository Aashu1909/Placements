def odd_occuring_number(l):
    odd_occuring=[]
    for element in l:
        count=l.count(element)
        if count%2!=0:
            if element not in odd_occuring:
                odd_occuring.append(element)
    return odd_occuring

# Solution using XOR operator for only one odd occuring element
def odd_occuring_using_xor(l):
    result=0
    for element in l:
        result=result^element
    return result

    # 10^10=0
    # 0^10=10
    # 10^20^20^45^45^20=10

test_list=[10,20,20,45,45,20]
# output [10, 20]

print(odd_occuring_number(test_list))
print("XOR",odd_occuring_using_xor(test_list))


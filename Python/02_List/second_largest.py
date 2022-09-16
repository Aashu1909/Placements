def get_max(l):
    result=l[0]
    for i in range(l):
        result=max(result,l[i])    
    return result

def second_largest_two_iteration(l):
    if len(l)<=1:
        return None
    largest=get_max(l)
    second_largest=None 
    for x in l:
        if x!=largest:
            if second_largest==None:
                second_largest=x
            else:
                second_largest=max(second_largest,x)
    return second_largest


def second_largest_one_iteration(l):
    if len(l)<=1:
        return None
    largest=l[0]
    s_largest=None
    for element in l[1:]:
        if element>largest:
            s_largest=largest
            largest=element
        elif (element<largest):
            if s_largest==None or element>s_largest:  #[20,20,20,18] largest=20,s_largest=18
                s_largest=element
    return largest,s_largest # This returns in a Tuple Format   

    
test_list=[0,0,0,128]                             
largest,second_largest=second_largest_one_iteration(test_list)
largest2,second_largest2=second_largest_one_iteration(test_list)
print(largest,second_largest)
print(largest2,second_largest2)
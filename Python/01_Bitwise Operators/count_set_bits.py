# using right shift operator o(total bits in n)
def count_set_bits(number):
    count=0
    while number>0:
        binary_form='{:032b}'.format(number)
        print(binary_form,int(binary_form,2))
        if number&1: #it can be replaced by number%2!=0
            count+=1
        number=number>>1
        # It can be replaced by number=number//2
    return count
number=35
print(count_set_bits(number))
# Using Brian Kerningan Algorithm
# here the idea is to perform an AND operation
# between number& number-1 
def count_set_bits(number):
    count=0
    while number>0:
        bin_number='{:032b}'.format(number)
        bin_number1='{:032b}'.format(number-1)
        count+=1
        number=(number) & (number-1)
        print()
        print("number:",bin_number)
        print("number-1:",bin_number1)
        print("number&number-1:",'{:032b}'.format(number))
        
    return count

number=35
print(count_set_bits(number))
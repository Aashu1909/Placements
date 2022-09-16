# I/P n=5 k=1 from right 0101
# o/p Yes
# I/P n=8 k=2 from right 100
# o/p No
# I/P n=0 k=3 from right 000
# o/p No

# using left shift operator
def check_kth_bit_left(number,k):
    # this format gives us 32 bit binary number
    bin_form=int('{:032b}'.format(number))
    # Move one to Kth position from right
    if ( 1<<(k-1) & bin_form) !=0:
        return True
    else:
        return False

# Using Right Shift 
def check_kth_bit_right(number,k):
    bin_form=int('{:032b}'.format(number),2)
    # Move the bits toward right,perform AND with 1
    if (number>>(k-1)) & 1 ==1:
        return True
    else:
        return False


number=35
k=5
print(check_kth_bit_left(number,k))
print(check_kth_bit_right(number,k))
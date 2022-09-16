def countSetBits(n):
    # code here
    # return the count
    total_bit_count=0
    for i in range(1,n+1):
        bit_count=0
        number=i
        while number>0:
            bit_count+=1
            number=(number)&(number-1)
        total_bit_count+=bit_count
    return total_bit_count

# Optimized solution
def largestPowerof2(self,n):
    x=0
    # same as pow(2,x)
    while (1<<x)<=n:
        x+=1
    return x-1
    
def countSetBits(self,n):
    # code here
    # return the count
    if n==0:
        return 0
    largest_pow_of_2=self.largestPowerof2(n)
    print(largest_pow_of_2)
    bits_till_largest_power2=(1<<(largest_pow_of_2-1))*largest_pow_of_2
    major_bits_till_n= n -(1<<largest_pow_of_2) + 1
    remaining_bits_of_n= n - (1<<largest_pow_of_2)
    total_bits=bits_till_largest_power2+major_bits_till_n+self.countSetBits(remaining_bits_of_n)
    return total_bits
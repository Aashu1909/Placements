# check the given is a power of 2 or not??
def power_of_two(number):
    while number!=1:
        if number%2!=0:
            return False
        number=number//2
    return True

# Using Brian Kriningan algorithm
def power_of_two_optimized(number):
    if number==0:
        return False
    return number&(number-1)==0




number=64
print(power_of_two(64))
print(power_of_two_optimized(64))
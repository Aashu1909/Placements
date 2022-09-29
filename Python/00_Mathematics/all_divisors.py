def all_divisors(n):
    for i in range(1,n):
        if n%i==0:
            print(i)
test_case=156
all_divisors(test_case)
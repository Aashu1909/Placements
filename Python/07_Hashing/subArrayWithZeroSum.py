import time
begin=time.time()

# Ques
# test_case=[-3,2,3,1,6]
# O/p False
# Ques
# test_case={4, 2, 0, 1, 6}
# O/p True


def subArrayExists(arr, n):
    n_sum = 0
    s = set()
    for i in range(n):
        n_sum += arr[i]
        if n_sum == 0 or n_sum in s:
            return True
        s.add(n_sum)
    return False


test_case=[-3,2,3,1,6]
print(subArrayExists(test_case))











time.sleep(1)
end=time.time()
print(f"Total Time Taken:{end-begin}")
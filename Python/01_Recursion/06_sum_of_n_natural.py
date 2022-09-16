def get_sum(n):
    if n==0:
        return 0
    return 1+get_sum(n-1)

get_sum()
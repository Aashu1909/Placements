def countRepeatingDigits(N):
    res = 0
    cnt = [0] * 10
    while (N > 0):
        rem = N % 10
        cnt[rem] += 1
        N = N // 10
    for i in range(10):
        if (cnt[i] > 1):
            res += 1
    return res


def solve(val_list):
    array_b=[]
    for i in range(len(val_list)):
        a=i+1
        val=val_list[i]+a
        array_b.append(val%2)
    print(array_b)
    return array_b



def solution(n,values,x):
    if (n==len(values)):
        new_vals=Odd_Even(values)
    else:
        return
    return sum(solve(new_vals))

if __name__=='__main__':
    no_test_case=int(input())
    while no_test_case>0:
        n,x=list(map(int,input().split(" ")))
        values=list(map(int,input().split(" ")))
        ans=solution(n,values,x)
        print(ans)
        no_test_case-=1

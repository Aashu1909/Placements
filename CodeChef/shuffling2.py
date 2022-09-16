def Odd_Even(values):
    m=len(values)
    for i in range(m):
        if values[i]%2==0 and i%2==0:
            continue
        else:
            


def solve(val_lsit):
    


def solution(n,values):
    if (n==len(values)):
        new_vals=Odd_Even(values)
    else:
        return
    solve(new_vals)

if __name__=='__main__':
    no_test_case=int(input())
    while no_test_case>0:
        n=int(input())
        values=list(map(int,input().split(" ")))
        ans=solution(n,values)
        print(ans)
        no_test_case-=1

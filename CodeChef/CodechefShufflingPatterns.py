def Odd_Even(values):
    m=len(values)
    new_values=[]
    even=[]
    odd=[]
    for i in range(m):
        if values[i]%2!=0:
            odd.append(values[i])
        else:
            even.append(values[i])
    odd_index=0
    even_index=0
    for j in range(0,m):
        if j%2==0 and even_index<len(even):
            new_values.append(even[even_index])
            even_index+=1
        elif j%2!=0 and odd_index<len(odd):
            new_values.append(odd[odd_index])
            odd_index+=1

    while odd_index<len(odd):
        new_values.append(odd[odd_index])
        odd_index+=1

    while even_index<len(even):
        new_values.append(even[even_index])
        even_index+=1

    return new_values 


def solve(val_list):
    array_b=[]
    for i in range(len(val_list)):
        a=i+1
        val=val_list[i]+a
        array_b.append(val%2)
    print(array_b)
    return array_b



def solution(n,values):
    if (n==len(values)):
        new_vals=Odd_Even(values)
    else:
        return
    return sum(solve(new_vals))

if __name__=='__main__':
    no_test_case=int(input())
    while no_test_case>0:
        n=int(input())
        values=list(map(int,input().split(" ")))
        ans=solution(n,values)
        print(ans)
        no_test_case-=1

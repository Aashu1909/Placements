def Entry(cw,ar):
    a=max(cw)
    c=min(cw)
    b=sum(cw)-a-c
    d,e=ar
    if a+b<=d and c<=e:
        print("YES")
    else:
        print("NO")
    
                
if __name__=='__main__':
    no_test_case=int(input())
    while no_test_case>0:
        list_of_weight=list(map(int,input().split(" ")))
        chef_weights=list_of_weight[:3]
        airline_restrictions=list_of_weight[3:]
        Entry(cw=chef_weights,ar=airline_restrictions)
        no_test_case-=1

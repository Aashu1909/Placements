
def nambiar_number(number):
    number_lst=list(map(int,list(number)))
    n=len(number_lst)
    flag=True
    k=0
    ans=""
    while flag:
        if number_lst[k]%2==0:
            i=k
            summ=number_lst[i]
            while summ%2==0 and i+1<n:
                i+=1
                summ+=number_lst[i]
            ans+=str(summ)
            k=i+1
        else:
            i=k 
            summ=number_lst[i]
            while summ%2!=0 and i+1<n:
                i+=1
                summ+=number_lst[i]
            ans+=str(summ)
            k=i+1
        
        if k==n:
            flag=False
    
    return ans   


n = '9866364552'
print(nambiar_number(n))


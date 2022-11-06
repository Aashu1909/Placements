def find_permutation(S):
    # Code here
    ans=[]
    def permute(lst,index,n):
        if index==n-1:
            ans.append("".join(lst[:]))
        for j in range(index,n):
            lst[index],lst[j]=lst[j],lst[index]
            permute(lst,index+1,n)
            lst[index],lst[j]=lst[j],lst[index]
        
    lst=list(S)
    n=len(S)
    permute(lst,0,n)
    ans.sort()
    return ans,len(ans)

a="abcd"

print(find_permutation(a))
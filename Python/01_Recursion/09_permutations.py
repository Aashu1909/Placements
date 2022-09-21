def find_permutation(S):
    # Code here
    ans=[]
    def permute(lst,left,right):
        if left==right:
            ans.append(''.join(lst[:]))
            return 
        for i in range(left,len(lst)):
            # Swapping of left,i 
            lst[left],lst[i]=lst[i],lst[left]
            permute(lst,left+1,right)
            lst[left],lst[i]=lst[i],lst[left]
    lst=list(S)
    n=len(S)
    permute(lst,0,n-1)
    ans.sort()
    return ans,len(ans)

a="abcd"

print(find_permutation(a))
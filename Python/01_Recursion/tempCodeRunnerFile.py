
    def permute(lst,left,n):
        if left==right:
            ans.append(''.join(lst[:]))
            return 
        for i in range(left,len(lst)):
            # Swapping of left,i 
            lst[left],lst[i]=lst[i],lst[left]
            permute(lst,left+1,right)
            lst[left],lst[i]=lst[i],lst[left]

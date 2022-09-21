def subsequence_k(index,arr,subseq,ans,target,sm):
    if index==len(arr):
        if target==sm:
            ans.append(subseq[:])
        return 
# Same take and Not Take approach
    sm+=arr[index]
    subseq.append(arr[index])
    subsequence_k(index+1,arr,subseq,ans,target,sm)
    sm-=arr[index]
    subseq.pop()
    subsequence_k(index+1,arr,subseq,ans,target,sm)

arr=[1,2,3,5]
k=8
ans=[]
index=0
subseq=[]
sm=0
subsequence_k(index,arr,subseq,ans,k,sm)
print(ans)

# O(2^n) T(n) Space O(n) stack space
def subsequence(index,subseq,arr,ans):
    if len(arr)==index:
        temp="".join(subseq[:])
        ans.append(temp)
        return
    subseq.append(arr[index])
    subsequence(index+1,subseq,arr,ans)
    subseq.pop()
    subsequence(index+1,subseq,arr,ans)

# For str
s="abbcd"
# arr=[1,2,3,4]
ans=[]
subsequence(0,[],list(s),ans)
print(ans)
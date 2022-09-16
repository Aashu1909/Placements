# O(2^n) T(n) Space O(n) stack space
def subsequence(index,subseq,arr,ans):
    if len(arr)==index:
        ans.append(subseq[:])
        return
    subseq.append(arr[index])
    subsequence(index+1,subseq,arr,ans)
    subseq.pop()
    subsequence(index+1,subseq,arr,ans)

arr=[1,2,3,4]
ans=[]
subsequence(0,[],arr,ans)
print(ans)
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

def numberOfSubsequences (S,W):
        n=len(S)
        cnt=0
        ans=[]
        def solve(idx,subseq,t):
            nonlocal cnt
            if (idx==n):
                temp="".join(subseq[:])
                ans.append(temp)
                if temp==W:
                    print(temp)
                    cnt+=1
                return 
            subseq.append(t[idx])
            solve(idx+1,subseq,t)
            subseq.pop()
            solve(idx+1,subseq,t)
        solve(0,[],list(S))
        return cnt,ans

# For str
s="abcd" 
w="bcd"
# arr=[1,2,3,4]
ans=[]
# subsequence(0,[],list(s),ans)
print(numberOfSubsequences(s,w))    
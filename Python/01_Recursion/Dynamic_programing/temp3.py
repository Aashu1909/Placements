def numberOfUniqueGoodSubsequences( binary: str) -> int:
    n=len(binary)
    hashmap={}
    
    def solve(index,subseq,arr):
        if index==n:
            s="".join(subseq[:])
            print(hashmap)
            if s and (s in hashmap):
                return 0
            if s and ((s[0]=="0" and len(s)==1) or (s[0]!="0") ):
                hashmap[s]=True
                return 1 
            return 0
        subseq.append(arr[index])
        take=solve(index+1,subseq,arr)
        subseq.pop()
        notTake=solve(index+1,subseq,arr)
        return take+notTake
    return solve(0,[],list(binary))
s="111001101100000001001110110101110001100"
print(numberOfUniqueGoodSubsequences(s))
import time
begin=time.time()

# Ques
# test_case
# O/p

def nBitbinary(x,k):
    if x>(1<<k):
        return "invalid"
    lst=[] 
    while k>0:
        remainder=x%2
        lst.append(remainder)
        x=x//2
        k=k-1
    return lst[::-1]

def maxXor(a,b,k):
    if a>b:
        bin1=nBitbinary(b,k)
        bin2=nBitbinary(a,k)
    else:
        bin1=nBitbinary(a,k)
        bin2=nBitbinary(b,k)
    
    if len(bin1)==len(bin2):
        n=len(bin1)
        for i in range(n):
            if (int(bin1[i])^int(bin2[i])==0) and i!=n-1:
                bin1[i],bin1[i+1]=bin1[i+1],bin1[i]
        x="".join(list(map(str,bin1)))
        y="".join(list(map(str,bin2)))
        return int(x,2)^int(y,2)
        
print(maxXor(7,3,3))











time.sleep(1)
end=time.time()
print(f"Total Time Taken:{end-begin}")
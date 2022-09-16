def dailyTemperatures(temp):
    n=len(temp)
    ans=[0]*len(temp)
    for i in range(n-1):
        for j in range(i+1,n):
            if temp[j]>temp[i]:
                ans[i]=j-i
                break
    return ans
    
testcase=[73,74,75,71,69,72,76,73]
print(dailyTemperatures(testcase))
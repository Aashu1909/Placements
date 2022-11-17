import time
begin=time.time()
# Ques to print the smallest window which contain all the char of pat string
# test_case str1='aabcbcdbca' smallest wiondow='dbca'
def smallestDistinctWindow(str1,pat):
    n,m=len(str1),len(pat)
    if m>n or pat=="":
        return ""

    countPat,window={},{}
    for i in range(m):
        countPat[pat[i]]=countPat.get(pat[i],0)+1
    # have:-represent the unique element that require
    # need:-is the count of element in the pat
    have,need=0,len(countPat)
    #result has been initialised [left,right] 
    result,lenResult=[-1,-1],float("Infinity")
    left=0
    for right in range(n):
        charWindow=str1[right]
        window[charWindow]=window.get(charWindow,0)+1

        if charWindow in countPat and countPat[charWindow]==window[charWindow]:
            have+=1
        #If the count of element in window and CountaPat are same
        while have==need:
            if (right-left+1)<lenResult:
                result=[left,right]
                lenResult=right-left+1
            #Popping the left element from the window 
            window[str1[left]]-=1
            if str1[left] in countPat and window[str1[left]]<countPat[str1[left]]:                
                have-=1
            left+=1
    start,end=result
    return str1[start:end+1] if lenResult!=float('Infinity') else ""


str1="aabdbcdca"
pat="dbca"
print(smallestDistinctWindow(str1,pat))











time.sleep(1)
end=time.time()
print(f"Total Time Taken:{end-begin}")
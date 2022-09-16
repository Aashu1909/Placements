import time
begin=time.time()

# Check for anagram search

def areSame(txt,pat):
    for i in range(256):
        if txt[i]!=pat[i]:
            return False
    return True

def searchAnagram(txt,pat):
    n,m=len(txt),len(pat)
    if m>n:
        return False
    countTxt=[0]*256
    countPat=[0]*256

    for i in range(m):
        countTxt[ord(pat[i])-ord('a')]+=1
        countPat[ord(pat[i])-ord('a')]+=1

    for i in range(m,n):
        if areSame(countTxt,countPat):
            return True
        countTxt[ord(txt[i])-ord('a')]+=1
        countTxt[ord(txt[i-m])-ord('a')]-=1
    return False

txt="geeksforgeeks"
pat="frog"
print(searchAnagram(txt,pat))











time.sleep(1)
end=time.time()
print(f"Total Time Taken:{end-begin}")
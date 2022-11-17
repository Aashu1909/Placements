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
    # Initializr Count arr of txt and Pat
    countTxt=[0]*256
    countPat=[0]*256
    # Fill the pattern array and initiales if TXT till m
    for i in range(m):
        countTxt[ord(txt[i])-ord('a')]+=1
        countPat[ord(pat[i])-ord('a')]+=1
    # if They are same return true else slide the window
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
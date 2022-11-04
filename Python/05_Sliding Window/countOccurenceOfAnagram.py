def isAnagram(pat,txt):
    countWord=[0]*26

    for i in range(len(pat)):
        countWord[ord(pat[i])-97]+=1
        countWord[ord(txt[i])-97]-=1
    for i in range(26):
        if countWord[i]!=0:
            return False
    return True

def search(pat, txt):
    # code here
    ans=0
    print(ord('A'),ord("Z"))
    for i in range(len(txt)-len(pat)+1):
        if isAnagram(pat,txt[i:i+len(pat)]):
            ans+=1
    return ans

txt="forxxorfxdofr"
pat="for"
print(search(pat,txt))
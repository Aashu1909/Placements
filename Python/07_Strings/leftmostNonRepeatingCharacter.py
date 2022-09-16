from cmath import inf
import time
begin=time.time()

# This approch of finding the Non repeating character 
# is the Naive one which requires O(n^2) time complexity in the worst case 
# when every character is repeating
def nonRepeatingCharacterN(s):
    n=len(s)
    for i in range(n):
        flag=False
        for j in range(i+1,n):
            if s[i]==s[j]:
                flag=True
        if flag==False:
            return s[i]
            break
    return -1

#Efficient Approach Linear time Two traversal
# we Create a Count array for the character in the string and then in the second traversal return 
# the leftmost/First Non repreating character
def nonRepeatingCharacter(s):
    charCount=[0]*256
    n=len(s)
    for i in range(n):
        charCount[ord(s[i])]+=1
    for i in range(n):
        if charCount[ord(s[i])]==1:
            return s[i]
    return -1

#Efficient Approach Linear time One traversal + CONST traversal
# we Create a fill arrray initialised with -1 if a character occurs only once mark its index as i  
# if the character repeats then mark it as -1
def nonRepeatingCharacterOne(s):
    fillArr=[-1]*256
    n=len(s)
    for i in range(n):
        if fillArr[ord(s[i])]==-1:
            fillArr[ord(s[i])]=i
        else:
            fillArr[ord(s[i])]=-2
        
    res=inf
    for i in range(256):
        if fillArr[i]>=0:
            res=min(res,fillArr[i])
    return -1 if res==inf else s[res]




test_case="geeksforgeeks"
print("Naive",nonRepeatingCharacterN(test_case))
print("better",nonRepeatingCharacter(test_case))
print("efficeint",nonRepeatingCharacterOne(test_case))

time.sleep(1)
end=time.time()
print(f"Total Time Taken:{end-begin}")
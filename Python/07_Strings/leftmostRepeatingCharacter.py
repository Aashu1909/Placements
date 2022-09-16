import time
begin=time.time()

# Ques Leftmost Repeating Character
# abccbd
# out:b

def leftMostRepeatingCharacter(s):
    n=len(s)
    for i in range(n):
        for j in range(i+1,n):
            if s[i]==s[j]:
                return s[i]
    return -1


def leftMostRepeatingCharacter(s):
    charCount=[0]*256 #assuming the input in AScii value
    #if its in alphabets we can reduce the size to 26
    n=len(s)
    for i in range(n):
        charCount[ord(s[i])]+=1
    for i in range(n):
        if charCount[ord(s[i])]>1:
            return s[i]
    return -1


time.sleep(1)
end=time.time()
print(f"Total Time Taken:{end-begin}")
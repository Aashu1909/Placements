# Here Ord Function return the ASCII value of the alphabets
# Initialising a list of 256 element with zero

# Find the two string are Anagram of each other 
# A string/Word is an anagram if they are permutation of each other.
# ie they have the same frequency of letters
# abba baba
# abcdcs csdcba
def check_anagram(s1,s2):
    if len(s1)!=len(s2):
        return False
    count=[0]*256
    for i in range(len(s1)):
        count[ord(s1[i])]+=1
        count[ord(s2[i])]-=1

    for element in count:
        if  element!=0:
            return False
    return True    

print(check_anagram("abbc","babc"))


# Another way is to sort the list and then compare the strings if true Anagram otehrwise not
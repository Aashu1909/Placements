from collections import Counter
def isSubset(word,words2):
    subsetDict=dict(Counter(words2))
    print(subsetDict)
    wordDict=dict(Counter(word))
    ans=False
    for letter,count in subsetDict.items():
        try:
            if wordDict[letter]>=subsetDict[letter]:
                ans=True
        except:
            return False
    return ans
    
    
    
def wordSubsets( words1,words2):
    ans=[]
    for word in words1:
        if isSubset(word,words2):
            ans.append(word)
    return ans

words1 = ["amazon","apple","facebook","google","leetcode"]
words2 = ["e","oo"]
print(wordSubsets(words1,words2))
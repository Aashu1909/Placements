from collections import Counter
def checkGoodWord(word,count_dict):
        letterCount=dict(Counter(word))
        for letter in word:
            if letter not in count_dict:
                return False
            if letterCount[letter]>count_dict[letter]:
                return False
        return len(word)

def countCharacters( words, chars: str) -> int:
    count_word=dict(Counter(chars))
    sumWords=0
    for word in words:
        val=checkGoodWord(word,count_word)
        print(word,val)

        sumWords+=val
    return sumWords
words = ["cat","bt","hat","tree"]
chars = "atach"
print(countCharacters(words,chars))
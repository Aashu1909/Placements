import time
begin=time.time()

def min_lenght_word(str):
    lenght_word=len(str[0])
    min_len_word=str[0]
    for word in str[1:]:
        if len(word)<lenght_word:
            min_len_word=word
            lenght_word=len(word)
    
    return lenght_word,min_len_word 

def longest_comman_prefix(list_str):
    comman_prefix=""
    word_lenght,smallest_len_word=min_lenght_word(list_str)
    counter=0
    while word_lenght>0:
        start_letter=smallest_len_word[counter]
        for word in list_str:
            if word[counter]!=start_letter:
                return comman_prefix
        comman_prefix+=start_letter

        word_lenght-=1
        counter+=1
    if len(comman_prefix):
        return comman_prefix
    return None

strs = ["flower","flow","flight"]
# return fl
# strs = ["dog","racecar","car"]
# print(longestCommonPrefix(strs))
print(longest_comman_prefix(strs))









time.sleep(1)
end=time.time()
print(f"Total Time Taken:{end-begin}")

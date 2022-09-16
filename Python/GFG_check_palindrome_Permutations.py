def check_palindrome_permutation(string):
    # Here we are going to use dictionary
    # The catch of this method is,either the string must contain even number of letter 
    # or it should contain atmost one letter with Odd Frequency.
    count_dictionary=dict()
    for letter in string:
        if letter not in count_dictionary: 
            count_dictionary[letter]=1
        else:
            count_dictionary[letter]+=1
    
    # Now if we have number of odd greater than 1 return False cause it cannot 
    # have any permutation that can be a palindrome
    odd=0
    for frequency in count_dictionary.values():
        if frequency%2!=0:
            odd+=1
        if odd>1:
            return False
    return True
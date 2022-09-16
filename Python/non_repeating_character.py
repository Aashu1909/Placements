def nonrepeatingCharacter(s):
    #code here
    from collections import Counter
    count_dict=Counter(str_list)
    print(count_dict)
    for key,value in count_dict.items():
        if count_dict[key]==1:
            return key
    return '$'

test_case="hello"
print(nonrepeatingCharacter(test_case))

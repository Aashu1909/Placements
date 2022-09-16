from doctest import testfile


def countNonRepeated(arr,n):
    #Your code here
    count_dict=dict()
    ans_list=[]
    for element in arr:
        if element not in count_dict:
            count_dict[element]=1
        else:
            count_dict[element]+=1
    for key,frequency in count_dict.items():
        print(key,frequency)
        if frequency==1:
                ans_list.append(key)
    return (ans_list)

            
test_case=[1, 1, 2, 2 ,3 ,3 ,4, 5, 6, 7]
print(countNonRepeated(test_case,10))
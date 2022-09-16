# Check the odd ocuuring element in the list
def check_odd_occuring(inputList):
    odd_occuring=[]
    for i in range(len(inputList)):
        count=0
        for j in inputList:
            if j==inputList[i]:
                count+=1
        if count%2!=0:
            odd_occuring.append(inputList[i])
    return odd_occuring
# Use XOR operator when there is only one odd occuring element in the given array
def odd_occuring_XOR(inputlist):
    result=0
    # 4^4=0
    for element in inputlist:
        result=result^element
    return result

test_list=[4,4,4,3,5,5]
print(check_odd_occuring())
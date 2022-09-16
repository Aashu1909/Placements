import time
begin=time.time()

def twoSum(numbers, target):
    ans_list=[]
    start=0
    end=len(numbers)-1
    while end>start:
        # print(numbers[start],numbers[start])
        if numbers[start]+numbers[end]>target:
            end-=1
        elif numbers[start]+numbers[end]<target:
            start+=1
        elif numbers[start]+numbers[end]==target:
            ans_list.append(start+1)
            ans_list.append(end+1)
    return ans_list

def twoSum1(numbers, target):
    start = 0
    end = len(numbers) - 1
    res = []
    while start < end and len(res) == 0:
        if numbers[start] + numbers[end] < target:
            start = start + 1
        elif numbers[start] + numbers[end] > target:
            end = end - 1
        else:
            res.append(start + 1)
            res.append(end + 1)
    return res
test_case= [2,7,11,15]
target = 9
print("Answer",twoSum(test_case,target))
# print("Answer",twoSum1(test_case,target))







time.sleep(1)
end=time.time()
print(f"Total Time Taken:{begin-end}")

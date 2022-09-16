def canPartition(nums) -> bool:
    start=1
    end=len(nums)-2
    nums.sort()
    sumStart=nums[0]
    sumEnd=nums[-1]
    print(nums)
    while sumStart!=sumEnd and sumStart<=sumEnd:
        print('start',start,'end',end)
        if sumStart<sumEnd:
            sumStart+=nums[start]
            start+=1
            print('sumstart<sumend',sumStart,sumEnd)
            print('start',start)
        else:
            sumEnd+=nums[end]
            print('sumstart<sumend',sumStart,sumEnd)
            end-=1
        print('start',start,'end',end)
        print(sumStart,':',sumEnd)
    if sumStart==sumEnd:
        return True
    return False

testcase=[1,3,4,4]
print(canPartition(testcase))
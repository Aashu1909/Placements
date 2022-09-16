import time
begin=time.time()


def countDistinctElementinWindow(arr,k):
    n=len(arr)
    count_arr=[]
    for i in range(n-k):
        count=0
        for j in range(k):
            flag=False
            for p in range(j):
                if arr[i+j]==arr[i+p]:
                    flag=True
                    break
            if flag!=True:
                count+=1
        count_arr.append(count)
    return count_arr





test_case=[10,10,5,3,20,5]
k=4
print(countDistinctElementinWindow(test_case,k))











time.sleep(1)
end=time.time()
print(f"Total Time Taken:{end-begin}")
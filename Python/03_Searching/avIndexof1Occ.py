def indexOfFirstOccurence(arr,element):
    low=0
    high=len(arr)-1
    res=-1
    while (low<=high):
        print('low-high',low,"-",high)
        mid=(high+low)//2
        print("arr mid",mid,":",arr[mid])
        if arr[mid]==element:
            res=mid
            high=mid-1
        elif arr[mid]>element:
            high=mid-1
        elif arr[mid]<element:
            low=mid+1
    return res

test_case=[5,7,7,8,8,10]
print(indexOfFirstOccurence(test_case,8))


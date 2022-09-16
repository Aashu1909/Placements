def minimumPlatform(n,arr,dep):
    arr.sort()
    dep.sort()
    result=1
    i,j=1,1
    platform_needed=1
    while (i<n) and (j<n):
        print(i,j)
        if arr[i]<=dep[j]:
            platform_needed+=1
            i+=1       
        elif arr[i]>dep[j]:
            platform_needed-=1
            j+=1
    if result<platform_needed:
        result=platform_needed
    return result
    
arr=[900, 940, 950, 1100, 1500, 1800]
dep=[910, 1200, 1120, 1130, 1900, 2000]

print(minimumPlatform(len(arr),arr,dep))

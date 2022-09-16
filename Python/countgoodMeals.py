from collections import Counter
def countPairs(deliciousness) -> int:
    MOD=10**9+7
    counts=Counter()
    total=0
    for x in deliciousness:
        print(x,counts)
        for y in range(22):
            target=(1<<y)-x
            print(f"Target:{(1<<y)}-{x}=",target)
            if target in counts:
                print("target in counts",target)
                total+=counts[target]
                print('total',total)
        counts[x]+=1
    return total%MOD


testcase=[1,3,5,7,9]
# [1,1,1,3,3,3,7]
print(countPairs(testcase))
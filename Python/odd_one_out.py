def return_odd(arr):
    n,m=len(arr),len(arr[0])
    temp=[]
    for w in arr:
        sm,i=0,1
        a=ord(w[0])
        while i<m:
            t=ord(w[i])-a
            sm+=(t)
            i+=1
        temp.append(sm)
    print(temp)
    if temp[0]!=temp[1] and temp[1]==temp[2]:
        return arr[0]
    for i in range(1,n):
        if temp[i-1]!=temp[i]:
            return arr[i]
n=int(input())
str1=[]
for _ in range(n):
    txt=input()
    str1.append(txt)
print(str1)
print(return_odd(str1))
# arr=["acb","bdc","ced","def"]
# print(return_odd(arr))
# arr=["abcd","bcde","efgh","dcbe"]
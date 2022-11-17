temp=[]
def get_all_subset(index,curr,s):
    if len(s)==index:
        if curr:
            temp.append(curr)
        return 
    get_all_subset(index+1,curr+s[index],s)
    get_all_subset(index+1,curr,s)

get_all_subset(0,'','abcd')
print(*temp)
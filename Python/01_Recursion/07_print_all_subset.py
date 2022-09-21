temp=[]
def get_all_subset(input,output,i):
    if len(input)==i:
        if len(output)!=0:
            temp.append(output)
        return
    # not including first character in the output
    get_all_subset(input,output,i+1)
    # input including the first character
    output+=input[i]
    get_all_subset(input,output,i+1)

get_all_subset('abcd','',0)
print(*temp)
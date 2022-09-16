def reverseStr(s: str, k: int) -> str:
    if len(s)<k:
        return s[::-1]
    char_list=list(s)
    rev_list=char_list[:k]
    remaining_lst=char_list[k:]
    ans=rev_list[::-1]+remaining_lst
    print(ans)
    return "".join(ans)
s = "abcdefg"
k = 2
print(reverseStr(s,k))
# "bacdfeg"
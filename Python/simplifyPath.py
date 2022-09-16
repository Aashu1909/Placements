def simplifyPath(path):
    stack = []
    print(path)
    print(path.split("/"))
    for p in path.split("/"):
        if p == '..' and len(stack) > 0:
            stack.pop()
        if p == '' or p == '.' or p =='..':
            continue
        else:
            stack.append(p)
    res=""

    while len(stack)>0:
        res='/'+stack.pop()+res
        
    if len(res)==0:
        return "/"
    return res
path="/home/a/b/c/../"
print(simplifyPath(path))
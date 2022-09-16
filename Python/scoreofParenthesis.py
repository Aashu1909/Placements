def scoreOfParentheses( s: str) -> int:
    count = 0
    stack = []
    flag = 0
    i=0
    while i==0 or len(stack)!=0:
        print("stack:",stack)
        if s[i] == "(":
            print(i,"(")
            flag = 1
            stack.append("(")
        if s[i] == ")":
            if flag == 1:
                count += 2**(len(stack)-1)
                flag = 0                
            stack.pop()
        print(count)
        i+=1
    return count
testcase="(()((())))"
print(scoreOfParentheses(testcase))
# Valid parenthesis using stack
def isMatching(last_ele,curr_ele):
    if (last_ele=="{" and curr_ele=="}"):
        return True
    elif (last_ele=="(" and curr_ele==")"):
        return True
    elif (last_ele=="[" and curr_ele=="]"):
        return True
    else:
        return False

def valid_parenthesis(string):
    stack=[]
    for element in string:
        if element in ["{","[","("]:
            stack.append(element)
        else:
            if isMatching(stack[-1],element)!=True:
                return False
            else:
                stack.pop()
    if len(stack)<1:
        return True
    return False

string="[[[[{{{{(((())))}}}}]]}]]"
print(valid_parenthesis(string))
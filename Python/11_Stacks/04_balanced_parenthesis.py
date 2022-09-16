# The first method is to use a replace funtion 
# this requries o(N^2) t(n)
def valid_parenthesis(string):
    for i in range(len(string)//2):
        string =string.replace("()","").replace("{}","").replace("[]","")
    if len(string)!=0:
        return False
    return True

string="[[[[{{{{(((())))}}}}]]]]"
print(valid_parenthesis(string))
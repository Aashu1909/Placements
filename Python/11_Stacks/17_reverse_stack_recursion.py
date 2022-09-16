# Reverse a Stack using recursion O(1) space
from stack_class import Stack

def insert_at_bottom(stack,x):
    if stack.isEmpty():
        stack.push(x)
        return 
    else:
        top_ele=stack.top()
        stack.pop()
        insert_at_bottom(stack,x)
        stack.push(top_ele)

def reverse(stack):
    if stack.size()>0:
        x=stack.top()
        stack.pop()
        reverse(stack)
        insert_at_bottom(stack,x)
    else:
        return
'''
I/P     O/P
 1       5   
 2       4
 3       3  
 4       2
 5       1
'''
stack=Stack()
stack.push(5)
stack.push(4)
stack.push(3)
stack.push(2)
stack.push(1)
print('original Stack')
stack.print()
reverse(stack)
print('reverse stack')
stack.print()
# there are two ways of impmenting Stacks in python
# 1 Using list 
# 2 Using modules

# 1 Method list
# stack=[]
# stack.append(10)
# stack.append(20)
# stack.append(30)
# print(stack)
# stack.pop()
# stack.pop()
# stack.pop()
# print(stack)
stack=[]
def push_element():
        element=input('Enter the element')
        stack.append(element)
        print(stack)

def pop_element():
    if not stack:
        print("Stack is emplty")
    else:
        removed_element=stack.pop()
        print(f"Removed Element:{removed_element}")
        print(stack)

run=True
while run:
    print("Select the operation 1.push 2.pop 3.Quit .")
    choice=int(input("Enter Your Choice."))
    if choice==1:
        push_element()
    elif choice==2:
        pop_element()
    elif choice==3:
        run=False
    else:
        print("Enter the Correct option")



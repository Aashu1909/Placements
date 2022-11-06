# Python3 program for iterative postorder traversal
# using one stack

# Stores the answer
ans = []

# A Binary tree node


class Node:
    # Constructor to create a new node
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def peek(stack):
    if len(stack) > 0:
        return stack[-1]
    return None
# A iterative function to do postorder traversal of
# a given binary tree

def postOrderIterative(root):
    if root==None:
        return None
    stack1=[root]
    stack2=[]
    while len(stack1)!=0:
        curr=stack1.pop()
        stack2.append(curr)
        if curr.left!=None:
            stack1.append(curr.left)
        if curr.right!=None:
            stack1.append(curr.right)
    postOrder=[]
    while len(stack2)!=0:
        postOrder.append(stack2.pop().data)
    return postOrder

# Driver program to test above function
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

print("Post Order traversal of binary tree is")
postOrderIterative(root)
print(ans)

# Postorder Traversal in Binary tree
# left Right root 20 40 50 30 10
#    10
#   /  \
# 20    30
#      /  \
#    40    50

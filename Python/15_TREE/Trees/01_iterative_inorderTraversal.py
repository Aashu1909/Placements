class Node:
    def __init__(self,data):
        self.left=None
        self.right=None
        self.key=data
# INORDER TRAVERSAL MEANS 
# LEFT-> ROOT-> RIGHT
# Here in iterative Inorder traversal
# First steep is to check that root should not be None 
# If root==none return none
# Otherwise initialse a stack 
def iterativeInorder(root):
    if root==None:
        return None
    stack=[]
    # Now after initialising a stack create a variable 
    # CURR which we will use to traverse the tree.
    # while curr!=None curr=curr.left 
    # Traverse the curr varuiable till the stack contain
    #  all the left tree nodes of the given Binary Tree.
    curr=root
    while curr!=None:
        stack.append(curr)
        curr=curr.left
    # Now after appending alll the values of Binary tree into the stack
    # Rum another loop for printing its InOrder traversal.

    while len(stack)!=0:
        # Pop the last node of the stack 
        # And print since Its the leftmost treenode of the given binary tree
        # Traverse its right part till curr!=None and append its left node in the stack
        curr=stack.pop()
        print(curr.key,end=" ")
        curr=curr.right
        while curr!=None:
            stack.append(curr)
            curr=curr.left 

# Time complexity (append and poping O(1) )-theta(n)
# Aux Space-theta(height)
# Driver Code
root = Node(10)
root.left = Node(20)
root.right = Node(30)
root.right.left = Node(40)
root.right.right = Node(50)
iterativeInorder(root)
# Inorder Traversal in Binary tree
# Left Root Right   20 10 40 30 50
#    10 
#   /  \
# 20    30
#      /  \
#    40    50
# T(n) O(number of nodes) 


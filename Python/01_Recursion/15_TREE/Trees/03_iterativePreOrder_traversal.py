class Node:
    def __init__(self,data):
        self.left=None
        self.right=None
        self.key=data
# PREORDER TRAVERSAL
# ROOT->LEFT->RIGHT
# Root Left Right   10 20 30 40 50
#    10 
#   /  \
# 20    30
#      /  \
#    40    50
# T(n) O(number of nodes)

def iterativePreorder(root):
    if root==None:
        return None
    stack=[root]
    while len(stack)!=0:
        curr=stack.pop()
        print(curr.key,end=" ")
        if curr.right!=None:
            stack.append(curr.right)
        if curr.left!=None:
            stack.append(curr.left)
# Driver Code

root = Node(10)
root.left = Node(20)
root.right = Node(30)
root.right.left = Node(40)
root.right.right = Node(50)
iterativePreorder(root)



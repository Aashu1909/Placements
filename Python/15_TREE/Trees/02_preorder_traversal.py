# Preorder Traversal in Binary tree
# root left Right  10 20 30 40 50
#    10 
#   /  \
# 20    30
#      /  \
#    40    50
# T(n) O(number of nodes) 

class Node:
    def __init__(self,data):
        self.left=None
        self.right=None
        self.key=data
    

def preOrder(root):
    if root!=None:
        print(root.key)
        preOrder(root.left)
        preOrder(root.right)

# Driver Code
root = Node(10)
root.left = Node(20)
root.right = Node(30)
root.right.left = Node(40)
root.right.right = Node(50)
preOrder(root)



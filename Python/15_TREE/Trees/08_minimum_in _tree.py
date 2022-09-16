from numpy import Infinity
class Node:
    def __init__(self,data):
        self.left=None
        self.right=None
        self.key=data
    
def minOfBinaryTree(root):
    if root==None:
        return Infinity
    leftMin=minOfBinaryTree(root.left)
    rightMin=minOfBinaryTree(root.right)
    return min(root.key,leftMin,rightMin)

# Driver Code=
root = Node(60)    
root.left = Node(-50)
root.right = Node(30)
root.right.left = Node(40)
root.right.right = Node(50)
print(minOfBinaryTree(root))
#    10 
#   /  \
# 20    30
#      /  \
#    40    50
from numpy import Infinity


class Node:
    def __init__(self,data):
        self.left=None
        self.right=None
        self.key=data
    
def maxOfBinaryTree(root):
    if root==None:
        return -Infinity
    leftMax=maxOfBinaryTree(root.left)
    rightMax=maxOfBinaryTree(root.right)
    return max(root.key,leftMax,rightMax)

# Driver Code=
root = Node(60)
root.left = Node(10)
root.right = Node(30)
root.right.left = Node(40)
root.right.right = Node(50)
print(maxOfBinaryTree(root))
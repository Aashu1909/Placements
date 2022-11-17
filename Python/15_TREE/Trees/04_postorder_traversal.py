# Postorder Traversal in Binary tree
# left Right root 20 40 50 30 10
#    10 
#   /  \
# 20    30
#      /  \
#    40    50
# T(n) O(N) aux Space theta(h) 
# PostOrder is not tail recursive and because of this this
#  traversal is faster when compared with 2

class Node:
    def __init__(self,data):
        self.left=None
        self.right=None
        self.key=data
    
def postOrder(root):
    if root!=None:
        postOrder(root.left)
        postOrder(root.right)
        print(root.key,end=" ")

# Driver Code
root = Node(10)
root.left = Node(20)
root.right = Node(30)
root.right.left = Node(40)
root.right.right = Node(50)
postOrder(root)



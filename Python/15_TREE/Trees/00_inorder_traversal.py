# Inorder Traversal in Binary tree
# Left Root Right   20 10 40 30 50
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

ans=[]

def inOrder(root):
    if root!=None:
        inOrder(root.left)
        ans.append(root.key)
        inOrder(root.right)        
# Driver Code

root = Node(10)
root.left = Node(20)
root.right = Node(30)
root.right.left = Node(40)
root.right.right = Node(50)
inOrder(root)

print(ans)




        

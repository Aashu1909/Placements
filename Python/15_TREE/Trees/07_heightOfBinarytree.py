#    10 
#   /  \
# 20    30
#      /  \
#    40    50
class Node:
    def __init__(self,data):
        self.left=None
        self.right=None
        self.key=data
    
def heightofBinTree(root):
    if root ==None:
        return 0
    leftHeight=heightofBinTree(root.left)
    rightHeight=heightofBinTree(root.right)
    return 1+(max(leftHeight,rightHeight))

# Driver Code
root = Node(10)
root.left = Node(20)
root.right = Node(30)
root.right.left = Node(40)
root.right.right = Node(50)
print(heightofBinTree(root))



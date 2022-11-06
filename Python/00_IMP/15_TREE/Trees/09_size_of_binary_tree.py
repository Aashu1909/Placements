class Node:
    def __init__(self,data):
        self.left=None
        self.right=None
        self.key=data
    
def sizeOfTree(root):
    if root==None:
        return 0
    else:
        leftSubTree=sizeOfTree(root.left)
        rightSubTree=sizeOfTree(root.right)
        ans=leftSubTree+rightSubTree+1
        return ans

# Driver Code
root = Node(10)
root.left = Node(20)
root.right = Node(30)
root.right.left = Node(40)
root.right.right = Node(50)
print(sizeOfTree(root))



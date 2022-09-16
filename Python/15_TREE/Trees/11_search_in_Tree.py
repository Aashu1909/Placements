class Node:
    def __init__(self,data):
        self.left=None
        self.right=None
        self.key=data
    
def searchInTree(root,x):
    if root==None:
        return False
    elif root.key==x:
        return True
    elif searchInTree(root.left,x)==True:
        return True
    elif searchInTree(root.right,x)==True:
        return True
    else:
        return False

# Driver Code
root = Node(10)
root.left = Node(20)
root.right = Node(30)
root.right.left = Node(40)
root.right.right = Node(50)
print(searchInTree(root,10))



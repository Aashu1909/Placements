class Node:
    def __init__(self,data):
        self.left=None
        self.right=None
        self.key=data

def floorOfBST(root,x):
    res = None
    while root != None:    
        if root.key == x:
            return root
        elif root.key>x:
            root = root.left
        else:
            res = root
            root = root.right
    return res

def iterativeInsertBst(root,key):
    parent=None
    curr=root
    while curr!=None:
        parent=curr
        if curr.key==key:
            return root
        elif curr.key<key:
            curr=curr.right
        else:
            curr=curr.left
    if parent ==None:
        return Node(key)
    elif parent.key>key:
        parent.left=Node(key)
    else:
        parent.right=Node(key)
    return root

def InOrder(root):
    if root!=None:
        InOrder(root.left)
        print(root.key,end=" ")
        InOrder(root.right)


root=None
root=iterativeInsertBst(root,10)
root=iterativeInsertBst(root,15)
root=iterativeInsertBst(root,5)
root=iterativeInsertBst(root,12)
root=iterativeInsertBst(root,18)
root=iterativeInsertBst(root,8)
# Here we are using Inoder traversal because
InOrder(root)
print()
print(floorOfBST(root,20).key)

class Node:
    def __init__(self,data):
        self.left=None
        self.right=None
        self.key=data
    
    # Value greater than or equal to key
def ceilingBst(root,key):
    res=None
    while root!=None:
        if root.key==key:
            return root
        elif root.key<key:
            root=root.right
        else:
            res=root
            root=root.left
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
print(ceilingBst(root,16).key)


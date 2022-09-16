class Node:
    def __init__(self,data):
        self.left=None
        self.right=None
        self.key=data
    
def insertBst(root,key):
    if root==None:
        temp_node=Node(key)
        return temp_node
    elif root.key==key:
        return root
    elif root.key>key:
        root.left=insertBst(root.left,key)
    else:
        root.right=insertBst(root.right,key)
    return root
    
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
root=insertBst(root,10)
root=insertBst(root,15)
root=insertBst(root,5)
root=insertBst(root,12)
root=insertBst(root,18)
root=insertBst(root,8)
# Here we are using Inoder traversal because
# its traversal will always results in a sorted array
InOrder(root)
print()
root1=None
root1=iterativeInsertBst(root1,10)
root1=iterativeInsertBst(root1,15)
root1=iterativeInsertBst(root1,5)
InOrder(root1)
# root=insertBst(root,12)
# root=insertBst(root,18)
# root=insertBst(root,8)


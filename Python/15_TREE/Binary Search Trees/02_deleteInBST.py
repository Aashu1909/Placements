class Node:
    def __init__(self,data):
        self.left=None
        self.right=None
        self.key=data

def getSuccesor(curr,key):
    while curr.left!=None:
        curr=curr.left
    return curr.key
    
def DeleteBst(root,key):
    if root==None:
        temp_node=Node(key)
        return temp_node
    elif root.key>key:
        root.left=DeleteBst(root.left,key)
    elif root.key<key:
        root.right=DeleteBst(root.right,key)
    else:
        # root.key==key
        if root.left==None:
            return root.right
        elif root.right==None:
            return root.left
        else:
            succesor=getSuccesor(root.right,key)
            root.key=succesor
            root.right=DeleteBst(root.right,succesor)
    return root
    
def iterativeDeleteBst(root,key):
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


# root=None
# root=insertBst(root,10)
# root=insertBst(root,15)
# root=insertBst(root,5)
# root=insertBst(root,12)
# root=insertBst(root,18)
# root=insertBst(root,8)
# # Here we are using Inoder traversal because
# # its traversal will always results in a sorted array
# InOrder(root)
# print()
# root1=None
# root1=iterativeInsertBst(root1,10)
# root1=iterativeInsertBst(root1,15)
# root1=iterativeInsertBst(root1,5)
# InOrder(root1)
# # root=insertBst(root,12)
# root=insertBst(root,18)
# root=insertBst(root,8)


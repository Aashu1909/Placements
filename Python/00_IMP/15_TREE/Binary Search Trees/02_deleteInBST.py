import collections
from A_InsertInBST import iterativeInsertInBST,Node

def maximumVal(root):
    if root==None:
        return -10**9
    curr=root
    while curr.right!=None:
        curr=curr.right
    return curr

def minimumVal(root):
    if root==None:
        return 10**9
    curr=root
    while curr.left!=None:
        curr=curr.left
    return curr
      
def DeleteBst(root,val):
    if root==None:
       return root
    # Base Condition
    if root.key==val:
        # 0 Chlid
        if root.right==None and root.left==None:
            return None
        # 1 Clild 
        # Left child None
        if root.right!=None and root.left==None:
            return root.right
        # right chlid None
        if root.left!=None and root.right==None:
            return root.left
        
        # 2 Child
        if root.right!=None and root.left!=None:
            maxi=maximumVal(root.left)
            root.key=maxi.key
            root.left=DeleteBst(root.left,maxi)
            return root
    
    elif root.key>val:
        root.left=DeleteBst(root.left,val)
    else:
        root.right=DeleteBst(root.right,val)

    return root

def levelOrder(root)->None:
    if root==None:
        return None
    queue=collections.deque()
    queue.append(root)
    while len(queue)!=0:
        n=len(queue)
        for _ in range(n):
            node=queue.popleft()
            print(node.key,end=" ")
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        print("")

key=[5,10,20,3,4,7]
root1=None
for i in key:
    root1=iterativeInsertInBST(root1,i)
levelOrder(root1)
root1=DeleteBst(root1,7)
levelOrder(root1)

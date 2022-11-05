import collections
class Node:
    def __init__(self,data):
        self.left=None
        self.right=None
        self.key=data

#O(logn) time  O(H) space    
def insertBst(root,key):
    if root==None:
        temp_node=Node(key)
        return temp_node
    # If Already that root is Present
    if root.key==key:
        return root
    
    if root.key>key:
        root.left=insertBst(root.left,key)
    else:
        root.right=insertBst(root.right,key)
    
    return root

def iterativeInsertInBST(root,d):
    if root==None:
        root=Node(d)
        return root
    parent=None
    curr=root
    while curr!=None:
        parent=curr
        if curr.key==d:
            return curr
        if curr.key>d:
            curr=curr.left
        else:
            curr=curr.right
    if parent.key>d:
        parent.left=Node(d)
    else:
        parent.right=Node(d)
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

def InOrder(root):
    if root!=None:
        InOrder(root.left)
        print(root.key,end=" ")
        InOrder(root.right)


# key=[5,15,20,3,4,7]
# root1=None
# for i in key:
#     # root1=insertBst(root1,i)
#     root1=iterativeInsertInBST(root1,i)
# InOrder(root1)
# levelOrder(root1)


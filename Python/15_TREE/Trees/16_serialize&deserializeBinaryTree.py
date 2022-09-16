from tree import Node,inOrder
'''
Basically serialization means converting the Binary Tree into an array
it takes a node into the tree and put into an array 
and if the root is none it append(-1)
'''
EMPTY=-1
def serialize(root, arr):
    if root==None:
        arr.append(EMPTY)
        return 
    arr.append(root.key)
    serialize(root.left,arr)
    serialize(root.right,arr)
'''
so deserializing means that converting the given string or an array into a the given tree
'''
# Presuming that the tree is in Preorder traversal
def deserialize(arr,index):
    if index==len(arr):
        return None
    data=arr[index]
    index+=1
    if data==EMPTY:
        return None
    node=Node(data)
    node.left=deserialize(arr,index)
    node.right=deserialize(arr,index)
    return node

# Left Root Right   20 10 40 30 50
#    10 
#   /  \
# 20    30
#      /  \
#    40    50
root = Node(10)
root.left = Node(20)
root.right = Node(30)
root.right.left = Node(40)
root.right.right = Node(50)
arr=[]
serialize(root,arr)
root1=deserialize(arr,0)
inOrder(root1)
print(arr)
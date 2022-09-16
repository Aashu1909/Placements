# Here we are first storing the root of the tree in arr in Inorder form
# Inorder traversal using Stack
from tree import Node
# Inorder Traversal in Binary tree
# Left Root Right   20 10 40 30 50
#    10 
#   /  \
# 20    30
#      /  \
#    40    50
def inordertraversal(root):
    stack=[]
    arr=[]
    current=root
    while(current!=None or len(stack)>0):
        # st=[curr.key for curr in stack]
        # print('stack',st)
        # print('current',current.key) if current else print('current',None)
        if current:
            stack.append(current)
            current=current.left
        else:
            current=stack.pop()
            arr.append(current)
            current=current.right
    return arr
    
    
def Conversion_to_DLL(self,root):
    temp=None
    arr=self.inordertraversal(root)
    for i in range(0,len(arr)-1):
        arr[i].left=temp
        arr[i].right=arr[i+1]
        temp=arr[i]
    last=arr.pop()
    last.left=temp
    last.right=None
    arr.append(last)
    return arr

def binaryTreeToDLL(self,root):
    arr=Conversion_to_DLL(root)
    # returning the head
    return arr[0]

root = Node(10)
root.left = Node(20)
root.right = Node(30)
root.right.left = Node(40)
root.right.right = Node(50)
print()
st=[curr.key for curr in inordertraversal(root)]
print(st)




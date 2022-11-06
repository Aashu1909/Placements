# Consider a senario where we need to represent hierarchy
# eg folder structure a company structure how will you represent it in a data structure
# Tree is a Non linear Data structure which stores the data in hierarical Fashion
# Top node in the tree is Root
# Nodes with no children is called leaf nodes
# Desendant of the node is the subtree which contain the node
# Degree is the no of children it has

# Level order Traversal
# Inorder left root right
# Preorder root left right
# postorder left right root
import collections
class TreeNode:
    def __init__(self,data):
        self.left=None
        self.right=None
        self.key=data

def inorder(root):
    if root!=None:
        inorder(root.left)
        print(root.key,end=" ")
        inorder(root.right)

def buildTree(root):
    data=int(input("Enter then Data:"))
    if data==-1:
        return None
    root=TreeNode(data)
    print(f"Enter data to the left of {data}")
    root.left=buildTree(root.left)
    print(f"Enter data to the right of {data}")
    root.right=buildTree(root.right)
    return root

def buildFromLevelOrder(root):
    queue=collections.deque()
    data=int(input("Enter data"))
    if data==-1:
        return None
    root=TreeNode(data)
    queue.append(root)

    while len(queue)!=0:
        temp=queue.popleft()
        print(f"Enter data to left {temp.key}:")
        leftData=int(input())
        if leftData!=-1:
            node=TreeNode(leftData)
            temp.left=node
            queue.append(node)
        print(f"Enter data to right {temp.key}:")
        rightData=int(input())
        if rightData!=-1:
            node=TreeNode(rightData)
            temp.right=node
            queue.append(node)
    return root
        
root=None
# root=buildTree(root)
root1=buildFromLevelOrder(root)
print("Inorder")
# inorder(root)
inorder(root1)
      
    


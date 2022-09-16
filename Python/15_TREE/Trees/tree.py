# Consider a senario where we need to represent hierarchy
# eg folder structure a company structure how will you represent it in a data structure
# Tree is a Non linear Data structure which stores the data in hierarical Fashion
# Top node in the tree is Root
# Nodes with no children is called leaf nodes
# Desendant of the node is the subtree which contain the node
# Degree is the no of children it has


# Inorder left root right
# Preorder root left right
# postorder left right root
class Node:
    def __init__(self,data):
        self.left=None
        self.right=None
        self.key=data

def inOrder(root):
    if root!=None:
        inOrder(root.left)
        print(root.key)
        inOrder(root.right)        
    


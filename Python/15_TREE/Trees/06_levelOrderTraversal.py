from collections import deque
from itertools import count
class Node:
    def __init__(self,data):
        self.left=None
        self.right=None
        self.key=data
        
# 10 20 30 40 50
#    10 
#   /  \
# 20    30
#      /  \
#    40    50
# T(n) O(number of nodes) 
# Tn O(N) space theta(n)
def levelOrderTraversal(root):
    if root==None:
        return None
    queue=deque()
    queue.append(root)
    while len(queue)!=0:
        node=queue.popleft()
        print(node.key,end=" ")
        if node.left!=None:
            queue.append(node.left)
        if node.right!=None:
            queue.append(node.right)
# Line by Line
def levelOrderTraversalLineByLine(root):
    if root==None:
        return None
    queue=deque()
    queue.append(root)
    queue.append(None)
    while len(queue)>1:
        node=queue.popleft()
        
        if node==None:
            print()
            queue.append(None)
            continue

        print(node.key,end=" ")
        if node.left!=None:
            queue.append(node.left)
        if node.right!=None:
            queue.append(node.right)
    
# Method 2 line by line
def levelOrderTraversalLineLine(root):
    if root==None:
        return None
    queue=deque()
    queue.append(root)
    print(queue)
    while len(queue)>0:
        count=len(queue)
        for _ in range(count):
            node=queue.popleft()
            print(node.key,end=" ")
            if node.left!=None:
                queue.append(node.left)
            if node.right!=None:
                queue.append(node.right)
        print()
    


# Driver Code
root = Node(10)
root.left = Node(20)
root.right = Node(30)
root.right.left = Node(40)
root.right.right = Node(50)
# levelOrderTraversal(root)
# levelOrderTraversalLineByLine(root)
levelOrderTraversalLineLine(root)



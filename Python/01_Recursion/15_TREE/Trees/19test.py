from this import d


class Node:
    def __init__(self,d) -> None:
        self.data=d
        self.left=self.right=None

def solve(root):
    if root==None:
        return 
    print(root.data)
    solve(root.right)
    solve(root.right)

root = Node(3)
root.left = Node(4)
root.right = Node(5)
# root.right.left = Node(30)
root.right.right = Node(6)
print(solve(root))
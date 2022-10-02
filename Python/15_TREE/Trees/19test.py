from a_TREE import Node
def inorder(root,r,sm):
    if root==None and r<=0:
        return 
    if root.left:
        inorder(root.left,r-1,sm)
    sm+=(root.key)
    print(sm,r)
    # r-=1
    if root.right:
        inorder(root.right,r-1,sm)

def summ(root, k):
    # code here
    r=k
    sm=0
    inorder(root,r,sm)
    print(sm)
    # return sum(ans)

root = Node(20)
root.left = Node(10)
root.right = Node(40)
root.right.left = Node(30)
root.right.right = Node(50)
print(summ(root,3))
# Method 1 o(n^2) time 
# here we are calling the height function for every node in the tree which results in the o(n^2)
def height(root):
    if root==None:
        return 0
    return 1+max(height(root.right),height(root.left))

def isbalanced(root):
    if root==None:
        return True
    left_height=height(root.left)
    right_height=height(root.right)
    return (abs(right_height-left_height)<=1) and isbalanced(root.left) and isbalanced(root.right)

# Method 2 time o(n)
# In this method we have basically modified the height funtion 
def isbalanced2(root):
    if root==None:
        return 0
    leftHeight=isbalanced2(root.left)
    if leftHeight==-1:
        return -1
    rightHeight=isbalanced2(root.right)
    if rightHeight==-1:
        return -1
    if abs(leftHeight-rightHeight)>1:
        return -1
    return max(leftHeight,rightHeight)+1
class Node:
    def __init__(self,d):
        self.data=d
        self.left=None
        self.right=None
        
class Solution:
    def solve(self,inorder,preorder,index):
        if inorder:
            idx=inorder.index(preorder[index])
            index+=1
            root=Node(inorder[idx])
            root.left=self.solve(inorder[:idx],preorder,index)
            root.right=self.solve(inorder[idx+1:],preorder,index)
            return root
        else:
            return None
    
    def checkPostorder(self,root,postorder,index):
        if root==None:
            return index
        index=self.checkPostorder(root.left,postorder,index)
        index=self.checkPostorder(root.right,postorder,index)
        if root.data==postorder[index]:
            index+=1
        else:
            return -1
        return index

    def checktree(self, preorder, inorder, postorder, N): 
        # Your code goes here
        self.inMap={inorder[i]:i for i in range(len(inorder))}
        root1=self.solve(preorder,inorder,0)
        temp=self.checkPostorder(root1,postorder,0)
        return temp==N
    
N = 5
preorder =[1, 5, 4, 2, 3]
inorder = [4, 2, 5, 1, 3]
postorder = [4, 1, 2, 3, 5]
obj=Solution()
print(obj.checktree(preorder,inorder,postorder,N))
q
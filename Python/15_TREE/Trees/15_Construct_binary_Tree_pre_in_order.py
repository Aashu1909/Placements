# Construct a binary tree using preorder or post order
class TreeNode:
    def __init__(self,data) -> None:
        self.data=data
        self.left=None
        self.right=None


class Solution:
    def search(self,inorder,ele):
        return inorder.index(ele)
    

    def solve(self,inorder,preorder,inStart,inEnd,index):
        if index>=len(inorder) or inStart>inEnd:
            return None
        element=preorder[index]
        index+=1
        root=TreeNode(element)
        idx=self.search(inorder,element)
        root.left=self.solve(inorder,preorder,inStart,idx-1,index)
        root.right=self.solve(inorder,preorder,idx+1,inEnd,index)
        return root
    
    def buildtree(self, inorder, preorder, n):
        # code here
        # build tree and return root node
        return self.solve(inorder,preorder,0,n-1,0)
    
    def solve1(self,inorder,preorder,index):
        if inorder:
            idx=inorder.index(preorder[index])
            index+=1
            root=TreeNode(inorder[idx])
            root.left=self.solve1(inorder[:idx],preorder,index)
            root.right=self.solve1(inorder[idx+1:],preorder,index)
            return root 

    def postorder(self,root):
        if root!=None:
            self.postorder(root.left)
            self.postorder(root.right)
            print(root.data,end=" ")

inorder = [1 ,6 ,8 ,7]
preorder = [1 ,6 ,7 ,8]
n=len(inorder)
obj=Solution()
root=obj.solve1(inorder,preorder,0)
obj.postorder(root)
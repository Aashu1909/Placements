class Solution:
    #Function to return the lowest common ancestor in a Binary Tree.
    def findpath(self,root,path,n):
        if root==None:
            return False
        path.append(root)
        if root.data==n:
            return True
        left=self.findpath(root.left,path,n)
        right=self.findpath(root.right,path,n)
        if left or right: 
            return True
        path.pop()
        return False
    
    def lca(self,root, n1, n2):
        # Code here
        # TN O(2N) time O(2N) 
        path1=[]
        path2=[]
        if self.findpath(root,path1,n1)==False or self.findpath(root,path2,n2)==False:
            return None
        i=0
        while i<len(path1) and i<len(path2):
            if path1[i].data!=path2[i].data:
                break
            i+=1
        return path1[i-1]
        
    def lca_recursion(self,root,n1,n2):
        #  TN O(N) time O(N) 
        if root==None:
            return None
        if root==n1 or root==n2:
            return root
        left=self.lca_recursion(root.left,n1,n2)
        right=self.lca_recursion(root.right,n1,n2)
        if left!=None and right!=None:
            return root.data
        elif left==None and right!=None:
            return right
        elif left!=None and right==None:
            return left
        elif left==None and right==None:
            return None
    
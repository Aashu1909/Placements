"""
First approach 
1 Do the inorder traversal of the binary search tree
2 Then find the pair using two pinter approach
"""

'''
Second approach
we initialise a set which contain root in it and 
we do an inorder traversal and check if the sum-root.data exists or not 
'''
def pair_sum(root,sm,hashset):
    if root==None:
        return False
    
    if pair_sum(root.left,sm,hashset):
        return True
    
    if (sm-root.data) in hashset:
        return True
    else:
        hashset.add(root.data)
    
    return pair_sum(root.right,sm,hashset)

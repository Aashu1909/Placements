
def search_in_bst(root,element):
    if root==None:
        return False
    if root.key==element:
        return True
    elif root.key<element:
        return search_in_bst(root.right,element)
    else:
        return search_in_bst(root.left,element)


def iteratrive_search_bst(root,element):
    while root!=None:
        if root.key==element:
            return True
        if root.key<element:
            root=root.right
        else:
            root=root.left
    
    return False
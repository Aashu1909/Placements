# Cloning is the process of creating a copy linked list of the given ll
# Method 1 hashing
# We crate n nodes ll and create a hashmap to link the nodes with random pointer with each other

class node:
    def __init__(self,data):
        self.data=data
        self.next=None

def randomClone(head):
    hashmap={None:None}
    curr=head
    
    while curr!=None:
        copyNode=node(curr.val)
        hashmap[curr]=copyNode
        curr=curr.next
    curr=head
    # using the hashtable we can put the value of the hash
    while curr!=None:
        copyNode=hashmap[curr]
        copyNode.next=hashmap[curr.next]
        copyNode.random=hashmap[curr.random]
        curr=curr.next
    return hashmap[head]

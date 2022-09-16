# It uses doubly linked list internally
# A dequeue can be used as both Stack and Queue
# A-Steal Process scheduling algorithm 
# Helps in implementing Priority Queue,ie insert an item with priority 1
# in the front and others at rear which have different priority
from collections import deque
d=deque()
d.append(10) #[10]
d.append(20) #[10,20]
d.append(30) #[10,20,30]
# appendleft inserts the element in front ie left of the end.
d.appendleft(40) #[40,10,20,30]
print(d)
d.pop() #remove item from the rear ie end of deque
d1=deque([10,20,30,40])
# Insert funtion in deque=d.insert(index,value)
d1.insert(2,10)#[10,20,10,30,40]
d1.extend([50,60])#[10,20,10,30,40,50,60]
d1.extendleft([5,6])#[5,6,10,20,10,30,40,50,60]
d1.remove(10)
d1.rotate(2)#this function rotate the deque clockwise the number of times specdified
d1.reverse() #reverses the deque
# Slicing is not allowed with Dequeue
# Time complexities 
# O(1)-append() appendleft() pop() popleft()
# O(N)- d[i] (accesing an element), count(x) ,insert(index,element)
# Theta(N)-rotate(abs(r))
# Theta(len(l))- extendleft(l),extend(l)

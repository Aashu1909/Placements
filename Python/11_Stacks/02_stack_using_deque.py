# Stack can alse be implemented using DEQUE Doubly ended queue Data stucture in Python
# Here Ppush Operation can be performed by Append 
# POP operation can be performed by pop op in deque

import collections
stack=collections.deque()
stack.append(10)
stack.append(20)
stack.append(30)
print(stack)
stack.pop()
print(stack)
stack.pop()
print(stack)
stack.pop()
print(stack)

# There is one more way to implement Stack in python using LastInFirstOut Queue
 
import queue
stack=queue.LifoQueue()  # here Inside we can give the maximum lenght 
# here for PUSH operation we use PUT 
# and for POP we use GET
stack.put(10)
stack.put(20)
stack.put(30)
print(stack.get())
print(stack.get())
print(stack.get())
# And if the stack got empty this method will search for an object
# to remove that we need to use timeout functionality 
print(stack.get(timeout=1))
# now the stack 

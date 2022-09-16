# From Deque Class in Collection 
import collections
queue1=collections.deque()
queue1.appendleft(10)
queue1.appendleft(20)
queue1.appendleft(30)
# for removing use pop method 
queue1.pop()
queue1.pop()
queue1.pop()

import queue
queue2=queue.Queue()
queue2.put(10)
queue2.put(20)
queue2.put(30)
# For removing the Element
queue2.get()
queue2.get()
queue2.get()

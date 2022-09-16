# Design a data structure that support following ops in O(1)-T(N)
# insertMin(x) insertMax(x)
# getMin(x) getMax(x)
# extractMin(x) extractMax(x)
# Here the idea is to use DEQUE data structure
from collections import deque

class MyDataStructure:
    
    def __init__(self):
        self.dq=deque()
    
    def insertMin(self,data):
        self.dq.appendleft(data)

    def insertMax(self,data):
        self.dq.append(data)
    
    def getMin(self):
        return self.dq[0]

    def getMax(self):
        return self.dq[0]
    
    def extractMin(self):
        return self.dq.pop(0)
    
    def extractMax(self):
        return self.dq.pop()
    
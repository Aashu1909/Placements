# Circular list implementation
# of Queue
class Queue:
    def __init__(self,capacity):
        self.list=[None]*capacity
        self.capacity=capacity
        self.front=0
        self.size=0

    # Class Methods
    def getFront(self):
        if self.size == 0:
            return None
        else:
            return self.list[self.front]

    def getRear(self):
        if self.size == 0:
            return None
        else:
            rear = (self.front + self.size - 1) % self.capacity
            return self.list[rear]

    def enque(self, x):
        if self.size == self.capacity:
            return
        else:
            rear = (self.front + self.size - 1) % self.capacity
            rear = (rear + 1) % self.capacity
            self.l[rear] = x

            self.size = self.size + 1

    def deque(self):
        if self.size == 0:
            return None
        else:
            res = self.l[self.front]
            self.front = (self.front + 1) % self.capacity
            self.size = self.size - 1
        return res
        
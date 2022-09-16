class Stack:
    def __init__(self):
        self.stack = []

    def isEmpty(self):
        return len(self.stack) == 0

    def top(self):
        if self.isEmpty():
            return False
        return self.stack[-1]


    def push( self, item ):
        self.stack.append(item)


    def pop(self):
        if(self.isEmpty()):
            print("Stack Underflow ")
            exit(1)
        return self.stack.pop()
    
    def size(self):
        return len(self.stack)
    
    def print(self):
        for i in range(len(self.stack)-1, -1, -1):
            print(self.stack[i], end = ' ')
        print()

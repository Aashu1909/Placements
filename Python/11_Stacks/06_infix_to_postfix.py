# Python program to convert infix expression to postfix
# Class to convert the expression

class Conversion:
    # Constructor to initialize the class variables
    def __init__(self, capacity):
        self.top = -1
        self.capacity = capacity
        self.array = []
        # Precedence setting
        self.output = []
        self.precedence = {'+':1, '-':1, '*':2, '/':2, '^':3}
    
    # check if the stack is empty
    def isEmpty(self):
        return True if self.top == -1 else False
    
    # Return the value of the top of the stack
    def peek(self):
        return self.array[-1]
    
    # Pop the element from the stack
    def pop(self):
        if not self.isEmpty():
            self.top -= 1
            return self.array.pop()
        else:
            return "$"
    
    # Push the element to the stack
    def push(self, op):
        self.top += 1
        self.array.append(op)
    
    # A utility function to check is the given character is operand
    def isOperand(self, ch):
        return ch.isalpha()
    
    # Check if the precedence of operator is strictly less than top of stack or not
    def notGreater(self, i):
        try:
            a = self.precedence[i]
            b = self.precedence[self.peek()]
            return True if a  <= b else False
        except KeyError:
            return False

    def infixToPostfix(self, exp):








# time.sleep(1)
# end=time.time()
# print(f"Total Time Taken:{end-begin}")
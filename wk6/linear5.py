class Stack:
    
    def __init__(self):
        self.array = []
    
    def push(self, item):
        self.array.append(item)
        
    def pop(self):
        if len(self.array) > 0:
            last = self.array[-1]
            self.array.pop()
            return last
        else:
            print("Stack is empty")
    
    def peek(self):
        if len(self.array) == 0:
            print("Stack is empty")
        else:
            return self.array[-1]
    
    def count(self):
        return len(self.array)
        
    def display(self):
        print(str(self.array) + " <= top")


def factorial1(n):
    if n == 1:
        return 1
    return n*factorial1(n-1)

def factorial(n):
    s = Stack()
    s.push(n)
    n -= 1
    while n != 0:
        s.push(s.peek()*n)
        n -= 1
    return s.peek()

print(factorial1(5))
print(factorial(5))
print(factorial1(10))
print(factorial(10))
print(factorial1(3))
print(factorial(3))
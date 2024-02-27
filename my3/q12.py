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

def power4(x, n):
    s = Stack()
    s.push(n)
    result = 1
    while s.count() > 0:
        s.display()
        current = s.pop()
        if current > 0:
            result *= x
            s.push(current-1)
    return result

print(power4(3, 5))
    
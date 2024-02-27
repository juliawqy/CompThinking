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


def pt(n, k):
    if k == 1 or k == n+1:
        return 1
    else:
        return pt(n-1,k) + pt(n-1, k-1)

def stk_pt(n, k):
    s = Stack()
    if k > n:
        k = n+2-k
    # s.push(1)
    while n > 1:
        for i in range(k):
            s.push(1)
        n -= 1
        k -= 1
    sum = 0
    while s.count()>0:
        sum += s.pop()
    return sum

def stk_pt_ans(n, k):
    s = Stack() #Step (1)
    s.push(n) #Step (2)
    s.push(k) #Step (2)
    result = 0 #Step (3)
    while s.count() > 0: #Step (4)
        k = s.pop() #Step (5)
        n = s.pop() #Step (5)
        if k == 1 or k == n+1: #Step (6)
            result += 1 #Step (6)
        else:
            s.push(n-1)
            s.push(k)
            s.push(n-1)
            s.push(k-1)
    return result

print(pt(4, 3))
print(stk_pt_ans(4, 3))
print(pt(5, 5))
print(stk_pt_ans(5, 5))
print(pt(6, 7))
print(stk_pt_ans(6, 7))

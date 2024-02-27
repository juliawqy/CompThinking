def func3(A):
    n = len(A)
    if n == 1:
        return A[0]
    elif A[n-1] > A[0]:
        return A[n-1]
    elif n == 2:
        return A[0]
    x = A[0:n//2]
    y = A[n//2:n-1]
    while len(x) > 1 or len(y) > 1: 
        if x[0] > y[0]:
            return func3(x)
        else:
            return func3(y)

A = [6, 19, 30, 31, 33, 47, 57, 60]
A1 = [60, 6, 19, 30, 31, 33, 47, 57]
A3 = [47, 57, 60, 6, 19, 30, 31, 33]

print(func3(A))
print(func3(A1))
print(func3(A3))
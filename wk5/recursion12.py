def power(x,n):
    if n == 0:
        return 1
    if n == 1:
        return x
    return x * power(x, n-1)

def f12_rec(x, n):
    if n == 1:
        return 1/power(x,n)
    else:
        return 1/power(x,n) + f12_rec(x,n-1)
    
print(f12_rec(2,4))
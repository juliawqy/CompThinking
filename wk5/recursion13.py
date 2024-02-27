def f13_rec(x,y,n):
    # if n%2 == 0:
    #     if n == 0:
    #         return 0
    #     else:
    #         return y*n + x*(n-1) + f13_rec(x, y, n-2)
    # else:
    #     if n == 1:
    #         return x
    #     else:
    #         return x*n + y*(n-1) + f13_rec(x, y, n-2)
        
    if n == 1:
        return x
    else:
        if n%2 == 0:
            return y*n + f13_rec(x, y, n-1)
        else:
            return x*n + y*(n-1) + f13_rec(x, y, n-2)
    
print(f13_rec(4, 3, 5))
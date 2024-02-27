def max_array(a):
    if len(a) == 1:
        return a[0]
        
    if max_array(a[0:len(a)//2]) > max_array(a[len(a)//2:len(a)]):
        return max_array(a[0:len(a)//2])
    else:
        return max_array(a[len(a)//2:len(a)]) #oi wtf u damn lame eh fking forgot the return >:()




a = [12, 15, 2, 17, 87, 3]
print(max_array(a))
b = [72, 5, 27, 70, 827, 103]
print(max_array(b))
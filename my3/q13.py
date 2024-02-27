def mirror(s):
    if len(s) == 1:
        return s+s
    else:
        return s[0] + mirror(s[1:len(s)]) + s[0]
    
print(mirror("abbc"))
print(mirror("xyz"))

def mystery (x):
    s = []
    out = 0
    if x%2 == 1:
        s.append(0)
    while x > 1:
        s.append(x//2)
        x = x//2
    print(s)
    for i in range(0, len(s)):
        out += 10**s[i]
    return out

print(mystery(3))
print(mystery(5))
print(mystery(6))
print(mystery(7))
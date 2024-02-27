def euclid1(a, b):
    while b != 0: 
        t = b
        b = a % b 
        a = t
    return a

def euclid(a,b):
    if b == 0:
        return a
    return euclid(b, a%b)

print(euclid1(9,3))
print(euclid1(9,6))
print(euclid1(8,4))
print(euclid1(8,5))

print(euclid(9,3))
print(euclid(9,6))
print(euclid(8,4))
print(euclid(8,5))
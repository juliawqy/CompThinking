def isSorted_ans(a):	# a is a list of integers

    n = len(a)
    for i in range(n-1): 
        if a[i] > a[i+1]:
            return False

    return True

def isSorted(a):
    if len(a) == 1:
        return True
    return a[0] < a[1] and isSorted(a[1:])


a = [1, 2, 3, 4, 5]
b = [2, 3, 4, 5, 6, 7, 8]
c = [4, 2, 4, 1, 5, 9]
a = []

print(isSorted_ans(a))
print(isSorted(a))
print(isSorted_ans(b))
print(isSorted(b))
print(isSorted_ans(c))
print(isSorted(c))
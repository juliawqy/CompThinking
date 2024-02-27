def reverse(a):
    if len(a) == 1:
        return [a[0]]
    else:
        return [a[-1]] + reverse(a[0:-1])


a = [1, 2, 3, 4, 5]
print(reverse(a))
print(a[0:-1])
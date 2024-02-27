a = [2, 5, 6, 2, 7, 3, 9, 2, 0, 3]

def search1(a,k):
    count = 0
    for i in range(len(a)):
        if a[i] == k:
            count += 1
    return count

def search2(a,k):
    count = 0
    for i in range(len(a)):
        if count <= 1:
            if a[i] == k:
                count += 1
        if count == 2:
            return i
    return None

def search3(a,k):
    for i in range(len(a)-1, -1, -1):
        if a[i] == k:
            return i
    return None

print(search1(a,5)) #3
print(search2(a,5)) #3
print(search3(a,5)) #7
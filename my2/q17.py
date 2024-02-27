def fmp_ans(sequence):
    product = 0
    n = len(sequence)
    index_1 = 0
    for i in range(1, n):
        if sequence[i] > sequence[index_1]:
            index_1 = i
    index_2 = 0
    for i in range(1, n):
        if i != index_1 and sequence[i] > sequence[index_2]:
            index_2 = i
    product = sequence[index_1] * sequence[index_2]
    return(product)

def fmp(sequence):
    highest = 0
    next = 0
    for num in sequence:
        if num > next:
            if num > highest:
                next = highest
                highest = num
            else:
                next = num
    
    return highest*next

a = [5, 6, 2, 7, 4]
b = [5, 6, 2, 8, 4, 10]

print(fmp_ans(a))
print(fmp(a))
print(fmp_ans(b))
print(fmp(b))
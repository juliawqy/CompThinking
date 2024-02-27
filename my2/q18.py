def search_ans(nums, target): 
    lower = 0
    upper = len(nums) - 1

    while lower <= upper:
        mid = (lower + upper) // 2

        if nums[mid] == target :
            return mid
        if nums[mid] >= nums[lower] :
            if nums[lower] <= target and target < nums[mid]: 
                upper = mid - 1
            else:
                lower = mid + 1
        else:
            if nums[mid] < target and target <= nums[upper]: 
                lower = mid + 1
            else:
                upper = mid - 1
    return -1

def search(nums, target): 
    lower = 0
    upper = len(nums) - 1

    while lower <= upper:
        mid = (lower + upper) // 2

        if target == nums[mid] :
            return mid
        if nums[mid] > nums[mid-1] :
            if target >= nums[lower] and target < nums[mid]: 
                upper = mid - 1
            else:
                lower = mid + 1
        else:
            if target > nums[mid] and target <= nums[upper]: 
                lower = mid + 1
            else:
                upper = mid - 1
    return -1

a = [4, 5, 6, 0, 1, 2, 3]
b = [5, 6, 0, 1, 2, 3, 4]
c = [6, 0, 1, 2, 3, 4, 5]
d = [0, 1, 2, 3, 4, 5, 6]
e = [1, 2, 3, 4, 5, 6, 0]
f = [2, 3, 4, 5, 6, 0, 1]
g = [3, 4, 5, 6, 0, 1, 2]

print(search_ans(a, 5))
print(search(a, 5))
print(search_ans(b, 5))
print(search(b, 5))
print(search_ans(c, 5))
print(search(c, 5))
print(search_ans(d, 5))
print(search(d, 5))
print(search_ans(e, 5))
print(search(e, 5))
print(search_ans(f, 5))
print(search(f, 5))
print(search_ans(g, 5))
print(search(g, 5))


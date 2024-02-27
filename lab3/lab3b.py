# Name:    julia
# Section: g1

# All statements should only be in functions.

# Takes in a base-10 integer and returns the base-2 (binary) equivalent as a string
# this function does NOT have to handle negative numbers (i.e. d will always be >=0)
# this function must NOT use Python's bin() function.
# this function must be recursive (i.e. it calls itself)
# there should not be leading zeros in the string that this function returns.

# int method:
# def to_binary(d):

#     if d == 0:
#         return 0
#     elif d == 1:
#         return 1
#     else:
#         return to_binary(d//2)*10 + to_binary(d%2)

def to_binary(d):

    if d == 0:
        return "0"
    elif d == 1:
        return "1"
    else:
        return to_binary(d//2) + to_binary(d%2)
    



# Name:    julia
# Section: g1

# All statements should only be in functions.
# Takes in an integer and returns the sum of all its digits as an integer
# this function does NOT have to handle negative numbers (i.e. i will always be >=0)
# this function must be recursive (i.e. it will call itself)

def sum_of_digits(i):
  
    if i == 0:
        return 0
    else:
        return i%10 + sum_of_digits(i//10)

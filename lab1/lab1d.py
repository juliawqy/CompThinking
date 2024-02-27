# Filename: lab1d.py
# Name:    julia
# Section: g1

# lab1d (Binary/Stein's algo)

# All statements should only be in functions.
def gcd_d(x, y):
  # TODO: Edit this function

  k = 0

  while x%2 == 0 and y%2 == 0:
    x = x/2
    y = y/2
    k += 1
  
  while not x == y:
    if x%2 == 0:
      x = x/2
    elif y%2 == 0:
      y = y/2
    elif x > y:
      x = (x-y)/2
    else:
      y = (y-x)/2

  return x*(2**k)
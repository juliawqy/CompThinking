# Filename: lab1a.py
# Name:    julia
# Section: g1

# lab1a (Brute force)

# All statements should only be in functions.
def gcd_a(x, y):
  # TODO: Edit this function
  t = min(x,y)
  while not x%t == 0 or not y%t == 0:
    t -= 1
  return t
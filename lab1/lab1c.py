# Filename: lab1c.py
# Name:    julia
# Section: g1

# lab1c (Euclid's algo)

# All statements should only be in functions.
def gcd_c(x, y):
  # TODO: Edit this function

  while not y == 0:
    t = y
    y = x%y
    x = t

  return x
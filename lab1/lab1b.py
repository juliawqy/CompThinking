# Filename: lab1b.py
# Name:    julia
# Section: g1

# lab1b (Dijkstra's algo)

# All statements should only be in functions.
def gcd_b(x, y):
  # TODO: Edit this function
  while not x == y:
    if x > y:
      x -= y
    else:
      y -= x

  return x
# my_list is a list of strings
def mystery(my_list):
  if len(my_list) == 1:
    return my_list[0] # only element in list
  else:
    f = my_list.pop(0) #.pop() returns the removed element
    return f + mystery(my_list)
  
print(mystery(["a", "b", "c"]))

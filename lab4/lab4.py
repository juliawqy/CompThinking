# Name:    julia
# Section: g1

# All statements should only be in functions.

def select_tweeters(followers):
  
  r_list = []
  follower_dict = {}
  unique_audience = []

  for i in range(len(followers)):
    follower_dict[i] = followers[i]

  print(follower_dict)
  # sorted_dict = sorted(follower_dict.items(), key=lambda x:len(x[1]), reverse=True)
  # print(sorted_dict)

  while len(r_list) < 5:
    sorted_dict = sorted(follower_dict.items(), key=lambda x:len(x[1]), reverse=True)
    print(sorted_dict)
    r_list.append(sorted_dict[0][0])
    for user in sorted_dict[0][1]:
      if user not in unique_audience:
        unique_audience.append(user)
      for keys in follower_dict.keys():
        if user in follower_dict[keys]:
          follower_dict[keys].remove(user)
        if sorted_dict[0][0] in follower_dict[keys]:
          follower_dict[keys].remove(sorted_dict[0][0])
    follower_dict[sorted_dict[0][0]] = []

  return r_list


# Name:    julia
# Section: g1

# All statements should only be in functions.

def perform_once_2b(employee_with_birthyear_list):
  # do nothing
    employee_with_birthyear_list.sort(key=lambda x: x[1])
    return employee_with_birthyear_list

# TODO:
# Write a function called get_IDs_with_birthyear that takes in a year (as an integer) and a list (employee_with_birthyear_list)
# It then returns a list of employee IDs (integers) that have matching birthyears.
def get_IDs_with_birthyear(year, employee_with_birthyear_list):
  # for now, this function always returns an empty list
    n = len(employee_with_birthyear_list)
    check = (n-1)//2

    r_list = []

    while not (employee_with_birthyear_list[check][1] == year):
        if employee_with_birthyear_list[check][1] > year:
            employee_with_birthyear_list = employee_with_birthyear_list[:check]
            n = check
        elif employee_with_birthyear_list[check][1] < year:
            employee_with_birthyear_list = employee_with_birthyear_list[check+1:]
            n = len(employee_with_birthyear_list)
        if n == 0:
            return r_list
        check = (n-1)//2

    i = check
    while i < n and employee_with_birthyear_list[i][1] == year:
        r_list.append(employee_with_birthyear_list[i][0])
        i += 1

    j = check-1
    while j > -1 and employee_with_birthyear_list[j][1] == year:
        r_list.append(employee_with_birthyear_list[j][0])
        j -= 1

    return r_list
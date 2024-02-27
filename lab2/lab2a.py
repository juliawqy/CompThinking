# Name:    julia
# Section: g1

# All statements should only be in functions.

def perform_once_2a(employee_list):
  # do nothing



    return employee_list

# returns True if the id is found in employee_list, and False otherwise.
def exist(id, employee_list):
    # TODO: Replace this function's body with a more efficient search algorithm.

    n = len(employee_list)
    check = (n-1)//2

    while n > 0:
        if employee_list[check] == id:
            return True
        elif employee_list[check] > id:
            employee_list = employee_list[:check]
            n = check
        else:
            employee_list = employee_list[check+1:]
            n = len(employee_list)
        check = (n-1)//2

    return False
# EXTRACT THIS CODE & SUBMIT AS lab0a.py TO eLearn!!!
# Filename: lab0a.py
# Name:    Qian Yu Wong
# Section: G1

# All statements should only be in functions. Do not include statements outside functions in this file.

def admit(sex,age):
  
    if sex == "M" and age >= 23:
        return True
    elif sex == "F" and age >= 18:
            return True

    return False
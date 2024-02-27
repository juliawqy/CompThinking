# EXTRACT THIS CODE & SUBMIT AS lab0b.py TO eLearn!!!
# Filename: lab0b.py
# Name:    Qian Yu Wong
# Section: G1

# All statements should only be in functions. Do not include statements outside functions in this file.
# fill up the weight_category method to return either "underweight", "overweight" or "normal"
# depending on the height (in cm) and weight (in kg)

def weight_category(weight, height):
  
    heightm = height/100
    bmi = weight/(heightm*heightm)
    if bmi < 18.5:
        return "underweight"
    elif bmi <= 25:
        return "normal"
    else:
        return "overweight"
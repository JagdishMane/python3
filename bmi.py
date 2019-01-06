#!/usr/bin/env python3.6

# BMI = (weight in kg/ heigh in meter squared)
# Imperial version: BMI * 703


def gather_info():
    height = float(input("what is you height (inches or meters) "))
    weight = float(input("what is you weight (ponds or kilograms) "))
    system = input("Are your measurments in metric or imperial units ? ").lower().strip()
    return (height, weight, system)

def cal_bmi(weight, height, system='metric'):
    """
    Return the body mass index (BMI) for the
    given weight, height, and mesaurment system.
    """
    if system == 'metric':
        bmi = (weight / (height ** 2))
    else:
        bmi = 703 * (weight / (height ** 2))
    return bmi


while True:
    height, weight, system = gather_info()
    if system.startswith('i'):
        bmi = cal_bmi(weight, system=system, height=height)
        print(f"Your BMI is {bmi}")
        break
    elif system.startswith('m'):
        bmi = cal_bmi(weight, height)
        print(f"Your BMI is {bmi}")
        break
    else:
        print(f"Error: Unknown measurment system, Please enter 'metric' or 'imperial'")





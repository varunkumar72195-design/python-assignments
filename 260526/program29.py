#Write a Python Program to calculate your Body Mass Index.
def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    return bmi
weight = float(input("Enter your weight in kilograms: "))
height = float(input("Enter your height in meters: "))
bmi = calculate_bmi(weight, height)
print("Your Body Mass Index (BMI) is:", bmi)

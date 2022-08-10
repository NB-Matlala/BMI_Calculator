
# 29331900 NB MATLALA
# Practical 6_WS

import math
print("BMI Calculator:")
print(" ")
print("""1. Weight in Pounds, Height in Inches.
2. Weight in Kilograms, Height in Meters.""")
print(" ")
user_typ= int(input("Choice: "))
print(" ")

if user_typ==1:
    weight = float(input("Weight in Pounds?: "))
    print(" ")
    height = float(input("Height in Inches?: "))
    bmi = weight/(pow(height,2)) * 703
    word_wei = "pounds"
    word_hei = "inches"

elif user_typ==2:
    weight = float(input("Weight in Kilograms?: "))
    print(" ")
    height = float(input("Height in Meters?: "))
    bmi = weight/(pow(height,2))
    word_wei = "kilograms"
    word_hei = "meters"
if bmi >29:
    stat = "Obese"
elif bmi <29 and bmi >25:
    stat = "Overweight"
elif bmi <25 and bmi >18.5:
    stat = "Normal"
elif bmi <18.5:
    stat = "Underweight"

print(" ")
print("Results: \n===============================")
print(" ")
print(f"Weight:         {weight} {word_wei}  ")
print(f"Height:         {height} {word_hei}")
print(f"BMI:            {round(bmi,1)}  ")
print(f"Status:         {stat}  ")
print("\n===============================\nEnd.")

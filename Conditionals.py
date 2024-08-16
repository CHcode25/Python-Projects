height = float(input("What is your height:"))
weight = float(input("What is your weight:"))
bmi2 = weight /(height ** 2)
print("Your BMI is", round(bmi2, 2))

if (bmi2 <= 18.5):
    classification = "Underweight"
elif (bmi2 > 18.5 and bmi2 <= 24.9):
    classification = "Normal weight"
elif ( bmi2 > 24.9 and bmi2 <= 29.9):
    classification = "Overweight"
else:
    classification = "Obseity"
    
print("The classification of your BMI is:", classification)
   

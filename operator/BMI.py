weight_in_kg=int(input("Weight in kg:"))

height_in_cm=int(input("Height in cm:"))

height_in_metre=height_in_cm/100

BMI=weight_in_kg/height_in_metre**2 #** ==> exponent

BMI=round(BMI,2)

print("BMI:",BMI)


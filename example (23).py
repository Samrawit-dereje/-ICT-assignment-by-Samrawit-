def calculate_bmi():
    weight = float(input("Enter your weight in kg: "))
    height = float(input("Enter your height in meters: "))
    
    bmi = weight / ( height ** 2 )
    bmi = round (bmi, 2)
    
    if bmi < 18.5:
        category = "Underweight"
    elif bmi < 25:
        category = "Normal weight"
    elif bmi < 30:
        category = "=Overweight"
    else:
        category = "Obese"
    
    print("Your BMI is", bmi, "and you are ", category)

calculate_bmi()

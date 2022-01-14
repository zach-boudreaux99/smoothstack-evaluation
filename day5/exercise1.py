def bmi():
    num_calculations = int(input("How many BMIs do you want to calculate?"))
    result = ""
    while (num_calculations > 0):
        weight = input("What is your weight (kg)?")
        height = input("What is your height (m)?")
        bmi = float(weight) / (float(height) ** 2)
        
        if bmi < 18.5:
            result += "underweight "
        elif bmi < 25.0 and bmi >= 18.5:
            result += "normal "
        elif bmi < 30.0 and bmi >= 25.0:
            result += "overweight "
        elif bmi >= 30.0:
            result += "obese "
        
        num_calculations -= 1
    
    print(result)
    
bmi()
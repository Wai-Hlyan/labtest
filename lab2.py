#practicing python

def calculate_bmi(height, weight):
    print("Height = " + str(height))
    print("Weight = " + str(weight))
    
    bmi = 25
    
    print("BMI = " + str(bmi))
    if bmi < 18.5:
        print("Under Weight")
    elif 18.5 <= bmi <= 25.0:
        print("Normal Weight")
    elif bmi > 25.0:
        print("Over Weight")

calculate_bmi(57, 1.73)
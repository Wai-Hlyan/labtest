#practicing python

def main():
    calculate_bmi(57, 1.73)


def calculate_bmi(height, weight):
    print("Height = " + str(height))
    print("Weight = " + str(weight))
    
    bmi = weight/(height*height)
    
    print("BMI = " + str(bmi))
    if bmi < 18.5:
        print("Under Weight")
    elif 18.5 <= bmi <= 25.0:
        print("Normal Weight")
    elif bmi > 25.0:
        print("Over Weight")



if __name__ == "__main__":
    main()
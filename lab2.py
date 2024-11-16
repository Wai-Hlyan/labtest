#practicing python

def main():
    display_main_menu()



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

def display_main_menu():
    print("Python practice")
    userInput = get_user_input()
    sorted_list = sort_temperature(userInput)
    calc_avg(userInput)
    find_min_max(userInput)
    sort_temperature(userInput)
    calc_medium(sorted_list)
    calculate_bmi(57, 1.73)

def get_user_input():
    user_input = input()  
    formatted_input = user_input.split(",")
    float_list = [float(item) for item in formatted_input]
    print("Converted to float list:", float_list)
    return float_list 


def calc_avg(num):
    total = 0
    for i in num:
        total += i
    avg =  total / len(num)
    print(f'Average = {avg}')
    
def find_min_max(list):
    maxNum = max(list)
    minNum = min(list)
    print(f"Maximum Number is: {maxNum}")
    print(f"Minimum Number is: {minNum}")
    
def sort_temperature(list):
    sortedList = sorted(list)
    print(f"Sorted list is : {sortedList}")
    return sortedList

def calc_medium(list):
    length = len(list)
    mid = length // 2
    
    if length%2 == 1:
        medium = (list[mid-1] + list[mid]) / 2
        print(f"The medium number is: {medium}")
    elif length%2 == 0:
        print(f"The medium number is: {list[mid]}")

if __name__ == "__main__":
    main()
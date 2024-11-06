#
# Frederik
# BMI Calculator
# 
 
while True:
    w = float(input('Enter uour weight in kg      : '))
    h = float(input('Enter uour height in meters  : '))

    bmi = w/h**2

    print(f'Your BMI is: {bmi}')
    answer = input('Continue? (yes/no) ')
    if answer == "no":
        break

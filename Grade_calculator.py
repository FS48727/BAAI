#
# Frederik
# Assignment Grade Calculator
#

i = 1
s = int(input("How many subjects do you have?: "))
total = 0

while (i <= s):

    # 1. Input
    name = input(f'Enter the name of the subject {i}: ')
    grade = int(input(f'Enter the grade of the subject {name}: ' ))

    # 2. Process
    total += grade
    i+=1   
        
# 3. Output
print(f'Your average grade is {round(total/(i-1))}')
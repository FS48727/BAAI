#
# Frederik
# Simple Tip Calculator
#
 
i = 1
s = int(input("How many people are dining? "))
total = 0
 
while (i <= s):
 
    # 1. Input
    bill = int(input(f'Enter amount of spent by Person {i}: '))
   
    # 2. Process
    total += bill
    i+=1   

tip = int(input(f'Enter the tip percentage: '))

# 3. Output
print(f'Your total bill including tip is: ${round((total*(1+(tip/100))))}')
 
s = int(input("How many subjects do you have?: "))
total = sum([int(input(f'Enter the grade for subject {input(f"Name of subject {i+1}: ")}: ')) for i in range(s)])
print(f'Your average grade is {round(total/s)}')
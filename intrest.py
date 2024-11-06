#
# Frederik
# calculate intrest
# 

# Define function
def calucalte_intrest(principle,rate,time):
    intrest = (principle*rate*time)/100
    return intrest

# Process
y = calucalte_intrest(1000,5,2)

# Output
print(f'Intrest {y}')
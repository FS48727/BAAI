#
# Frederik
# my_add 
# 

def my_add(input):
    sum =0
    for x in input:
        sum+= int(x)
    return sum

input =[10,20,30]

answer = my_add(input)

print (f'Answer{answer}')
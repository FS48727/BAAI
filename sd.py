#
# Frederik
# my sd
#
import math
import statistics

 
def my_sd(input):
    print(f"Input: {input}")
    length = len(input)
    sum=0
    output = 0
    mean = statistics.mean(input)
    print(f"Mean: {mean}")
    for x in input:
        sum += (int(x)-mean)**2
    sum = sum / length
    output = math.sqrt(sum)
    return output
 
answer = my_sd([100, 50 ,75])

print(answer)


def add(x1,x2)
    sum x1+x2
    return sum


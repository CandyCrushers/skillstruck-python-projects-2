import math 
number = int(input("Enter a number"))
total = 0 
for i in range(1, number + 1): 
    fact = math.factorial(i)
    total += fact 
print(total)




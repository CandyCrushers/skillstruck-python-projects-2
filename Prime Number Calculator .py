number = int(input("Enter a number: "))

fact = []

for i in range(2, number): 
    if number % i == 0:
        fact.append(i)


if len(fact) == 0: 
    print(str(number) + " is a prime number")
else:
    print(fact)

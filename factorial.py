x = int(input("Enter a number to calculate it's factorial: "))
fact = 1

for i in range(1, x + 1, 1):
    fact = fact * i

print(f"Factorial of {x} is {fact}")  
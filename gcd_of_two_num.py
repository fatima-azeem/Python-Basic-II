x = int(input("Enter first number:  "))
y = int(input("Enter second number:  "))

a = x
b = y

while b != 0:
    t = b
    b = a%b
    a = t
gcd = a

print(f"Greatest Common Divisor of {x} and {y} is {gcd}" )   
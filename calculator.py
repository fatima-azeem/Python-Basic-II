x = int(input("Enter the value of x: "))
y = int(input("Enter the value of y: "))
op = input("Enter an operator (+, -, *, /): ")

if op == "+":
    result = x + y
elif op == "-":
    result = x - y
elif op == "*":
    result = x * y
elif op == "/":
    result = x / y
else:
    print("Invalid operator")

print("The result is: " + str(result))
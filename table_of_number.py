num = int(input("Enter Table Number: "))
len = int(input("Enter Table Length: "))

for x in range(1, len + 1, 1):
  print(f"{num} x {x} = {num * x}")
num = int(input("Enter a number: "))
count = 0

for x in range(2, num, 1) :
  if num % x == 0:
      count = count + 1
      break
    
if count == 0:
  print("The number is prime")
else:
  print(f"The number is not prime")
percentage = int(input("Enter Your Percnetage: "))
print(f"You Entered {percentage} % ")

if percentage >= 90:
  print("You got A+ Grade")
elif percentage >= 80:
  print("You got A Grade")
elif percentage >= 70:
  print("You got B Grade")
elif percentage >= 60:
  print("You got C Grade")  
elif percentage >= 50:
  print("You got D Grade") 
else:
  print("You are Fail")
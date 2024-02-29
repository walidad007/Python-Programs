print("~~~~Mini CalCulator~~~~")

num1 = float(input("Enter your First Number: "))
num2 = float(input("Enter your Second Number: "))


print("""
      press 1 for Addition: 
      press 2 for subtraction: 
      press 3 for Multiplication: 
      press 4 for Division: """)

choice = int(input("Enter a Number between 1-4: "))

if choice == 1:
    print("The Addition of the given numbers is: ",num1 + num2)
    
elif choice == 2:
    print("The Subtraction of the given numbers is: ",num1 - num2)
    
elif choice == 3:
    print("The Multiplication of the given numbers is: ", num1 * num2)
    
elif choice == 4:
    print("The Division of the given numbers is: ",num1 / num2)
    
else:
    print("Invalid Input from the User.")
# User will input (3Ages).Find the oldest one


a = int(input("Enter your First  Age : "))

b = int(input("Enter your Second Age : "))

c = int(input("Enter your Third  Age : "))

max = a

# if max less then B then max will be B
if max < b:
    max = b
    
# if max less then C then max will be C
elif max < c:
    max = c

print("Your maxium Age Number is: ",max)
# Prompt the user to enter the temperature
temp = float(input("Enter Temperature: "))

# Prompt the user to enter the unit of temperature ('C' for Celsius or 'F' for Fahrenheit)
unit = input("Enter unit ('C' for Celsius or 'F' for Fahrenheit): ")

# Check if the unit is Celsius ('C' or 'c')
if unit == 'C' or unit == 'c':
    # Convert Celsius to Fahrenheit using the formula: (Celsius * 9/5) + 32
    newTemp = 9 / 5 * temp + 32
    # Print the converted temperature in Fahrenheit
    print("Temperature in Fahrenheit = ", newTemp)

# Check if the unit is Fahrenheit ('F' or 'f')
elif unit == 'F' or unit == 'f':
    # Convert Fahrenheit to Celsius using the formula: (Fahrenheit - 32) * 5/9
    newTemp = 5 / 9 * (temp - 32)
    # Print the converted temperature in Celsius
    print("Temperature in Celsius =", newTemp)

# If the unit is neither 'C' nor 'F', print an error message
else:
    print("Unknown unit", unit)

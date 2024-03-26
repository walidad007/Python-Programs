
n = 5

# First loop for the right triangle pattern
for i in range(n):

    # Second loop to print asterisks in each row
    for j in range(i):
        print('*', end="")

    print('')  # Move to the next line after printing each row

# Second loop for the inverted right triangle pattern
for i in range(n, 0, -1):

    # Third loop to print asterisks in each row
    for j in range(i):
        print('*', end="")

    print('')  # Move to the next line after printing each row

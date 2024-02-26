# random module, which provides functions for generating random numbers.
import random

'''
defining the 'guess' function
this line defines a function named 'guess' that takes one parameter 'x'
'''
def guess(x):
    
    # Generating a random number
    # this line genrate random number between 1 and x
    random_number = random.randint(1, x)
    
    guess= 0
    # while loop that continues until 
    # the user's guess matches the random_number.
    while guess != random_number:
        
        # taking integer number between 1 and x
        guess = int(input('Guess a number between 1 and {x}: '))
        
        # if guess number  less than random_number
        # showes 'Too low'
        if guess < random_number:
            print("Sorry guess again. Too low.")
            
        # if guess number  greater than random_number
        # showes 'Too High'
        elif guess > random_number:
            print("Sorry, guess again. Too High.")
            
    # If the user's guess matches the random_number, 
    # the loop terminates, and the following message is printed:
    print(f'Yay, Congrats. You have Guessed the Number {random_number} correctly!! ')
    
guess(20)
            
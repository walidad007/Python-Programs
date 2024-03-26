import random

def play():
    # Ask the user for their choice
    user = input("What's your choice? 'r' for rock, 'p' for paper, 's' for scissors\n ")
    # Generate a random choice for the computer
    computer = random.choice(['r','p','s'])
    
    # Check if it's a tie
    if user == computer:
        return 'It\'s a Tie'
    
    # Check if the user wins
    if is_win(user, computer):
        return 'You won!'
    
    # If it's not a tie and the user didn't win, they lost
    return 'You Lost'

def is_win(player, opponent):
    # Define the winning combinations for the player
    # Rock beats scissors, scissors beats paper, paper beats rock
    if (player == 'r' and opponent =='s') or (player == 's' and opponent =='p') \
        or (player == 'p' and opponent =='r'):
            return True

# Call the play function and print the result
print(play())

import random
print("***************** Welcome Rock-Paper-Scissor Game ****************")
user = input("Do you want to play this game or not! Enter Yes/No: ")
if user == "no" or user == "No":
 print("Thank You! Have a nice day")
else:
   user_action = input('Enter a choice (rock, paper, scissor): ')
possible_actions = ['rock', 'paper', 'scissor']
computer_action = random.choice(possible_actions)
print(f"\nYou chose {user_action}, computer chose {computer_action}. \n")

if user_action == computer_action:
    print(f"Both players selected {user_action}. It's a tie")
elif user_action == "rock":
    if computer_action == "scissor":
        print("Rock smashes scissor! You win!")
    else:
        print('Paper covers rock! You lose.')
elif user_action == 'paper':
    if computer_action == 'rock':
        print('Paper covers rock! You win!')
    else:
        print('Scissor cut paper! You lose.') 
elif user_action == 'scissor':
    if computer_action == 'paper':
        print('Scissor cut paper! You win!')
    else:
        print('Rock smashes scissor! You lose.')


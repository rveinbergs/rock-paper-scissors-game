import random
turns = ['rock', 'paper', 'scissors']


human_turn = input ('Input human turn: ')
computer_turn = random.choice(turns)
if computer_turn == human_turn: 
    print('Draw!')
if human_turn == 'rock' and computer_turn == 'scissors':
    print('human wins!')
elif human_turn == 'paper' and computer_turn == 'rock':
    print('human wins!')    
elif human_turn == 'scissors' and computer_turn == 'paper':
    print('human wins!')
else: print('Computer wins!')

restart = input("Would you like to play again? ")
if restart == "yes" or restart == "y":
    script()
if restart == "n" or restart == "no":
    print("Good bye!")

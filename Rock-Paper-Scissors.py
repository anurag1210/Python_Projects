#Simple rock paper scissors game

import random


print('Let the Rock, Paper, Scissor game begin')


user_input = input('Enter your choice from Rock, Paper, Scissors : ')

choice = random.randint(1,3)
print(choice)
if choice==1:
    my_choice = 'Rock'
    print(f'My Choice is Rock')
elif choice==2:
    my_choice = 'Paper'
    print(f'My Choice is Paper')
else:
    my_choice = 'Scissors'
    print(f'My Choice is Scissors')


#Logic to win

if my_choice == user_input:
    print('Its a tie')
elif my_choice =='Rock' and user_input == 'Paper':
    print('I win')
elif my_choice == 'Paper' and user_input == 'Scissors':
    print('I win')
elif my_choice == 'Scissors' and user_input == 'Rock':
    print('I win')
else:
    print('User wins')


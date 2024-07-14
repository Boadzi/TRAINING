#This is a guessing gsme 

def display_menu():
    print('Hello! Welcome to Guess World')
    print('You guess rightly, You win.  You guess wrongly, You are FIRED!')

import random

def main_game():
    random_number = random.randint(1,100)
    attempts=0
    while True:
          user_guess = int(input('It is time. Now guess a number '))
          attempts += 1
          if user_guess == random_number:
             print(f'Yes! you got it, in {attempts} attempts.')
          elif user_guess < random_number:
             print('Oh NOO! Too Low.Try again')
          else:
             print('Oops! Too High. Try again')
             break

display_menu()             



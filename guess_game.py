print('Hello! Welcome to Guess World')
print('You guess rightly, You win.  You guess wrongly, You are FIRED!')

# randomly select a number between 1-100.
import random
random_number = random.randint(1,100)

attempts=0
while True:
         # getting user input
        user_guess = int(input('You want to guess again? Now guess a number '))
        attempts += 1
        if user_guess == random_number:
             print(f'Yes! you got it, in {attempts} attempts.')
        elif user_guess < random_number:
             print('Oh NOO! Too Low.Try again')
        else:
             print('Oops! Too High. Try again')
             


    
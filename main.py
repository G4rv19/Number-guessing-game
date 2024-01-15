import random
#User inputs the lower bound and upper bound of the range.
lower_bound = int(input("What is your starting number for the guessing game range ? "))
upper_bound = int(input("What is your ending number for the guessing game range ? "))
#generate a random number from the upper and lower range int.
number = random.randrange(lower_bound, upper_bound)
while True:
    user_guess = int(input("Guess the number: "))
    if user_guess > number:
        print("Too high guess again")
    elif user_guess < number:
        print("Too small guess again.")
    else:
        print("Guessed")
        break

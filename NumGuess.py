import random


def game_loop(number):
    """Main game loop - this function takes an argument which is the winning number,
     and loops until player guesses correctly"""
    guess = ''
    while guess != number:

        guess = input("Guess the number:")
        try:
            guess = int(guess)
        except TypeError:
            print("Please provide a valid number")
            continue
        if guess > number:
            print("Too big!")
        elif guess < number:
            print("Too small!")

    print("You win!")


random_num = random.randint(1, 100)
game_loop(random_num)

import random

def guess(x):
    random_number = random.randint(1,x)
    guess = 0
    while guess != random_number:
        guess = int(input(f"guess your random number between 1 and {x}: "))
        print(guess)
        if guess > random_number:
            print("try again, guess is greater ")
        elif guess <  random_number:   
            print("try again, guess is lowe")
    print(f"congrats your guess {guess} is right ")
guess(10)    
    
import random

def guess_number():
    random_generator = random.SystemRandom()
    number = random_generator.randint(1, 100)
    attempts = 0

    print("Welcome to the High Low!")
    print(f"Your starting number is {number}. Is the next number higher or lower?")
    print("Enter 'h' for higher, 'l' for lower, or 'q' to quit.")
    
    while True:
        guess = input("Enter your guess: ")
        new_number = random_generator.randint(number, 100)
        if guess == 'q':
            break
        elif guess == 'h':
            if new_number > number:
                print(f"Correct! The new number is {new_number}. Is the next number higher or lower?")
                number = new_number
                attempts += 1
            else:
                print(f"Wrong! The number was {new_number}.")
                break
        elif guess == 'l':
            if new_number < number:
                print(f"Correct! The new number is {new_number}. Is the next number higher or lower?")
                number = new_number
                attempts += 1
            else:
                print(f"Wrong! The number was {new_number}.")
                break
        else:
            print("Invalid input. Please try again.")
            continue

    print(f"Thanks for playing! You guessed correctly {attempts} time(s) before failing!")


guess_number()


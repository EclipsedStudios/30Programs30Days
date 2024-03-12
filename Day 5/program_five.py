import random

def secure_input(prompt, valid_responses=None):
    while True:
        response = input(prompt).lower()[0]
        if valid_responses is None or response in valid_responses:
            return response
        print("Invalid input. Please try again.")

def generate_number(current_number=None):
    random_generator = random.SystemRandom()
    output = random_generator.randint(1, 100)
    if(output == current_number):
        output = generate_number(output)
    return output

def process_guess(current_number, guess):
    new_number = generate_number(current_number)
    if (guess == 'h' and new_number > current_number) or (guess == 'l' and new_number < current_number):
        return True, new_number
    return False, new_number

def play_game():
    print("Welcome! This game is called High Low...")
    number = generate_number()
    print(f"Your starting number is {number}. Is the next number higher or lower?")

    attempts = 0

    while True:
        guess = secure_input("Enter 'h' for higher, 'l' for lower, or 'q' to quit: ", ['h', 'l', 'q'])
        if guess == 'q':
            break
        correct, number = process_guess(number, guess)
        if correct:
            print(f"Correct! The new number is {number}.")
            attempts += 1
        else:
            print(f"Wrong! The number was {number}.")
            break

    print(f"Thanks for playing! You guessed correctly {attempts} time(s).")

if __name__ == "__main__":
    play_game()

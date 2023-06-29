import os
import secrets
import string

def generate_mnemonic(input_file):
    mnemonics = {}

    with open(input_file, 'r') as file:
        for line in file:
            character, word = line.strip().split(',')
            mnemonic = f"{word} "
            mnemonics[character] = mnemonic

    return mnemonics


password_letters = [char for char in string.ascii_lowercase if char.isalnum()]

def generate_password():
    user_input = input("Enter a word or phrase to include in your password: ")

    characters = ''.join(password_letters) + string.digits + string.punctuation
    random_part = ''.join(secrets.choice(characters) for _ in range(4))

    password = user_input.lower() + random_part
    return password


current_directory = os.path.dirname(os.path.abspath(__file__))

input_file = os.path.join(current_directory, 'mnemonic_data.txt')
mnemonic_dict = generate_mnemonic(input_file)

password = generate_password()

print(f"Here is your new password:\n{password}")

print("Here is a mnemonic for your password: ")

for c in password:
    if mnemonic_dict.get(c) is not None:
        print(mnemonic_dict.get(c), end="")
    else:
        print(f"{c} ", end="")

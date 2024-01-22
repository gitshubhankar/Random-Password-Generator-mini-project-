#import the necessary modules
import random
import string

#define the function generate_password
def generate_password(length=12, uppercase=True, digits=True, symbols=True):
    characters = string.ascii_letters  # lowercase + uppercase letters
    if digits:
        characters += string.digits  # add digits
    if symbols:
        characters += string.punctuation  # add symbols

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

if __name__ == "__main__":
    # Example usage: generate a password with default settings
    password = generate_password()
    print("Generated Password:", password)

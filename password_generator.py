import random
import string

def generate_password(length, use_upper=True, use_digits=True, use_symbols=True):
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase if use_upper else ''
    digits = string.digits if use_digits else ''
    symbols = string.punctuation if use_symbols else ''

    all_chars = lower + upper + digits + symbols

    if not all_chars:
        return "No character types selected!"

    password = ''.join(random.choice(all_chars) for _ in range(length))
    return password

try:
    length = int(input("Enter desired password length: "))
    upper = input("Include uppercase letters? (yes/no): ").lower() == 'yes'
    digits = input("Include digits? (yes/no): ").lower() == 'yes'
    symbols = input("Include symbols? (yes/no): ").lower() == 'yes'

    result = generate_password(length, upper, digits, symbols)
    print("\nGenerated Password:", result)

except ValueError:
    print("Please enter a valid number for password length.")

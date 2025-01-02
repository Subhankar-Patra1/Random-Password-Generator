import random
import string

def generate_password(length=12):
    
    upper = string.ascii_uppercase
    lower = string.ascii_lowercase
    digits = string.digits
    special = string.punctuation
    
    
    all_characters = upper + lower + digits + special
    password = [
        random.choice(upper),
        random.choice(lower),
        random.choice(digits),
        random.choice(special),
    ]
    
    password += random.choices(all_characters, k=length - 4)
    
    
    random.shuffle(password)
    
    return ''.join(password)

try:
    length = int(input("Enter the desired password length (minimum 4): "))
    if length < 4:
        print("Password length must be at least 4.")
    else:
        print("Generated Password:", generate_password(length))
except ValueError:
    print("Please enter a valid number.")

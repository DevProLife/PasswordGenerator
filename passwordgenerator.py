import random
import string
import pyperclip

def generate_password(length=12, use_upper=True, use_lower=True, use_digits=True, use_special=True):
    characters = ''
    if use_upper:
        characters += string.ascii_uppercase
    if use_lower:
        characters += string.ascii_lowercase
    if use_digits:
        characters += string.digits
    if use_special:
        characters += string.punctuation

    if not characters:
        return "Error: No character types selected!"

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("Password Generator")
    length = int(input("Enter password length: "))
    use_upper = input("Include uppercase letters? (y/n): ").lower() == 'y'
    use_lower = input("Include lowercase letters? (y/n): ").lower() == 'y'
    use_digits = input("Include digits? (y/n): ").lower() == 'y'
    use_special = input("Include special characters? (y/n): ").lower() == 'y'

    password = generate_password(length, use_upper, use_lower, use_digits, use_special)
    
    if "Error" in password:
        print(password)
    else:
        print(f"Generated Password: {password}")
        copy_choice = input("Copy to clipboard? (y/n): ").lower()
        if copy_choice == 'y':
            pyperclip.copy(password)
            print("Password copied to clipboard!")

if __name__ == "__main__":
    main()

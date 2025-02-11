import random
import string
import pyperclip

def generate_password(length=12, use_upper=True, use_lower=True, use_digits=True, use_special=True, avoid_similar=True, ensure_all_types=True):
    characters = ''
    if use_upper:
        characters += string.ascii_uppercase
    if use_lower:
        characters += string.ascii_lowercase
    if use_digits:
        characters += string.digits
    if use_special:
        characters += string.punctuation

    if avoid_similar:
        similar_chars = 'Il1O0'  # Characters that can be easily confused
        characters = ''.join(c for c in characters if c not in similar_chars)

    if not characters:
        return "Error: No character types selected!"

    if ensure_all_types:
        password = []
        if use_upper:
            password.append(random.choice(string.ascii_uppercase))
        if use_lower:
            password.append(random.choice(string.ascii_lowercase))
        if use_digits:
            password.append(random.choice(string.digits))
        if use_special:
            password.append(random.choice(string.punctuation))

        remaining_length = length - len(password)
        password += [random.choice(characters) for _ in range(remaining_length)]
        random.shuffle(password)
        password = ''.join(password)
    else:
        password = ''.join(random.choice(characters) for _ in range(length))

    return password

def main():
    print("\n=== Strong Password Generator ===")
    length = int(input("Enter password length (minimum 6): "))
    if length < 6:
        print("Password length should be at least 6 for better security.")
        return

    use_upper = input("Include uppercase letters? (y/n): ").lower() == 'y'
    use_lower = input("Include lowercase letters? (y/n): ").lower() == 'y'
    use_digits = input("Include digits? (y/n): ").lower() == 'y'
    use_special = input("Include special characters? (y/n): ").lower() == 'y'
    avoid_similar = input("Avoid similar characters (e.g., 'l', '1', 'O')? (y/n): ").lower() == 'y'
    ensure_all_types = input("Ensure at least one of each selected type? (y/n): ").lower() == 'y'

    password = generate_password(length, use_upper, use_lower, use_digits, use_special, avoid_similar, ensure_all_types)
    
    if "Error" in password:
        print(password)
    else:
        print(f"\nGenerated Password: {password}")
        copy_choice = input("Copy to clipboard? (y/n): ").lower()
        if copy_choice == 'y':
            pyperclip.copy(password)
            print("Password copied to clipboard!")

if __name__ == "__main__":
    main()

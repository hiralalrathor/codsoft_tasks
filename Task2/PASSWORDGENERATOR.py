import random
import string

def generate_password(length, include_digits=True, include_symbols=True):
    """Generates a random password based on specified criteria."""
    
    character_pool = string.ascii_letters
    
    if include_digits:
        character_pool += string.digits
    if include_symbols:
        character_pool += string.punctuation
        
    password = ''.join(random.choice(character_pool) for _ in range(length))
    return password

def main():
    print("=== Random Password Generator ===")
    
    while True:
        try:
            length = int(input("\nEnter the desired password length (minimum 4): "))
            if length < 4:
                print("For decent security, please choose a length of at least 4.")
                continue
            break
        except ValueError:
            print("Invalid input! Please enter a valid number.")

    print("\n--- Password Complexity Options ---")
    include_digits = input("Include numbers? (y/n, default 'y'): ").strip().lower() != 'n'
    include_symbols = input("Include special symbols (!@#$...)? (y/n, default 'y'): ").strip().lower() != 'n'

    password = generate_password(length, include_digits, include_symbols)

    print("\n" + "=" * 32)
    print(f"Generated Password: {password}")
    print("=" * 32)

if __name__ == "__main__":
    main()

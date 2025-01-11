import random
import string

def generate_password(length=12, include_digits=True, include_symbols=True):
    # Define a string of characters to choose from (letters by default)
    characters = string.ascii_letters
    
    # Add digits to the character set if requested
    if include_digits:
        characters += string.digits
        
    # Add symbols to the character set if requested
    if include_symbols:
        characters += string.punctuation

    # Generate a password by randomly selecting characters from the set
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("\nWelcome to the Advanced Password Generator!")
    
    # Get user input for password customization
    length = int(input("Enter the desired password length: "))
    include_digits = input("Include digits? (yes/no): ").lower() == "yes"
    include_symbols = input("Include symbols? (yes/no): ").lower() == "yes"

    # Generate and display the password using the function
    password = generate_password(length, include_digits, include_symbols)
    print("Generated Password:", password)

if __name__ == "__main__":
    main()

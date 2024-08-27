import random
import string

def generate_password(length):
    # Define the character sets to include in the password
    characters = string.ascii_letters + string.digits + string.punctuation
    
    # Generate a random password
    password = ''.join(random.choice(characters) for i in range(length))
    
    return password

def main():
    print("Welcome to the Password Generator!")
    
    # Get the desired password length from the user
    while True:
        try:
            length = int(input("Enter the desired password length: "))
            if length < 1:
                print("Please enter a positive number.")
            else:
                break
        except ValueError:
            print("Please enter a valid number.")
    
    # Generate the password
    password = generate_password(length)
    
    # Display the generated password
    print(f"Your generated password is: {password}")

if __name__ == "__main__":
    main()

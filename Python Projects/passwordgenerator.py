import random
import string

def generate_password(length, difficulty):
    if difficulty == "easy":
        characters = string.ascii_letters + string.digits
    elif difficulty == "ok":
        characters = string.ascii_letters + string.digits + "!@#$%^&*()-_=+[{]}\\|;:'\",<.>/?"
    elif difficulty == "hard":
        characters = string.ascii_letters + string.digits + string.punctuation
    else:
        print("Invalid difficulty level. Using default characters.")
        characters = string.ascii_letters + string.digits + string.punctuation
    
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def generate_multiple_passwords(num_passwords, password_length, difficulty):
    passwords = []
    for _ in range(num_passwords):
        passwords.append(generate_password(password_length, difficulty))
    return passwords

def main():
    num_passwords = int(input("Enter the number of passwords to generate: "))
    password_length = int(input("Enter the length of each password: "))
    difficulty = input("Choose password difficulty (easy, ok, hard): ").lower()
    
    passwords = generate_multiple_passwords(num_passwords, password_length, difficulty)
    
    print("\nGenerated Passwords:")
    for password in passwords:
        print(password)

if __name__ == "__main__":
    main()

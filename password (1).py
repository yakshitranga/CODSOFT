import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    try:
        length = int(input("Enter the desired password length: "))
        if length <= 0:
            print("Invalid input. Please enter a positive integer.")
            return
        password = generate_password(length)
        print(f"Generated password: {password}")
    except ValueError:
        print("Invalid input")

if __name__ == "__main__":
    main()

def main():
    password_length = 10
    password = input("Enter password: ")
    while len(password) < password_length:
        print("Password does not satisfy requirements. Try again.")
        password = input("Enter password: ")
    print("*" * len(password))


main()

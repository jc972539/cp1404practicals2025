def main():
    password_length = 10
    password = get_password(password_length)
    print_stars(password)


def print_stars(password: str):
    print("*" * len(password))


def get_password(password_length: int) -> str:
    password = input("Enter password: ")
    while len(password) < password_length:
        print("Password does not satisfy requirements. Try again.")
        password = input("Enter password: ")
    return password


main()

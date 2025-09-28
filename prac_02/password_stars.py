MINIMUM_LENGTH = 10


def main():
    """Ask user for a password, then print a number of stars according to its length"""
    password = get_password(MINIMUM_LENGTH)
    print_stars(password)


def get_password(MINIMUM_LENGTH):
    """Get password from user and check that it satisfies the requirements, then return the password"""
    password = input(f"Enter password at least {MINIMUM_LENGTH} characters long: ")
    while len(password) < MINIMUM_LENGTH:
        print("Password does not satisfy requirements. Try again.")
        password = input(f"Enter password at least {MINIMUM_LENGTH} characters long: ")
    return password


def print_stars(password):
    """Print the number of stars according to the length of the password"""
    print("*" * len(password))


main()

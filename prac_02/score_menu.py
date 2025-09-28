import math


MENU = "(G)et a valid score\n(P)rint result\n(S)how stars\n(Q)uit"


def main():
    """Ask user for score, then provide a menu of potential options"""
    score = float(input("Enter score: "))
    while return_status(score) == "Invalid":
        print("Invalid score. Try again")
        score = float(input("Enter score: "))
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "G":
            score = float(input("Enter score: "))
            while return_status(score) == "Invalid":
                print("Invalid score. Try again")
                score = float(input("Enter score: "))
        elif choice == "P":
            print(return_status(score))
        elif choice == "S":
            print_stars(score)
        else:
            print("Invalid choice")
        print(MENU)
        choice = input(">>> ").upper()
    print("Finished")


def return_status(score):
    """Return the score status"""
    if score < 0 or score > 100:
        return "Invalid"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


def print_stars(score):
    """Print the number of stars according to the score"""
    print("*" * math.ceil(score))


main()

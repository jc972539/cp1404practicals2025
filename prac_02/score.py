"""
CP1404/CP5632 - Practical
Program to determine score status
"""

from random import randint


def main():
    """Ask user for score and print score status"""
    score = float(input("Enter score: "))
    print(return_result(score))
    score = randint(0, 100)
    print(f"The score of {score} is {return_result(score).lower()}")


def return_result(score):
    """determine the score status given the score"""
    if score < 0 or score > 100:
        return "Invalid"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


main()

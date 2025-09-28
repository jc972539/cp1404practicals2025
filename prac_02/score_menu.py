import math, random

menu = "(G)et a valid score\n(P)rint result\n(S)how stars\n(Q)uit"
print(menu)
choice = input(">>> ").upper()
while choice != "Q":
    if choice == "G":
        score = random.randint(0, 100)
        print(f"The generated score is {score}")
    elif choice == "P":
        if score >= 90:
            print("Excellent")
        elif score >= 50:
            print("Passable")
        else:
            print("Bad")
    elif choice == "S":
        print("*" * math.ceil(score))
    else:
        print("Invalid choice")
    print(menu)
    choice = input(">>> ").upper()
print("Finished.")

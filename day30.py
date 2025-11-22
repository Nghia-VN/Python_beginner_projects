import random

options = ("Kéo", "Búa", "Bao")
computer = random.choice(options)
player = None
running = True
while running:
    while player not in options:
        player = input("Enter a choice:")
    print(f"Player:{player}")
    print(f"computer:{computer}")
    if player == computer:
        print("TIE!")
    elif player == "Kéo" and computer == "Bao":
        print("You WIN!")
    elif player == "Búa" and computer == "Kéo":
        print("You WIN!")
    elif player == "Bao" and computer == "Búa":
        print("You WIN!")
    else:
        print("You LOSE!")
    # play_again = input("Play again? Y/N").lower()
    # if play_again == "y":
    # running = False
    if not input("Play again? y/n:").lower == "y":
        running = False

print("Thanks for playing!")

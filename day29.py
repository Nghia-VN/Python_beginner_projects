import random

lowest_num = int(input("Enter lowest number:"))
hightest_num = int(input("Enter hightest number:"))
answer = random.randint(lowest_num, hightest_num)
guesses = 0
is_running = True
print(f"Please select a number betwen {lowest_num} and {hightest_num}")
while is_running:
    guess = input("Enter your guess:")

    if guess.isdigit():
        guess = int(guess)
        guesses += 1
        if guess < lowest_num or guess > hightest_num:
            print("That number is out of range")
            print(f"Please select a number betwen {lowest_num} and {hightest_num}")
        elif guess < answer:
            print("Too low ! try again")
        elif guess > answer:
            print("Too high!, try again")
        else:
            print("CORRCET!")
            print(f"Number of guesses: {guess}")
            is_running = False
    else:
        print("Invalid guess")
        print("Enter your guess:")

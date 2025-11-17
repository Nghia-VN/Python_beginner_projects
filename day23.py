user_names = []
while True:
    user_name = input("Enter your name:")
    user_names.append(user_name)
    for i in range(len(user_names)):
        if i == "!":
            print("Your name is not correct!")
        else:
            i = ++i
        print(f"Hello {user_names}")

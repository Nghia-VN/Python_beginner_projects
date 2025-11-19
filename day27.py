menu = {"pizza": 30.0, "rice": 1.0, "chicken wing": 10.0, "mushroom": 3.50}
cart = []
total = 0
print("-------------MENU-------------")
for key, value in menu.items():
    print(f"{key:20}: ${value: .2f}")
while True:
    food = input("Select an item (q to quit):").lower()
    if food == "q":
        break
    elif menu.get(food) is not None:
        cart.append(food)
    else:
        print("incorect")
print("---------Your Order---------")
for food in cart:
    total += menu.get(food)
    print(food, end=" ")

print()
print(f"your total is: ${total: .2f}")

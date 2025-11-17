rows = int(input("Enter the # of rows:"))
colums = int(input("Enter the # of colums:"))
symbol = input("Enter a symbol to use:")
for x in range(rows):
    for y in range(colums):
        print(symbol, end=" ")

    print()

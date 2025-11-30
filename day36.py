# List comprehension
# add = [x for x in range(1, 5) if x > 2]
# fruits = ["Appel", "Banana", "Mango", "Orange"]
# x = [fruit for fruit in fruits]
number = [1, 3, 5, 7, 8, -9, -10, -11, 0]
# possitive_nums = [num for num in number if num >= 0]
even_num = [num for num in number if num % 2 == 0 and num >= 0]
print(even_num)

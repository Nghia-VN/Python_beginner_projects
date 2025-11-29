"""gardes = {"Nghia": 8, "Anh": 10, "Hiep": 9}
student = input("Enter the name of a student:")
if student not in gardes:
    print(f"{student} was not found")
else:
    print(f"{student}'s grade is {gardes[student]}")"""

email = input("Enter your email:")
if "@" and "." in email:
    print(email)
else:
    print("Invalid email")

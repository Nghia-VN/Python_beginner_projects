capital = {"USA": "Washington D.C", "India": "New dehli", "Viet Nam": "Ha Noi"}
# print(capital.get("Viet Nam"))
"""if capital.get("Japan"):
    print("Capital is exist")
else:
    print("Capital doesn't exist")"""
# print(dir(capital))
# capital.update({"Japan": "Tokyo"})
# print(capital.get("Japan"))
# keys = capital.keys()
# capital.pop("China")
# capital.clear()


# print(capital)
# item = capital.items()
# print(item)
for value, item in capital.items():
    print(f"{value}:{item}")

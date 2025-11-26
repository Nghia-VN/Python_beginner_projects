# arg
"""
def add(*args):
    total = 0
    for arg in args:
        total += arg
    return total


print(add(1, 4, 9))"""

# kwargs
"""
def print_adress(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}:{value}")


print(print_adress(City="Ha Noi", Zipcode=10000, Street="Phung Khoang"))
"""


def shipping_label(*args, **kwargs):
    for name in args:
        print(name)
    print()
    if "apt" in kwargs:
        print(f"{kwargs.get('street')} {kwargs.get('apt')}")
    else:
        print(f"{kwargs.get('street')}")
    print(f"{kwargs.get('city')} {kwargs.get('zip')}")


print(
    shipping_label(
        "Van Nghia", "Do", street="Nguyen trai", apt=100, zip=10000, city="Ha Noi"
    )
)

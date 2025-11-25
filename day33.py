def get_phone(country, area, first, last):
    return f"{country}-{area}-{first}-{last}"


phone_num = get_phone(country=1, first="Van Nghia", area=456, last="Do")
print(phone_num)

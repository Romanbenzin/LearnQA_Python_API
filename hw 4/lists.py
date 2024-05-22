list_one = [
    "one",
    "two",
    "three"
]

list_two = [
    {"one":1},
    {"two":2},
    {"three":3}
]

for i in range(len(list_one)):
    for key, value in list_two[i].items():
        if list_one[i] == key:
            print(f"Значение из списка list_one: '{list_one[i]}' равно ключу из списка list_two: '{key}'")
        else:
            print("Ошибка")
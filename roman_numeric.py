from collections import OrderedDict

int_number = int(input('Write number to convert:\n>> '))

ROMAN_NUMBERS = OrderedDict({
    1000: "M",
    900: "CM",
    500: "D",
    400: "CD",
    100: "CM",
    90: "XC",
    50: "L",
    40: "XL",
    10: "X",
    9: "IX",
    5: "V",
    4: "IV",
    1: "I",
})


def convert(num):
    for r in ROMAN_NUMBERS.keys():
        x, y = divmod(num, r)
        yield ROMAN_NUMBERS[r] * x
        num -= r * x
        if num <= 0:
            break


print(">> "+"".join([i for i in convert(int_number)]))

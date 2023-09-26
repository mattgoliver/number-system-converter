"""Positional Number System Converter.

I am learning about positional number systems in my IT 101 class,
so I figured what better way to review them than to program something with them.

Author: Matthew Oliver
Version: 9/25/2023
"""


def convert_to_decimal(base, number):
    """Converts a given number to a decimal (base 10) number.

    Args:
        base (int): Base number of the given number, up to 16
        number (str): Number you want to convert

    Returns:
        int: Number in decimal (base 10)
    """
    number = str(number)
    decimal_num = 0
    i = len(number) - 1

    for char in number:
        if char not in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
            if char.lower() == "a":
                char = 10
            elif char.lower() == "b":
                char = 11
            elif char.lower() == "c":
                char = 12
            elif char.lower() == "d":
                char = 13
            elif char.lower() == "e":
                char = 14
            elif char.lower() == "f":
                char = 15

        decimal_num += int(char) * (base ** i)

        i -= 1

    return decimal_num


def convert_from_decimal(base, number):
    """Converts from decimal to base x number.

    Args:
        base (int): Base of number to convert to, up to 16
        number (str): Decimal number to convert

    Returns:
        str: Number in specified base
    """
    new_num = ""

    while number != 0:
        remainder = number % base
        if remainder > 9:
            if remainder == 10:
                remainder = 'A'
            elif remainder == 11:
                remainder = 'B'
            elif remainder == 12:
                remainder = 'C'
            elif remainder == 13:
                remainder = 'D'
            elif remainder == 14:
                remainder = 'E'
            elif remainder == 15:
                remainder = 'F'

        new_num += str(remainder)
        number = number // base

    new_num = ''.join(reversed(new_num))

    return new_num


if __name__ == "__main__":
    print(f"408F (hexidecimal) in decimal is {convert_to_decimal(16, '408F')}.")
    print(f"3635 (decimal) in hexidecimal is {convert_from_decimal(16, 3635)}.")

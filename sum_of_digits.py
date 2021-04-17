"""
Given a number, find the sum of its digits. Take the number as
an input from the user
"""


def sum_of_digits(number):
    total = 0
    while number > 0:
        digit = number % 10
        number = number // 10
        total = total + digit
    return total


if __name__ == '__main__':
    print(sum_of_digits(125))
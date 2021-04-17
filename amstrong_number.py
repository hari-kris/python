"""
 Given a number, check whether the given number is an
Armstrong number or not. A positive integer is called an
Armstrong number of order n if:
abcd... = an
 + bn + cn
 + dn
 + ...
Example: 153 = 1*1*1 + 5*5*5 + 3*3*3
153 is an Armstrong number of order 3.
"""


def armstrong_number_checker(number):
    computed_number = 0
    original_number = number
    while number > 0:
        remainder = number % 10
        computed_number = computed_number + (remainder*remainder*remainder)
        number = number // 10
    if computed_number == original_number:
        return True
    else:
        return False


if __name__ == '__main__':
    print(armstrong_number_checker(370))
    print(armstrong_number_checker(121))
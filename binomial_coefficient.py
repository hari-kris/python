"""
 Given two numbers n and r, find the value of nCr (binomial
coefficient: nCr = (n!) / (r! * (n-r)!))
"""


def compute_factorial(number):
    fact = 1
    if number == 1:
        return fact
    else:
        return number * compute_factorial(number - 1)


def compute_binomial_coefficient(n, r):
    return compute_factorial(n) / (compute_factorial(r) * compute_factorial(n-r))


if __name__ == '__main__':
    # print(compute_factorial(120))
    print(compute_binomial_coefficient(7,2))
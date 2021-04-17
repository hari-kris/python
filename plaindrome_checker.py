"""
Given a string, write a python function to check if it is
palindrome or not. A string is said to be palindrome if the reverse
of the string is the same as string. For example, “malayalam” is a
palindrome, but “music” is not a palindrome.
"""


def palindrome_checker(input_string):
    if input_string[::-1] == input_string:
        return True
    else:
        return False


def palindrome_checker_loop(input_string):
    length = len(input_string)
    temp_string = ""
    for index in range(length-1, -1, -1):
        temp_string = temp_string + input_string[index]
    if temp_string == input_string:
        return True
    else:
        return False


if __name__ == '__main__':
    print(palindrome_checker_loop("music"))
    print(palindrome_checker_loop("malayalam"))
"""
Searching: Given a sorted array arr[] of n elements, write a
function to search a given element x in arr[]. Do it using linear
"""


def linear_search(input_array, search_element):
    pos = 0
    for each in input_array:
        if each == search_element:
            print(f"Element Found at Position {pos}")
            return pos
        else:
            pos = pos + 1
    return -1

if __name__ == '__main__':
    input_elements = [1, 2, 2, 3, 42, 24343, 342, 34, 5]
    search_item = 5
    print(linear_search(input_elements, 15))


"""
 Given an array which may contain duplicates, print all elements
and their frequencies
"""


def detect_duplicate_frequency(input_array):
    freq_array = {}
    for each in input_array:
        if freq_array.get(each) is None:
            freq_array[each] = 1
        else:
            freq_array[each] = freq_array[each] + 1
    return freq_array


if __name__ == '__main__':
    my_list = [1, 1, 2, 2, 3, 4, 5, 5]
    print(detect_duplicate_frequency(my_list))
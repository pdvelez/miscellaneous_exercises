"""
This exercise can be found at
http://www.w3resource.com/python-exercises/data-structures-and-algorithms/python-recursion.php
"""


def convert_int_string(num_int, base):
    """
    Method using recursion to convert an integer to a string in any base
    """
    convert_to_string = "0123456789ABCDEF"
    if num_int < base:
        return convert_to_string[num_int]
    else:
        return convert_int_string(num_int // base, base) + str(num_int % base)


if __name__ == '__main__':
    print(convert_int_string(15, 16))

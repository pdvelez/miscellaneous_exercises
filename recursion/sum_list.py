"""
This exercise can be found at
http://www.w3resource.com/python-exercises/data-structures-and-algorithms/python-recursion.php
"""


def sum_list(alist):
    """
    Function that calculates the sum of a list of numbers using recursion
    """
    if len(alist) == 1:
        return alist[0]
    else:
        return alist[0] + sum_list(alist[1:])


if __name__ == '__main__':
    print(sum_list([3, 7, 2, 1, 8, 4]))

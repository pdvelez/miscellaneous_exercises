"""
This exercise can be found at
http://www.w3resource.com/python-exercises/data-structures-and-algorithms/python-recursion.php
"""


def recursion_list_sum(alist):
    """
    Method to calculate a recursion list sum
    """
    total_sum = 0
    for item in alist:
        if type(item) == type([]):
            total_sum += recursion_list_sum(item)
        else:
            total_sum += item
    return total_sum


if __name__ == '__main__':
    print(recursion_list_sum([1, 2, [3, 4], [5, 6]]))
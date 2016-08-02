"""
This exercise can be found at
http://www.w3resource.com/python-exercises/data-structures-and-algorithms/python-recursion.php
"""


def a_to_power_b(a, b):
    """
    Return a to the power of b. i.e. pow(3, 4) = 81
    """

    if b == 0:
        return 1
    elif a == 0:
        return 0
    elif b == 1:
        return a
    else:
        return a * a_to_power_b(a, b - 1)


if __name__ == '__main__':
    print(a_to_power_b(3, 4))
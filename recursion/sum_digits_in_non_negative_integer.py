"""
This exercise can be found at
http://www.w3resource.com/python-exercises/data-structures-and-algorithms/python-recursion.php
"""


def sum_non_negative_integer(n):
    """
    Sum of digits that form a non-negative integer
    """
    if n < 1:
        return n % 10
    else:
        return n % 10 + sum_non_negative_integer(n // 10)


if __name__ == '__main__':
    print(sum_non_negative_integer(45))

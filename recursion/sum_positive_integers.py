"""
This exercise can be found at
http://www.w3resource.com/python-exercises/data-structures-and-algorithms/python-recursion.php
"""


def sum_positive_integers_mult_2(n):
    """
    Sum of positive integers of n+(n-2)+(n-4)...(until n-x <= 0)
    """

    if n <= 0:
        return n
    else:
        return n + sum_positive_integers_mult_2(n - 2)


if __name__ == '__main__':
    print(sum_positive_integers_mult_2(10))
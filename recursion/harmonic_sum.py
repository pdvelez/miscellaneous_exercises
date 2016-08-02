"""
This exercise can be found at
http://www.w3resource.com/python-exercises/data-structures-and-algorithms/python-recursion.php
"""


def harmonic_sum(n):
    """
    Return the harmonic sum of n-1
    i.e: 1/1 + 1/2 + 1/3 + 1/4 + 1/5 + ...
    """

    if n == 1:
        return 1.
    else:
        return 1. / n + harmonic_sum(n - 1)


if __name__ == '__main__':
    print(harmonic_sum(7))
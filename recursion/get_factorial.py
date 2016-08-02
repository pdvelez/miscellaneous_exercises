"""
This exercise can be found at
http://www.w3resource.com/python-exercises/data-structures-and-algorithms/python-recursion.php
"""


def get_factorial(number):
    """
    Get the factorial of a non-negative number
    """
    if number == 1:
        return 1
    else:
        return number * get_factorial(number - 1)


if __name__ == '__main__':
    print(get_factorial(5))
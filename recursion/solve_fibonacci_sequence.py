"""
This exercise can be found at
http://www.w3resource.com/python-exercises/data-structures-and-algorithms/python-recursion.php
"""


def solve_fibonacci_sequence(n):
    """
    Solve the fibonacci number using recursion. Returns the n-th element in the
    series
    """
    if n == 1 or n == 2:
        return 1
    else:
        return solve_fibonacci_sequence(n - 1) + solve_fibonacci_sequence(n - 2)


if __name__ == '__main__':
    print(solve_fibonacci_sequence(7))
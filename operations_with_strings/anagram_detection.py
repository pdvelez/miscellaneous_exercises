"""
This exercise can be found at
http://interactivepython.org/runestone/static/pythonds/AlgorithmAnalysis/AnAnagramDetectionExample.html
"""


def anagram_solution_1(s1, s2):
    """ O(n^2) operation """
    alist = list(s2)

    pos1 = 0
    still_ok = True

    while pos1 < len(s1) and still_ok:
        pos2 = 0
        found = False
        while pos2 < len(s2) and not found:
            if s1[pos1] == alist[pos2]:
                found = True
            else:
                pos2 += 1

        if found:
            alist[pos2] = None
        else:
            still_ok = False

        pos1 += 1

    return still_ok


def anagram_solution_2(s1, s2):
    """ O(n^2) operation """
    alist1 = list(s1)
    alist2 = list(s2)

    alist1.sort()  # Will produce O(n^2)
    alist2.sort()

    pos = 0
    matches = True

    while pos < len(s1) and matches:
        if alist1[pos] == alist2[pos]:
            pos += 1
        else:
            matches = False

    return matches


def anagram_solution_3(s1, s2):
    """ O(n) operation """
    c1 = [0] * 26
    c2 = [0] * 26

    for i in range(len(s1)):
        pos = ord(s1[i]) - ord('a')
        c1[pos] += 1

    for i in range(len(s2)):
        pos = ord(s2[i]) - ord('a')
        c2[pos] += 1

    j = 0
    still_ok = True
    while j < 26 and still_ok:
        if c1[j] == c2[j]:
            j += 1
        else:
            still_ok = False

    return still_ok


def main():
    string_1 = 'heart'
    string_2 = 'earth'

    isanagram = anagram_solution_1(string_1, string_2)
    print isanagram
    isanagram = anagram_solution_2(string_1, string_2)
    print isanagram
    isanagram = anagram_solution_3(string_1, string_2)
    print isanagram

if __name__ == '__main__':
    main()

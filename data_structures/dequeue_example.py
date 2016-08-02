"""
This exercise can be found at
http://interactivepython.org/runestone/static/pythonds/BasicDS/ImplementingaDequeinPython.html
"""


class Deque:
    def __init__(self):
        self.items = []

    def add_front(self, item):
        self.items.append(item)

    def add_rear(self, item):
        self.items.insert(0, item)

    def remove_front(self):
        return self.items.pop()

    def remove_rear(self):
        return self.items.pop(0)

    def is_empty(self):
        return self.items == []

    def size(self):
        return len(self.items)


def palindrome_checker(astring):
    chardeque = Deque()

    for ch in astring:
        chardeque.add_rear(ch)

    still_equal = True

    while chardeque.size() > 1 and still_equal:
        first = chardeque.remove_front()
        last = chardeque.remove_rear()

        if first != last:
            still_equal = False

    return still_equal


def main():
    print(palindrome_checker("lsdkjfskf"))
    print(palindrome_checker("radar"))


if __name__ == "__main__":
    main()

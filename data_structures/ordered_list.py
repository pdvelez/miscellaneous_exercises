"""
This exercise can be found at
http://interactivepython.org/runestone/static/pythonds/BasicDS/ImplementinganOrderedList.html
"""

from unordered_list import Node


class OrderedList:
    def __init__(self):
        self.head = None

    def search(self, item):
        current = self.head
        found = False
        stop = False
        while current is not None and not found and not stop:
            if current.get_data() == item:
                found = True
            else:
                if current.get_data() > item:
                    stop = True
                else:
                    current = current.get_next()

        return found

    def add(self, item):
        current = self.head
        previous = None
        stop = False
        while current is not None and not stop:
            if current.get_data() > item:
                stop = True
            else:
                previous = current
                current = current.get_next()

        temp = Node(item)
        if previous is None:
            temp.set_next(self.head)
            self.head = temp
        else:
            temp.set_next(current)
            previous.set_next(temp)

    def size(self):
        current = self.head
        count = 0
        while current is not None:
            count += 1
            current = current.get_next()

        return count

    def is_empty(self):
        return self.head is None


def main():
    mylist = OrderedList()
    mylist.add(31)
    mylist.add(77)
    mylist.add(17)
    mylist.add(93)
    mylist.add(26)
    mylist.add(54)

    print(mylist.size())
    print(mylist.search(93))
    print(mylist.search(100))


if __name__ == '__main__':
    main()

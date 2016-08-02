"""
This exercise can be found at
http://interactivepython.org/runestone/static/pythonds/BasicDS/ImplementingaQueueinPython.html
"""

from stack_example import Stack


class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        return self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def isEmpty(self):
        return self.items == []

    def size(self):
        return len(self.items)


class QueueUsingStacks:
    def __init__(self):
        self.stack_in = Stack()
        self.stack_out = Stack()

    def enqueue(self, item):
        while not self.stack_out.isEmpty:
            self.stack_in.push(self.stack_out.pop())
        self.stack_in.push(item)

    def dequeue(self):
        while not self.stack_in.isEmpty():
            self.stack_out.push(self.stack_in.pop())
        return self.stack_out.pop()

    def isEmpty(self):
        return self.stack_in.isEmpty() & self.stack_out.isEmpty()

    def size(self):
        if self.stack_in.isEmpty():
            return self.stack_out.size()
        if self.stack_out.isEmpty():
            return self.stack_in.size()


def main():
    q = Queue()
    p = QueueUsingStacks()

    q.enqueue('first in')
    q.enqueue(4)
    q.enqueue('dog')
    q.enqueue(True)

    p.enqueue('first in')
    p.enqueue(4)
    p.enqueue('dog')
    p.enqueue(True)

    print(q.isEmpty())
    print(q.size())
    print(q.dequeue())
    print(q.size())
    print(q.dequeue())
    print(q.size())

    print(p.isEmpty())
    print(p.size())
    print(p.dequeue())
    print(p.size())
    print(p.dequeue())
    print(p.size())


if __name__ == "__main__":
    main()

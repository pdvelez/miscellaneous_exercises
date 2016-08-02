"""
This exercise can be found at
http://interactivepython.org/runestone/static/pythonds/BasicDS/ImplementingaStackinPython.html
"""


class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def size(self):
        return len(self.items)


def revstring(mystr):
    s = Stack()

    for i in range(len(mystr)):
        s.push(mystr[i])

    outstr = ""
    for i in range(s.size()):
        outstr += str(s.pop())

    return outstr


def matches(open, close):
    opens = "([{"
    closers = ")]}"
    return opens.index(open) == closers.index(close)


def par_checker(symbolString):
    s = Stack()
    balanced = True
    index = 0
    while index < len(symbolString) and balanced:
        symbol = symbolString[index]
        if symbol in "([{":
            s.push(symbol)
        else:
            if s.isEmpty():
                balanced = False
            else:
                top = s.pop()
                if not matches(top, symbol):
                    balanced = False

        index += 1

    if balanced and s.isEmpty():
        return True
    else:
        return False


def main():
    s = Stack()

    print(s.isEmpty())
    s.push(4)
    s.push('dog')
    print(s.peek())
    s.push(True)
    print(s.size())
    print(s.isEmpty())
    s.push(8.4)
    print(s.pop())
    print(s.pop())
    print(s.size())

    print(revstring('dog'))

    print(par_checker('((()))'))
    print(par_checker('(()'))
    print(par_checker('{{([][])}()}'))
    print(par_checker('[{()]'))

if __name__ == '__main__':
    main()

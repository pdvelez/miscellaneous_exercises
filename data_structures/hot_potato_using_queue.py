"""
This exercise can be found at
http://interactivepython.org/runestone/static/pythonds/BasicDS/SimulationHotPotato.html
"""

from queue_example import Queue


def hot_potato(namelist, num):
    simqueue = Queue()

    for name in namelist:
        simqueue.enqueue(name)

    while simqueue.size() > 1:
        for i in range(num):
            simqueue.enqueue(simqueue.dequeue())

        simqueue.dequeue()

    return simqueue.dequeue()


def main():
    print(hot_potato(["Bill", "David", "Susan", "Jane", "Kent", "Brad"], 7))
    pass


if __name__ == "__main__":
    main()

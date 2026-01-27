'Create a Counter class that keeps track of how many objects have been created using a class variable.'

class Counter:
    count = 0

    def __init__(self):
        Counter.count += 1

c1 = Counter()
c2 = Counter()
print(Counter.count)
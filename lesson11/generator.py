import random


def gen():
    i = 2
    while True:

            # i = random.randint(1, 100)
        yield i
        i += 1000


for i in gen():
    print(i)

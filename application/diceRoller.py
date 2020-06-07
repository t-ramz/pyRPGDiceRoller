import random
import time

min = 1
max = 8

print random.randint(min, max)


random.seed(time.time())


# D10 code

def d10():
    print(random.randint(1, 10))


d10()

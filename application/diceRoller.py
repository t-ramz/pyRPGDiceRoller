import random
import time

# D8 code
min = 1
max = 8

print(random.randint(min, max))


random.seed(time.time())

# DVirgil code
min = 1
max = 50

print(random.randint(min, max))


random.seed(time.time())

# D12 code
min = 1
max = 12

print(random.randint(min, max))


random.seed(time.time())


# D10 code

def d10():
    print(random.randint(1, 10))


d10()

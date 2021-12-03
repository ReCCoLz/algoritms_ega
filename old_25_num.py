import time
import math
start_time = time.time()


def divisors(number: int):
    if math.sqrt(number) != int(math.sqrt(number)):
        return False
    cnt = 0
    mem = 0
    for i in range(2, int(number ** 0.5)):
        if number % i == 0:
            if cnt == 0:
                cnt += 1
                mem = i
            else:
                return False
    if mem > 0:
        return number // mem
    else:
        return False


a = 289123456
b = 389123456

for i in range(a, b + 1):
    d = divisors(i)
    if d > 0:
        print(i, d)
print("%s секунд" % (time.time() - start_time))

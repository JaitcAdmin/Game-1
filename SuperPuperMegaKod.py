import random
import time

i = 0


def sokratit(x, y):
    for i in range(1, y):
        if x % i == 0 and y % i == 0:
            return [int(x / i), int(y / i)]
    return [x, y]


print("|" + ("---" * 30) + "|")
print(f"      x               y                x+y                 x-y              x*y")
print("|" + ("---" * 30) + "|")
while True:
    a = int(random.random() * 10) + 1
    b = int(a * (random.random() * 1.5 + 1))
    c = int(random.random() * 10) + 1
    d = int(a * (random.random() * 1.5 + 1))
    if (a * d) - (c * b) <= 0 or a == b or c == d:
        continue
    if i >= 5:
        break
    i += 1
    print(
        f"    {a} / {b}          {c} / {d}          {sokratit((a * d) + (c * b), b * d)[0]} / {sokratit((a * d) + (c * b), b * d)[1]}          {sokratit((a * d) - (c * b), b * d)[0]} / {sokratit((a * d) - (c * b), b * d)[1]}            {sokratit(a*c, b*d)[0]} / {sokratit(a*c, b*d)[1]}")
    print("|" + ("---" * 30) + "|")
    time.sleep(1)

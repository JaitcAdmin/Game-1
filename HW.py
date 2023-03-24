a = 1
b = 5
c = 7
a1 = input()
a2 = input()
a3 = input()
for i in range(1, 13):
    a += 1
    b += 1
    c += 1
    if a == a1 or a == a2 or a == a3:
        print(a)
    if b == a1 or b == a2 or b == a3:
        print(b)
    if c == a1 or c == a2 or c == a3:
        print(c)

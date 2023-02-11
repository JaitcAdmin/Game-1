i = 0


def make_normal(x, y):
    a = int(x)
    b = int(y)
    c = a / b
    a = a % b
    otv = ""
    for j in range(1, b):
        if a % j == 0 and b % j == 0:
            if a / j == 0:
                otv = f"{int(c)}"
                continue
            otv = f"{int(c)} {int(a / j)}/{int(b / j)}"
    if c == 0:
        print(a, "/", b, " (не изменяется)")
    else:
        print(otv)


while 1:
    i += 1
    type_of_sum = int(input("Какого типа пример?\n"))
    if type_of_sum == 1:
        a = int(input("Пример: \n"))
        b = int(input(f"{a}/"))
        c = int(input(f"{a}/{b} * "))
        d = int(input(f"{a}/{b} * {c}/"))
        print(F"{i}) {a}/{b} * {c}/{d} = {a}*{c} / {b}*{d} = {a * c}/{b * d}")
        if (input("Включить профессианальную обработку числа?(Да/Нет)\n") == "Да"):
            make_normal(a * c, b * d)
    elif type_of_sum == 2:
        a = int(input("Пример: \n"))
        b = int(input(F"{a} * "))
        c = int(input(F"{a} * {b}/"))
        print(F"{i}) {a} * {b}/{c} = {a}*{b}/{c} = {a * b}/{c}")
        if (input("Включить профессианальную обработку числа?(Да/Нет)\n") == "Да"):
            make_normal(a * b, c)
    elif type_of_sum == 3:
        a = int(input("Пример: \n"))
        b = int(input(f"{a} "))
        c = int(input(f"{a} {b}/"))
        d = int(input(f"{a} {b}/{c} * "))
        e = int(input(f"{a} {b}/{c} * {d}/"))
        print(F"{a} {b}/{c} * {d}/{e} = {a} * {b}/{c} * {d}/{e} = {(a * c + b) * d}/{c * e}")
        if (input("Включить профессианальную обработку числа?(Да/Нет)\n") == "Да"):
            make_normal((a * c + b) * d, c * e)
    elif type_of_sum == 4:
        a = int(input("Пример: \n"))
        b = int(input(f"{a} "))
        c = int(input(f"{a} {b}/"))
        d = int(input(f"{a} {b}/{c} * "))
        e = int(input(f"{a} {b}/{c} * {d} "))
        f = int(input(f"{a} {b}/{c} * {d} {e}/"))
        print(F"{a} {b}/{c} * {d} {e}/{f} = {a} * {b}/{c} * {e}/{f} * {d} = {(a * c + b) * f}/{(d * f + e) * b}")
        if (input("Включить профессианальную обработку числа?(Да/Нет)\n") == "Да"):
            make_normal((a * c + b) * d, (d * f) * e)
    elif type_of_sum == 5:
        a = int(input("Пример: \n"))
        b = int(input(f"{a}/"))
        make_normal(a, b)

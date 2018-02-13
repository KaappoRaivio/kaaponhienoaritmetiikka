
def lisääyksi(x):
    return x + 1


def vähennäyksi(x):
    return x - 1


def add(x, y):
    if x < 0:
        x, y = y, x
    if y < 0:
        if y == 0:
            return x
        else:
            return add(vähennäyksi(x), lisääyksi(y))
    if y == 0:
        return x
    else:
        return add(lisääyksi(x), vähennäyksi(y))


def sub(x, y):
    return add(x, mul(y, -1))


def mul(x, y):
    if y < 0:
        if y == -1:
            return x
        else:
            return mul(add(x, x), lisääyksi(y))
    if y == 1:
        return x
    else:
        return mul(add(x, x), vähennäyksi(y))

a = int(input())
b = int(input())

print(add(a, b))
print(mul(a, b))

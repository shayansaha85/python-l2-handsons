c = 0


def f2(x):
    c += 1
    b = x + c
    print(c)
    return b


try:
    print(f2(1))
    print(c)
except UnboundLocalError:
    print("UnboundLocalError")


def fib():
    a = 0
    b = 1
    i = 0
    while True:
        yield a
        i += 1
        a, b = b,a + b
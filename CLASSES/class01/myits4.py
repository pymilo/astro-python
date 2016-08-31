
def fib1(start=0,end=None,maxnum=100):
    """
    another yield example, allowing the user to start their own Fibonacci sequence
    at start (default 0)
    """
    a = start
    b = start + 1
    n_yielded = 0
    while(n_yielded < maxnum or maxnum is None) and ((end is None) or (abs(a) < abs(end))):
        yield a
        n_yielded += 1 
        a, b = b, a + b

def fib1(start=0,end=None,maxnum=100):
    """
another yield example, allowing the user to start their own fibbinoci sequence at
start (default is 0)
    """
    a = start
    b = start + 1
    n_yielded = 0
    while (n_yielded < maxnum or maxnum is None) and ((end is None) or (abs(a) < abs(end))):
        "abs needed to control against silly user starting with a negative number"
        yield a
        n_yielded += 1
        a, b = b, a + b
    
    # if we got here then we are returning instead of yielding. The countdown is finished
    # we could raise a StopException excception here...this is done for us implicitly
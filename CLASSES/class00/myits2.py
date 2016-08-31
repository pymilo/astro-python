
def countdown(start,end=0,step=1):
    i = start
    while (i >= end) or end ==None:
        yield i
        i -= step
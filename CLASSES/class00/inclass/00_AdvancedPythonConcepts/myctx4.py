
def introspect(f):
    def wrapper(*arg,**kwarg):
        print("Function name = %s" % f.__name__)
        print(" docstring = %s" % f.__doc__)
        if len(arg) > 0:
            print("   ... got passed args: %s " % str(arg))
        if len(kwarg.keys()) > 0:
            print("   ... got passed keywords: %s " % str(kwarg))
        return f(*arg,**kwarg)
    return wrapper
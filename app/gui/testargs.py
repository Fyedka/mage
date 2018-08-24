from functools import wraps


def pass_thru(func):
    def wrapper(*args, **kwargs):
        if args:
            print("args")
            print(args)
            for arg in args:
                print(arg)
        if kwargs:
            print("kwargs")
            print(kwargs.items())
            for k, v in kwargs.items():
                print(k)
                print(v)
        return func(*args, **kwargs)
    return wrapper


@pass_thru
def testfunc(x=1, y=2, *args, **kwargs):
    x = x+1
    y = y+2
    print(x)
    print(y)


testfunc(1, 2, 3, 4, 5, hi='there', you='guy')

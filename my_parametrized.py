"""
For multiple calling function with list of arguments
@parametrized from lib parametrized is not compatible in Python3 :<
Example using:

l = [[2,3], [6,7,], [8,9], [12,34]]
@expand(l)
def add(a, b):
    print("a: ", a)
    print("b: ", b)
    return a+b

add()
"""


def expand(arglist):
    def decorator(func):
        def wrapped_function(*args, **kwargs):
            for arg in arglist:
                func(*arg)
        return wrapped_function
    return decorator



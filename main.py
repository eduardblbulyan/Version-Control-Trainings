def multiply(x, y):
    try:
        return x*y
    except TypeError:
        return "Type Error"


def summer(x, y):
    try:
        return x+y
    except TypeError:
        return "Type Error"


def diver(x, y):
    try:
        return x/y
    except ZeroDivisionError:
        return "Zero division error"
    except TypeError:
        return "Type Error!"

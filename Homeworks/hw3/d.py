import functools

def counter():
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **argv):

            result = func(*args, **argv)

            return result
        return wrapper
    return decorator

@counter
def func1():
    return

if __name__ == "__main__":
    func1()
    print(func1.ncalls, func1.rdepth)

    func1()
    print(func1.ncalls, func1.rdepth)
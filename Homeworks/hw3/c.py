import time
import functools

def timeout(rps):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **argv):
            t_start = time.time()
            result = func(*args, **argv)
            t_delta = time.time() - t_start
            
            time.sleep(max(1/rps - t_delta, 0))
            return result
        return wrapper
    return decorator

@timeout(rps=5)
def func():
    pass

if __name__ == "__main__":
    t_start = time.time()
    for i in range(10):
        func()
    t_delta = time.time() - t_start
    print("{:.2f}".format(t_delta))

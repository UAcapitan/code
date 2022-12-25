
import time
import functools


def clock(func):
    @functools.wraps(func)
    def clocked(*args, **kwargs):
        t0 = time.time()
        result = func(*args, **kwargs)

        elapsed = time.time() - t0
        name = func.__name__
        args_list = []
        if args:
            args_list.append(', '.join(repr(arg) for arg in args))
        if kwargs:
            args_list.append(", ".join([f"{i}={j}" for i,j in sorted(kwargs.items())]))
        print(f"Time: {elapsed}\nName: {name}\nArgs: {', '.join(args_list)}\nResult: {result}")
        return result
    return clocked


if __name__ == "__main__":
    
    @clock
    def print_name(name, active):
        if active:
            return f"It's your name: {name}."

    print_name("John", active=True)

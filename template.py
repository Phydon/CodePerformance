import sys
import os
import time
import functools

# import profile
# import math
# import cmath
# import re
# import random
# import numpy as np
# import pandas as pd
# import matplotlib.pyplot as plt


# sys.setrecursionlimit(1000) # default recursion limit is 1000

# sys.stdin = open(os.path.join(os.path.dirname(__file__), "input.txt"), "r")
# sys.stdout = open(os.path.join(os.path.dirname(__file__), "output.txt"), "w")


def get_time(func):
    def time_wrapper():
        start = time.perf_counter()
        func()
        end = time.perf_counter()
        t = (end - start) * 1000
        print("\nTime taken:", round(t, 6), "ms", "\n")

    return time_wrapper


def debug(func):
    @functools.wraps(func)
    def wrapper_debug(*args, **kwargs):
        args_repr = [repr(a) for a in args]
        kwargs_repr = [f"{k} = {v!r}" for k, v in kwargs.items()]
        signature = ", ".join(args_repr + kwargs_repr)
        print(f"Calling {func.__name__}({signature})")
        value = func(*args, **kwargs)
        print(f"{func.__name__!r} returned {value!r}")
        return value

    return wrapper_debug


def get_info(*args):
    args_size = [sys.getsizeof(a) for a in args]
    args_location = [hex(id(a)) for a in args]
    args_type = [type(a) for a in args]
    for a, t, s, l in zip(args, args_type, args_size, args_location):
        print(f"Value: {a}")
        print(f"Type: {t}")
        print(f"Size: {s} bytes")
        print(f"Located at: {l}\n")
    return None


def get_int():
    return int(sys.stdin.readline().strip())


def get_ints():
    return map(int, sys.stdin.readline().strip().split())


def get_floats():
    return map(float, sys.stdin.readline().strip().split())


def get_int_list():
    return list(map(int, sys.stdin.readline().strip().split()))


def get_float_list():
    return list(map(float, sys.stdin.readline().strip().split()))


def get_string():
    return sys.stdin.readline().strip()


def odd_even(x):
    if x & 1:
        return True  # odd
    else:
        return False  # even


# @get_time
def main():
    ##### - - - CODE STARTS HERE - - - #####

    pass

    ##### - - - CODE ENDS HERE - - - #####


if __name__ == "__main__":
    main()
    # profile.run('main()')

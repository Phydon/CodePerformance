import sys
import math, cmath, time, functools

sys.stdin = open('pythonProjects\CompetitiveProgramming\Input.txt', 'r')
sys.stdout = open('pythonProjects\CompetitiveProgramming\Output.txt', 'w')

def get_time(func):
    def time_wrapper():
        start = time.perf_counter()
        func()
        end = time.perf_counter()
        print("\nTime taken:", end - start)
    return time_wrapper

def debug(func):
    @functools.wraps(func)
    def wrapper_debug(*args, **kwargs):
        args_repr = [repr(a) for a in args]
        kwargs_repr = [f'{k} = {v!r}' for k, v in kwargs.items()]
        signature = ', '.join(args_repr + kwargs_repr)
        print(f'Calling {func.__name__}({signature})')
        value = func(*args, **kwargs)
        print(f'{func.__name__!r} returned {value!r}')
        return value
    return wrapper_debug


def get_int():
    return int(sys.stdin.readline().strip())

def get_ints(): 
    return map(int, sys.stdin.readline().strip().split())

def get_list(): 
    return list(map(int, sys.stdin.readline().strip().split()))

def get_string(): 
    return sys.stdin.readline().strip()


@ get_time
def solve():
##### - - - CODE STARTS HERE - - - #####

   
    


##### - - - CODE ENDS HERE - - - #####


if __name__ == "__main__":
    solve()

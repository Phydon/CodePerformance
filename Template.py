import sys, time
import math, cmath

sys.stdin = open('pythonProjects\CompetitiveProgramming\Input.txt', 'r')
sys.stdout = open('pythonProjects\CompetitiveProgramming\Output.txt', 'w')

def get_time(func):
    def wrapper():
        start = time.perf_counter()
        func()
        end = time.perf_counter()
        print("\nTime taken:", end - start)
    return wrapper

def get_input():
    return sys.stdin.readline().strip()

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

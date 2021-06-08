import sys, time
import math, cmath

sys.stdin = open('pythonProjects\CompetitiveProgramming\Input.txt', 'r')
sys.stdout = open('pythonProjects\CompetitiveProgramming\Output.txt', 'w')

def get_ints(): 
    return map(int, sys.stdin.readline().strip().split())

def get_list(): 
    return list(map(int, sys.stdin.readline().strip().split()))

def get_string(): 
    return sys.stdin.readline().strip()

#a,b,c,d = get_ints()
#Arr = get_list()
#string = get_string()


def solve():
    start = time.perf_counter()
##### - - - CODE STARTS- - - #####

    
    


##### - - - CODE ENDS - - - #####
    end = time.perf_counter()
    print("\nTime taken:", end - start)


if __name__ == "__main__":
    solve()

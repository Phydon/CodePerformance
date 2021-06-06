import sys

"""
When you want to take input of particular integers of integers given in a single line:
input:          5 7 19 20
what we want:   a = 5
                b = 7
                c = 19
                d = 20
"""

def get_ints(): 
    return map(int, sys.stdin.readline().strip().split())
 
a,b,c,d = get_ints()

"""
When you want to take input of list of integers given in a single line:
input:          1 2 3 4 5 6 7 8
what we want:   Arr = [1, 2, 3, 4, 5, 6, 7, 8]
"""
def get_ints(): 
    return list(map(int, sys.stdin.readline().strip().split()))
 
Arr = get_ints()

"""
When you want to take input of string:
input:          GeeksforGeeks is the best platform to practice Coding.
what we want:   string = "GeeksforGeeks if the best platform to practice coding."
"""

def get_string(): 
    return sys.stdin.readline().strip()
 
string = get_string()

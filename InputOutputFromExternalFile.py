# Below is Pythone code for input/output
  
import sys
# For getting input from input.txt file
sys.stdin = open('Input.txt', 'r') 
  
# Printing the Output to output.txt file
sys.stdout = open('Output.txt', 'w')

#####################################Implementation########################################
import sys

sys.stdin = open('C:/Users/Hubi/Desktop/Phydon/InOut/Input/InputText.txt', 'r')
sys.stdout = open('C:/Users/Hubi/Desktop/Phydon/InOut/Output/OutputText.txt', 'w')
############################Int
def get_ints(): 
    return map(int, sys.stdin.readline().strip().split())

a,b,c,d = get_ints()
print(a, b, c, d)
###########################List
def get_ints(): 
    return list(map(int, sys.stdin.readline().strip().split()))
 
Arr = get_ints()
print(Arr)
###########################String
def get_string(): 
    return sys.stdin.readline().strip()
 
string = get_string()
print(string)
"""
example to read multiple lines:
i = 0
n = 3
for i in range(n): 
    string = get_string()
    print(string)
""" 
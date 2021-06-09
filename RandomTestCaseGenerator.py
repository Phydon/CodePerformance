import sys
from random import * 

sys.stdout = open('pythonProjects\CompetitiveProgramming\Input.txt', 'w')

# n = int(10) # fixed number
n = int(randrange(1, 10, 1)) # random number from 1 to 10 in steps = 1
maxv = int(100) # maximum generated numbers

print(n) 
print(" ".join([str(randrange(maxv)) for _ in range(n)])) 

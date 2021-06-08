import sys
from random import * 

sys.stdout = open('pythonProjects\CompetitiveProgramming\Input.txt', 'w')

###### - - GENERATE HUGE NUMBERS - - ######
# n = int(1e5) 
# maxv = int(1e9) 
############### - - END - - ###############

# n = int(10) # fixed number
n = int(randrange(0, 10, 1)) # random number from 0 to 10 in steps 1
maxv = int(100) # maximum generated numbers

print(n) 
print(" ".join([str(randrange(maxv)) for _ in range(n)])) 

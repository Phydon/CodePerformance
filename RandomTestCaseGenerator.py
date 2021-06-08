import sys
from random import * 

sys.stdout = open('pythonProjects\CompetitiveProgramming\Input.txt', 'w')

###### - - GENERATE HUGE NUMBERS - - ######
# n = int(1e5) 
# maxv = int(1e9) 
############### - - END - - ###############

n = int(randrange(0, 10, 1))
maxv = int(100)

print(n) 
print(" ".join([str(randrange(maxv)) for _ in range(n)])) 

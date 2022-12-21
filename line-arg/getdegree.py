import math
import numpy as np
import stdio
import sys

def vector():
    
    print('please input vector: ')
    matrix = np.array(stdio.readAllFloats())
    rematrix = matrix.reshape(d,1)
    return rematrix

print('Input dimension: ')
d = stdio.readInt()
a = vector()
b = vector()

a2 = a*a
b2 = b.T *b.T
c2 = a * b
i = c2.sum()
j = math.sqrt(a2.sum()) * math.sqrt(b2.sum())
k = math.acos(i/j)
print(k * 180 / math.pi)

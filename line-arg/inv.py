import numpy as np
import sympy as sp
import numpy.linalg as LA
import stdarray
import stdio
import fractions

def matrix():
    print('please input row and column: ')
    row = stdio.readInt()
    col = stdio.readInt()
    print('input matrix:')
    matrix = np.array(stdio.readAllFloats())
    rematrix = matrix.reshape(row,col)
    return rematrix

def inv(a):
    return LA.inv(a)

def main():
    Matrix = matrix()
    print(inv(Matrix))
        
main()

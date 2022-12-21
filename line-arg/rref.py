import numpy as np
import sympy as sp
import stdarray
import stdio

def matrix():
    print('please input row and column: ')
    row = stdio.readInt()
    col = stdio.readInt()
    print('input matrix:')
    matrix = sp.Matrix(stdio.readAllFloats())
    rematrix = matrix.reshape(row,col)
    return rematrix

def rref(a):
    return a.rref()

def main():
    Matrix = matrix()
    print(rref(Matrix))
        
main()

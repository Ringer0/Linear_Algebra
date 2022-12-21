import numpy as np
import stdarray
import stdio

def matrix():
    print('please input row and column: ')
    row = stdio.readInt()
    col = stdio.readInt()
    print('input matrix:')
    matrix = np.matrix(stdio.readAllFloats())
    rematrix = matrix.reshape(row,col)
    return rematrix

def main():
    print('How many matrix? ')
    n = stdio.readInt()
    box = stdarray.create1D(n)
    for i in range(n):
        box[i] = matrix()

    print(box[0]**2 / 7**2)
    print(box[0]**3 / 7**3)
        
main()

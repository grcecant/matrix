"""
A matrix will be an N sized list of 4 element lists.
Each individual list will represent an [x, y, z, 1] point.
For multiplication purposes, consider the lists like so:
x0  x1      xn
y0  y1      yn
z0  z1  ... zn
1  1        1
"""
import math

#print the matrix such that it looks like
#the template in the top comment
def print_matrix( matrix ):
    x, y, z, one_row = '', '', '', ''
    for col in matrix:
        x += str(col[0]) + ' '
        y += str(col[1]) + ' '
        z += str(col[2]) + ' '
        #add row of ones
        one_row += str(col[3]) + ' '
    print(x + '\n' + y + '\n' + z + '\n' + one_row)


#turn the paramter matrix into an identity matrix
#you may assume matrix is square
def ident( matrix ):
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            matrix[row][col] = 0
            #if row=col, assign 1
            if row == col:
                matrix[row][col] = 1


#multiply m1 by m2, modifying m2 to be the product
#m1 * m2 -> m2
def matrix_mult( m1, m2 ):
    #temp matrix with 4 rows, x cols
    res = new_matrix(rows = 4, cols = len(m2))
    #fill temp matrix
    for m2col in range(len(m2)):
        for m1row in range(len(m1[0])):
            for m1col in range(len(m1)):
                res[m2col][m1row] += m1[m1col][m1row] * m2[m2col][m1col]
    #add values of temp to m2, m2 becomes product. solution to avoid shallow clone
    for row in range(len(res)):
        for col in range(len(res[0])):
            m2[row][col] = res[row][col]


def new_matrix(rows = 4, cols = 4):
    m = []
    for c in range( cols ):
        m.append( [] )
        for r in range( rows ):
            m[c].append( 0 )
    return m

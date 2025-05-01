# numpy_intro.py
"""Python Essentials: Intro to NumPy.
<Veronica Churchill>
<MTH420>
<04/26/2024>
"""

import numpy as np

def prob1():
    A= np.array([[3, -1, 4],[1, 5, -9]])
    B= np.array([[[2, 6, -5, 3],[5,-8,9,7], [9,-3,-2,-3]]])
    matrixAB= np.dot(A, B)
    return matrixAB
    """ Define the matrices A and B as arrays. Return the matrix product AB. """
    raise NotImplementedError("Problem 1 Incomplete")


def prob2():
    A=np.array([[3,1,4],[1,5,9],[-5,3,1]])
    Asq= np.dot(A,A)
    Acub=np.dot(Asq,A)
    ans= np.multiply(Acub, -1) + np.multiply(Asq,9) - np.multiply(A,15)
    return ans
    """ Define the matrix A as an array. Return the matrix -A^3 + 9A^2 - 15A. """
    raise NotImplementedError("Problem 2 Incomplete")


def prob3():
    A=np.triu(np.ones((7,7), dtype=np.int64))
    B= np.zeros((7,7),dtype=np.int64)
    for i in range (7):
        for j in range (7):
            if j<= i:
                B[i,j]=-1
            else:
                B[i,j]=5
    AB=np.dot(A,B)
    ABA=np.dot(AB,A)
    ans=ABA.astype(np.int64)
    return ans
    
    """ Define the matrices A and B as arrays using the functions presented in
    this section of the manual (not np.array()). Calculate the matrix product ABA,
    change its data type to np.int64, and return it.
    """
    raise NotImplementedError("Problem 3 Incomplete")


def prob4(A):
    """ Make a copy of 'A' and use fancy indexing to set all negative entries of
    the copy to 0. Return the resulting array.
    Example:
        >>> A = np.array([-3,-1,3])
        >>> prob4(A)
        array([0, 0, 3])
    """
    A_copy=A.copy()    
    rows,cols=A_copy.shape
    for i in range(rows):
        for j in range(cols):
            if A_copy[i, j] < 0:
                A_copy[i, j] = 0
    return A_copy
    raise NotImplementedError("Problem 4 Incomplete")


def prob5():
    """ Define the matrices A, B, and C as arrays. Use NumPy's stacking functions
    to create and return the block matrix:
                                | 0 A^T I |
                                | A  0  0 |
                                | B  0  C |
    where I is the 3x3 identity matrix and each 0 is a matrix of all zeros
    of the appropriate size.
    """
    A = np.array([[0, 2, 4],
                  [1, 3, 5]])

    B = np.array([[3, 0, 0],
                  [3, 3, 0],
                  [3, 3, 3]])

    C = np.array([[-2, 0, 0],
                  [ 0, -2, 0],
                  [ 0,  0, -2]])

    I = np.eye(3)

    top_zero = np.zeros((3, 3))
    top_row = np.hstack([top_zero, A.T, I])

    mid_zero_1 = np.zeros((2, 2))
    mid_zero_2 = np.zeros((2, 3))
    middle_row = np.hstack([A, mid_zero_1, mid_zero_2])

    bot_zero = np.zeros((3, 2))
    bottom_row = np.hstack([B, bot_zero, C])

    block_matrix = np.vstack([top_row, middle_row, bottom_row])

    return block_matrix
    raise NotImplementedError("Problem 5 Incomplete")


def prob6(A):
    """ Divide each row of 'A' by the row sum and return the resulting array.
    Use array broadcasting and the axis argument instead of a loop.

    Example:
        >>> A = np.array([[1,1,0],[0,1,0],[1,1,1]])
        >>> prob6(A)
        array([[ 0.5       ,  0.5       ,  0.        ],
               [ 0.        ,  1.        ,  0.        ],
               [ 0.33333333,  0.33333333,  0.33333333]])
    """
    row_sums = A.sum(axis=1, keepdims=True)  
    return A / row_sums

    raise NotImplementedError("Problem 6 Incomplete")


def prob7():
    """ Given the array stored in grid.npy, return the greatest product of four
    adjacent numbers in the same direction (up, down, left, right, or
    diagonally) in the grid. Use slicing, as specified in the manual.
    """
    raise NotImplementedError("Problem 7 Incomplete")

    
"""test problem 1"""
if __name__ == "__main__":
    print(prob1())
    
"""test problem 2"""
if __name__ == "__main__":
    print(prob2())
    
"""test problem 3"""
if __name__ == "__main__":
    print(prob3())

"""test problem 4"""
if __name__ == "__main__":
    B= np.array([[3, -1, 4],[1, 5, -9]])
    print(prob4(B))
    
"""test problem 5"""
if __name__ == "__main__":
    print(prob5())
    
"""test problem 6"""
if __name__ == "__main__":
    B= np.array([[3, -1, 4],[1, 5, -9]])
    print(prob6(B))
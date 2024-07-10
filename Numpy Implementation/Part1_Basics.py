# Importing numpy as np
import numpy as np

A = np.array([[9, 1, 1],
              [4, -2, 5],
              [3, 8, 7]])

# Rank of a matrix
print("Rank of A:", np.linalg.matrix_rank(A))

# Trace of matrix A
print("\nTrace of A:", np.trace(A))

# Determinant of a matrix
print("\nDeterminant of A:", np.linalg.det(A))

# Inverse of matrix A
print("\nInverse of A:\n", np.linalg.inv(A))

# Matrix A raised to power 3
print("\nMatrix A raised to power 3:\n", np.linalg.matrix_power(A, 3))

# Eigenvalues and eigenvectors of A
eigenvalues, eigenvectors = np.linalg.eig(A)
print("\nEigenvalues of A:\n", eigenvalues)
print("\nEigenvectors of A:\n", eigenvectors)

# Norm of matrix A
print("\nNorm of A (Frobenius Norm):", np.linalg.norm(A))

#Output:
'''
Rank of A: 3

Trace of A: 14

Determinant of A: -461.00000000000006

Inverse of A:
 [[ 0.11713666 -0.0021692  -0.01518438]
 [ 0.02819957 -0.13015184  0.08893709]
 [-0.0824295   0.14967462  0.04772234]]

Matrix A raised to power 3:
 [[ 915  226  310]
 [ 666  179  486]
 [1168  730  939]]

Eigenvalues of A:
 [12.22360986  7.09325675 -5.31686661]

Eigenvectors of A:
 [[ 0.38250202  0.53864328  0.02093863]
 [ 0.40029914 -0.21149825 -0.84076726]
 [ 0.83273814 -0.8155562   0.54099167]]

Norm of A (Frobenius Norm): 15.811388300841896

'''


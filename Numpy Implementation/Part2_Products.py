# Importing numpy as np
import numpy as np

# Define two vectors
v1 = np.array([1, 2, 3])
v2 = np.array([4, 5, 9])

# Dot product of v1 and v2
dot_product = np.dot(v1, v2)
print("Dot product of v1 and v2:\n", dot_product)

# Cross product of v1 and v2
cross_product = np.cross(v1, v2)
print("Cross product of v1 and v2:\n", cross_product)


# Define two 2D matrices
A = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])

B = np.array([[9, 8, 7],
              [6, 5, 4],
              [3, 2, 1]])

# Dot product (matrix multiplication) of A and B
dot_product = np.dot(A, B)
print("Dot product (matrix multiplication) of A and B:\n", dot_product)

# Cross product of corresponding rows of A and B
cross_product = np.cross(A, B)
print("Cross product of corresponding rows of A and B:\n", cross_product)


'''

Dot product of v1 and v2:
 41
Cross product of v1 and v2:
 [ 3  3 -3]
Dot product (matrix multiplication) of A and B:
 [[ 30  24  18]
 [ 84  69  54]
 [138 114  90]]
Cross product of corresponding rows of A and B:
 [[-10  20 -10]
 [-10  20 -10]
 [-10  20 -10]]
 
 '''
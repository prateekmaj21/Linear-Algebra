# Basic Linear Algebra Operations in R

# 1. Creating Vectors and Matrices

# Creating a vector
v <- c(1, 2, 3)
print("Vector v:")
print(v)

# Creating a matrix
m <- matrix(c(1, 2, 3, 4, 5, 6), nrow=2, ncol=3)
print("Matrix m:")
print(m)

# 2. Matrix Addition and Subtraction

# Creating two matrices
A <- matrix(c(1, 2, 3, 4), nrow=2, ncol=2)
B <- matrix(c(5, 6, 7, 8), nrow=2, ncol=2)

# Matrix addition
C <- A + B
print("Matrix Addition (A + B):")
print(C)

# Matrix subtraction
D <- A - B
print("Matrix Subtraction (A - B):")
print(D)

# 3. Matrix Multiplication

# Creating two matrices
E <- matrix(c(1, 2, 3, 4), nrow=2, ncol=2)
F <- matrix(c(5, 6, 7, 8), nrow=2, ncol=2)

# Matrix multiplication
G <- E %*% F
print("Matrix Multiplication (E %*% F):")
print(G)

# 4. Matrix Transposition

# Creating a matrix
H <- matrix(c(1, 2, 3, 4, 5, 6), nrow=2, ncol=3)

# Transposing the matrix
I <- t(H)
print("Matrix Transposition (t(H)):")
print(I)

# 5. Inverse of a Matrix

# Creating a square matrix
J <- matrix(c(1, 2, 3, 4), nrow=2, ncol=2)

# Finding the inverse of the matrix
K <- solve(J)
print("Inverse of Matrix J:")
print(K)

# 6. Determinant of a Matrix

# Creating a square matrix
L <- matrix(c(1, 2, 3, 4), nrow=2, ncol=2)

# Calculating the determinant of the matrix
det_L <- det(L)
print("Determinant of Matrix L:")
print(det_L)

# 7. Eigenvalues and Eigenvectors

# Creating a square matrix
M <- matrix(c(1, 2, 2, 1), nrow=2, ncol=2)

# Calculating eigenvalues and eigenvectors
eigen_M <- eigen(M)
print("Eigenvalues of Matrix M:")
print(eigen_M$values)    # Eigenvalues
print("Eigenvectors of Matrix M:")
print(eigen_M$vectors)   # Eigenvectors

# 8. Solving Linear Systems

# Coefficient matrix
N <- matrix(c(2, 1, 1, 3), nrow=2, ncol=2)

# Right-hand side vector
b <- c(1, 2)

# Solving the linear system
x <- solve(N, b)
print("Solution to the Linear System (N %*% x = b):")
print(x)

# Python Program illustrating
# numpy.linalg.det() method
 
import numpy as np
 
# creating an array using 
# array method
A = np.array([[6, 1, 1],
              [4, -2, 5],
              [2, 8, 7]])
 
 
print("Determinant of A:" , np.linalg.det(A))

# numpy.trace()() method
 
# creating an array using 
# array method
A = np.array([[6, 6, 1],
              [4, -2, 5],
              [2, 8, 7]])
 
 
print("\nTrace of A:", np.trace(A))

'''
Determinant of A: -306.0

Trace of A: 11
'''
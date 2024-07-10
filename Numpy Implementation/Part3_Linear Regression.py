# Importing necessary libraries
import numpy as np
import matplotlib.pyplot as plt

# Generate x coordinates
x = np.arange(0, 9)

# Create matrix A with x and ones
A = np.vstack([x, np.ones(len(x))]).T

# Linearly generated sequence (y coordinates)
y = np.array([19, 20, 20.5, 21.5, 22, 23, 23, 25.5, 24])

# Obtain the parameters (slope and intercept) of the regression line using least squares
w, residuals, rank, s = np.linalg.lstsq(A, y, rcond=None)

# Generate the regression line
line = w[0] * x + w[1]

# Plotting the data points
plt.plot(x, y, 'o', label='Data points')

# Plotting the regression line
plt.plot(x, line, 'r-', label='Regression line')

print("Data points: \n", line)

# Adding title and labels
plt.title('Linear Regression using Least Squares')
plt.xlabel('X')
plt.ylabel('Y')

# Adding legend
plt.legend()

# Display the plot
plt.show()


'''

Data points: 
 [19.18888889 19.90555556 20.62222222 21.33888889 22.05555556 22.77222222
 23.48888889 24.20555556 24.92222222]
 
'''
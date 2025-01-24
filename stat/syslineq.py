import numpy as np

# coefficients of the equation

A = np.array([[2,3],[3,1]])
B = np.array([8,5])

# calculate the solution
solution=np.linalg.solve(A,B)

print(f"solution of the equation is x={solution[0]}, y={solution[1]}")
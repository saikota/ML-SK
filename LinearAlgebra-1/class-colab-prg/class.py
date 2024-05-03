import numpy as np
# myList = [1, 2, 3]
# myVector = np.array(myList)

# print(myVector)


# Addition
# vec1 = np.array([10,20,30,40,50])
# vec2 = np.array([1,2,3,4,5])
# sum = vec1+vec2
# print(sum)


# Subtraction
# vec1 = np.array([10,20,30,40,50])
# vec2 = np.array([1,2,3,4,5])
# sub = vec1-vec2
# print(sub)


# Division
# vec1 = np.array([10,20,30,40,50])
# vec2 = np.array([1,4,4,4,5])
# div = vec1/vec2
# print(div)

# magnitude of vector
# from math import sqrt
# vec = np.array([3,4])
# magnitude = 
# print(f"magnitude of vector {vec} is {magnitude}")


# import numpy as np
# A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# AInv = np.linalg.inv(A)
# print(AInv)


# v1 = np.array([1, 2, 3])
# v2 = np.array([4, 5, 6])
# dotProduct = v1.dot(v2)
# print(dotProduct)

# print(np.cross(v1,v2))


##1 Write a Python function that takes a square matrix A as input and returns its eigenvalues and eigenvectors.
A = np.mat([[3,2],[1,0]])

eigenvalue, eigenvector = np.linalg.eig(A)

print('eigen value',eigenvalue)
print(eigenvector)


##2 Write a program which takes 2 arrays and returns the dot product  using NumPy

v1 =np.array([1, 2,3])
v2 =np.array([4,5,6])

print(v1.dot(v2))


##3 find determinant of a sq matrix 
A = np.array([[3, 7, 0], [8, 0, -2], [0, -4, -5]])
D = np.linalg.det(A)
print(round(D))

## 4
A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
rank = np.linalg.matrix_rank(A)
print('rank of matrix',rank)
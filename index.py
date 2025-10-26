# name = "Ajasa"
# if name.upper == "AJASA":
#     print('You are my namesake fam!')

import numpy as np
# a = [1,3,5]
# b = [1,2,3]
# print(a*b)

# The basics
# a = np.array([1,3,2], dtype ='int32')
# print(a)

# b = np.array([[9.0,8.0,7.0],[2.0,3.0,1.0]], dtype ='int16')
# print(b)
# # Get dimension
# print(a.ndim)
# print(b.ndim)

# # Get shape and getting type
# print(a.dtype)
# print(b.dtype)
# print(a.shape)
# print(b.shape)

# # Get size
# print(a.itemsize)
# print(b.itemsize)

# # Get total size
# print(a.nbytes)


# Accessing/Changing specific elements, rows, columns, etc.
# a = np.array([[1,2,3,4,5,6,7],[8,9,10,11,12,13,14]])
# print(a.shape)

# # get a specific element
# print(a[1,5])

# # Getting a specific row
# print(a[1, :])

# # getting a specific column
# print(a[:, 6])

# # getting a little more fancy [startindex:endindex:stepsize]
# print(a[0, 1:-5:1])

# Initializing different Types of array.
# All Zeros matrix
# print(np.zeros((2,3,4)))

# All Ones matrix
# print(np.ones((4,2,2)))

# Any number matrix 
# print(np.full((4,2,2), 19))

# Random decimal numbers
# print(np.random.rand(4,2))

# random integer values
# print(np.random.randint(40, size=(2,2)))

# Identity matrix
# print(np.identity(20))

# Class work
# output = np.ones((5,5))
# print(output)
# z = np.zeros((3,3))
# print(z)
# z[1,1] = 9
# print(z)
# output[1:4,1:4] = z
# print(output)

# Copying arrays
# a = np.array([1,2,3])
# b = a.copy()
# print(b)
# b[1] = 400
# print(a)
# print(b)
# print(a + 2)

# # Take the sin
# print(np.sin(a))

# linear algebra
# a = np.ones((2,3))
# print(a)
# b = np.full((3,2),2)
# print(b)
# print(np.matmul(a,b))

# Find the determinant
# c = np.identity(3)
# print(np.linalg.det(c))

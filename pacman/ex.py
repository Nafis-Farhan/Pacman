import numpy as np

list = [1,2,3,4,5,6]

array = np.array(list)

print(array.reshape(2, 3))

rand_matrix = np.random.rand(30, 30)

print(rand_matrix[:, 0])

matrix = np.array([[1, 2, 3], [4, 5, 6]])

vector = np.array([7, 8, 9])

print(matrix.dot( vector))
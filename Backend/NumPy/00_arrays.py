import numpy as np

l =[1, 2, 3]

a = np.array (l)

print(l)
print(a)

l2 = np.array ([[1, 2], [3, 4]])
a2 = ([1,2], [3,4])

print(l2)
print(a2)

### Arrays de ceros y unos

zeros_array = np.zeros((2,3))
ones_array = np.ones((3,2))

print("Zeros array:\n", zeros_array)
print("Ones Arrays:\n", ones_array)

## Arrays de rangos

range_array = np.arange(10)
print("Range Array:", range_array)

## Arrays espaciados linealmente

linspace_array = np.linspace(0, 1, num = 5)

print("Linspace: ", linspace_array)

## Matriz identidad

identity_matrix = np.eye(4)

print("Identity Matrix:\n", identity_matrix)
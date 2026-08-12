import numpy as np
print("========== Create a simple array ==========")
arr = np.array([10, 20, 30, 40])
print("arr:", arr)

print("\n ========== Create arrays using arange and linspace ==========")
print("np.arange(0, 10, 2):", np.arange(0, 10, 2))
print("np.linspace(0, 1, 5):", np.linspace(0, 1, 5))

print ("\n========== Create a 2D matrix ==========")
matrix = np.array([[1, 2, 3], [4, 5, 6]])
print("matrix:\n", matrix)

print("\n========== Special arrays ==========")
print("np.zeros((2, 3)):\n", np.zeros((2, 3)))
print("np.ones(4):", np.ones(4))
print("np.full((2, 2), 7):\n", np.full((2, 2), 7))
print("np.eye(3):\n", np.eye(3))

print("\n========== Indexing examples ==========")
a = np.array([10, 20, 30, 40, 50])
print("a[1]:", a[1])                # Single element
print("a[1:4]:", a[1:4])            # Slice
print("a[::-1]:", a[::-1])          # Reverse

print("\n========== 2D indexing ==========")
m = np.array([[1, 2, 3], [4, 5, 6]])
print("m[0, 2]:", m[0, 2])          # Single element
print("m[:, 1]:", m[:, 1])          # Column
print("m[1, :]:", m[1, :])          # Row

print("\n========== Boolean masking ==========")
scores = np.array([56, 78, 92, 41, 85, 67])
mask = scores >= 60
print("mask:", mask)
print("scores[mask]:", scores[mask])

print("\n========== Reshaping ==========")
arr = np.arange(1, 7)
print("arr:", arr)
reshaped = arr.reshape(2, 3)
print("reshaped:\n", reshaped)

print("========== Fancy indexing ==========")
a = np.array([10, 20, 30, 40, 50])
idx = [0, 2, 4]
print("a[idx]:", a[idx])

print("\n========== Flattening ==========")
m = np.array([[1, 2, 3], [4, 5, 6]])
print("m.flatten():", m.flatten())

print("\n========== Reshape with -1 (auto dimension) ==========")
print("arr.reshape(-1, 2):\n", arr.reshape(-1, 2))

print("========== Another scores array ==========")
scores = np.array([78, 85, 92, 66, 74])
print("scores:", scores)


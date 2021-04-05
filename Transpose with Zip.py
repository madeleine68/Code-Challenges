#Use zip to transpose data from a 4-by-3 matrix to a 3-by-4 matrix.

data = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (9, 10, 11))


data_transpose=tuple(zip(*data))
print(data_transpose)

#answer: ((0, 3, 6, 9), (1, 4, 7, 10), (2, 5, 8, 11))
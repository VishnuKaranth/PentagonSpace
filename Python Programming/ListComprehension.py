squares = [x**2 for x in range(10)]
print(squares)

even = [x for x in range(20) if x % 2 == 0]
print(even)

cubes = [x**3 for x in range(10)]
print(cubes)

names = ["Alice", "Bob", "Charlie", "David"]
uppercase_names = [name.upper() for name in names]
print(uppercase_names)

lengths = [len(name) for name in names]
print(lengths)

filtered_names = [name for name in names if len(name) > 3]
print(filtered_names)

nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened = [num for sublist in nested_list for num in sublist]
print(flattened)

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
transposed = [[row[i] for row in matrix] for i in range(len(matrix[0]))]
print(transposed)